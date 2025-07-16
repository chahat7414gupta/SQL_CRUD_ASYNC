from fastapi import FastAPI
from . import models, database, routes

app = FastAPI()
app.include_router(routes.router)

@app.on_event("startup")
async def startup():
    async with database.engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)
