import uvicorn
from fastapi import FastAPI

from routers import devices


app = FastAPI(title="Gazprom Neft Test")

app.include_router(devices.router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)