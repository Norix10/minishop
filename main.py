from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from items_views import router as items_router
from users.views import router as user_router

app = FastAPI()
app.include_router(items_router)
app.include_router(user_router)

@app.get("/")
async def read_root():
    return {"Hello": "World"}