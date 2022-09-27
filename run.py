import uvicorn as uvicorn
from fastapi import FastAPI

from src.routers.lamoda import lamoda_router

app = FastAPI()
app.include_router(lamoda_router)

if __name__ == '__main__':
    uvicorn.run("run:app", host="0.0.0.0")
