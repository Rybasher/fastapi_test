from fastapi import FastAPI
from crud import user


app = FastAPI()

app.include_router(user)

