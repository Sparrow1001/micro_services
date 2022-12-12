from fastapi import FastAPI

from deps import init_tracer
from router import router
from prometheus_fastapi_instrumentator import Instrumentator
import mongoengine

DB_NAME = 'mydb'

app = FastAPI(

)


@app.on_event("startup")
async def startup():
    mongoengine.connect(host=f"mongodb://mongo_product:27017/{DB_NAME}", alias=DB_NAME)
    Instrumentator().instrument(app).expose(app)
    init_tracer()


@app.on_event("shutdown")
async def shutdown():
    mongoengine.disconnect(alias=DB_NAME)


@app.get('/_health')
async def health_check():
    return {
        'status': 'Ok'
    }


app.include_router(router, prefix='/v1')
