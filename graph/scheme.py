import strawberry

from graph.mutation import Mutation
from graph.query import Query

schema = strawberry.Schema(query=Query, mutation=Mutation)
