import uvicorn

from fastapi import FastAPI

from app.api.v1.users import router as users_router
from app.core.database import Base, engine
from app.models import user  # noqa: F401

app = FastAPI()
app.include_router(users_router)


@app.on_event("startup")
def on_startup() -> None:
    Base.metadata.create_all(bind=engine)


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
