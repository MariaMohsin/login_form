from fastapi import FastAPI, Request
from fastapi.params import Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import httpx  # Optional if you're calling an external API

app = FastAPI()


templates = Jinja2Templates(directory="templates")

# GET route to show login form
@app.get("/", response_class=HTMLResponse)
async def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

# POST route to process login form
@app.post("/login", response_class=HTMLResponse)
async def login_user(
    request: Request,
    email: str = Form(...),
    password: str = Form(...),
    role: str = Form(...)
):
    # ✅ Option 1: Simulated login logic (you can replace this with an API call)
    if email == "admin@example.com" and password == "1234" and role == "admin":
        message = "✅ Login successful!"
    else:
        message = "❌ Login failed "

    return templates.TemplateResponse("login.html", {
        "request": request,
        "message": message
    })
