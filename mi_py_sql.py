import asyncio
from mi_py_test_lib.test.Self import Self as SelfTest

async def main():
    await SelfTest().exec()
        
if __name__ == "__main__":
    asyncio.run(main())