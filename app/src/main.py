from fastapi import FastAPI
from app.src.users.router import router as router_users
from app.src.lections.router import router as router_lections
from app.src.tests.router import router as router_tests

app = FastAPI()
app.include_router(router_users)
app.include_router(router_lections)
app.include_router(router_tests)