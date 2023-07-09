import json

import aioredis
from decouple import config
from src.state import state

from database.database import Connection
from routers.auth.router import router as auth_router
from routers.category.router import router as category_router
from routers.products.router import router as product_router
from routers.cart.router import router as cart_router

from starlette.middleware.cors import CORSMiddleware

from fastapi import FastAPI
from fastapi.requests import Request


app = FastAPI(
    title='Test task'
)

origins = ["*"]
# origins = [""]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(auth_router)
app.include_router(category_router)
app.include_router(product_router)
app.include_router(cart_router)


@app.on_event('startup')
async def startup():
    state.pgdb = Connection()
    await state.pgdb.create_pool(f'postgresql://{config("PG_USER")}:{config("PG_PASSWORD")}@{config("PG_HOST")}/{config("PG_NAME")}')
    state.redis = aioredis.Redis(host='localhost', port=6379)


@app.on_event("shutdown")
async def shutdown():
    await state.pgdb.close_pool()
    await state.redis.close()
































