from fastapi import FastAPI
import uvicorn



pds = FastAPI()


@pds.get('/')
async def index():
    return {'message':'Hello Guest'}

