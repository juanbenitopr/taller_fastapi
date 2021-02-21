import uvicorn
from fastapi import FastAPI

from api.routes import router
from db.connection import Base, engine

app = FastAPI()

app.include_router(router=router)

Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
