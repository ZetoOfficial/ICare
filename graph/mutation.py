from strawberry import mutation, type

from graph.descriptions import *


@type
class Mutation:
    @mutation(description=TEST_MUTATION)
    async def send_text(self, text: str) -> str:
        return text
