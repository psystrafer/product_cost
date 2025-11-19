import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.calc import router


def create_app() -> FastAPI:
    a = FastAPI()
    a.include_router(router)
    a.add_middleware(CORSMiddleware)
    return a


app = create_app()


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        reload=True,
        host="0.0.0.0",
        port=8000,
    )
