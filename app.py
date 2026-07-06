from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(
    title="Heritage Operations Center",
    description="Enterprise Operations Portal for Heritage",
    version="1.0.0"
)

# Static Files
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def root():
    return {
        "application": "Heritage Operations Center",
        "version": "1.0.0",
        "status": "Running"
    }
