from strawberry import field, type

from graph.descriptions import *


@type
class Query:
    @field(description=TEST_QUERY)
    async def get_info(self) -> str:
        return "hello world"
