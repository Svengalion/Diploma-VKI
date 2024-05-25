from datetime import datetime, date

from fastapi import FastAPI, Query, Depends
from typing import Optional, List
from pydantic import BaseModel
from app.users.router import router as router_users

app = FastAPI()
app.include_router(router_users)