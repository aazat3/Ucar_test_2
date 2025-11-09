from fastapi import FastAPI


from app.config import settings
from app.routers import incidents


app = FastAPI(title=settings.PROJECT_NAME)
app.include_router(incidents.router)


@app.get("/")
async def root():
    return {"service": settings.PROJECT_NAME, "docs": "/docs"}