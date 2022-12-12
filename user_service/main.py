from fastapi import FastAPI
from router import router
from auth.router import router as auth_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(

)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix='/v1')

app.include_router(auth_router, prefix='/v1')
