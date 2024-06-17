from fastapi import FastAPI
from app.src.users.router import router as router_users
from app.src.lections.router import router as router_lections
from app.src.tests.router import router as router_tests
from app.src.results.router import router as router_results
from app.src.courses.router import router as router_courses
from app.src.feedback.router import router as router_feedback


app = FastAPI()
app.include_router(router_users)
app.include_router(router_lections)
app.include_router(router_tests)
app.include_router(router_results)
app.include_router(router_courses)
app.include_router(router_feedback)
