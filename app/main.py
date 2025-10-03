from fastapi import FastAPI
from .routers import rest, graphql

app = FastAPI(title="API de Alumnos con FastAPI y REST")

app.include_router(rest.router)
app.include_router(graphql.graphql_app, prefix="/graphql")
