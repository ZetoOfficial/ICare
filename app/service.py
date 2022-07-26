from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from strawberry.fastapi import GraphQLRouter

from graph.scheme import schema
from settings import load_settings

settings = load_settings()

graphql_app = GraphQLRouter(schema)

app = FastAPI()

app.include_router(graphql_app, prefix=settings.graph.endpoint)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
