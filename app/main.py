from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .router import auth, protected,  public

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(protected.router)
app.include_router(public.router)
