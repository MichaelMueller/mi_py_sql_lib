from typing import Optional, Any
import argparse, inspect, sys, types, os

async def run_from_command_line( funcs:list[callable] ):
    function_names = [ f.__name__ for f in funcs ]
    app_description = sys.argv[0]
    initial_parser = argparse.ArgumentParser(description=app_description)
    initial_parser.add_argument("function_name", type=str, choices=function_names, help="Name of the function to run")
    initial_args, _ = initial_parser.parse_known_args()

    # Find the function in the module
    function_name = initial_args.function_name
    func = funcs[ function_names.index(function_name) ]

    # Create a new ArgumentParser to handle the arguments for the specific function
    app_description += " " + function_name
    final_parser = argparse.ArgumentParser(description=app_description)
    final_parser.add_argument("function_name", type=str, help=function_name, choices={function_name}, default=function_name)
    
    # Use the inspect module to get the function signature and add arguments dynamically
    signature = inspect.signature(func)
    for param_name, param in signature.parameters.items():
        # Determine the argument type based on the function parameter annotation
        param_type = param.annotation if param.annotation != inspect.Parameter.empty else str
        if param.annotation is Any:
            param_type = str

        # Determine if the parameter has a default value
        if param.default != inspect.Parameter.empty:
            final_parser.add_argument(f"--{param_name}", type=param_type, default=param.default, help=f"(default: {param.default})")
        else:
            final_parser.add_argument(param_name, type=param_type)

    # Parse the full set of arguments now
    final_args = final_parser.parse_args()

    # Call the function with the parsed arguments
    func_args = vars(final_args)
    del func_args["function_name"]
    return await func(**func_args)

