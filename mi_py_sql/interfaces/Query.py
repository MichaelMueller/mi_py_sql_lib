from typing import Any

class Query:
    
    async def exec(self) ->  Any:
        raise NotImplementedError()