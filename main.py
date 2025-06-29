from contextlib import asynccontextmanager
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

from core.config import settings
from core.models import Base, db_healper
from api_v1 import router as router_v1
from items_views import router as items_router
from users.views import router as user_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_healper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router=router_v1, prefix=settings.api_v1_prefix)
app.include_router(items_router)
app.include_router(user_router)

@app.get("/")
async def read_root():
    return {"Hello": "World"} 