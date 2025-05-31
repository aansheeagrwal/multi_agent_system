from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from api.endpoints import router as api_router
from api.home import router as home_router

app = FastAPI()

# Mount static files at /static (for CSS, JS, images etc.)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Home router to serve templates at "/"
app.include_router(home_router)

# API router under /api
app.include_router(api_router, prefix="/api")
