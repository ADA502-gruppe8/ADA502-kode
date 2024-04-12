from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from API.db.conDeconDb import Database
from passlib.context import CryptContext

app = FastAPI()
templates = Jinja2Templates(directory="API/web/templates")

# Create a password context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Function to hash a password
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

@app.get("/", response_class=HTMLResponse)
def get_login_page(request: Request, msg: str = None):
    return templates.TemplateResponse("login.html", {"request": request, "msg": msg})

@app.post("/make-user")
async def make_user(username: str = Form(...), password: str = Form(...)):
    hashed_password = hash_password(password)
    DSN = "dbname=login user=postgres password=123456aa host=host.docker.internal port=5555"
    db = Database(DSN)

    try:
        role_id = 2  # Assuming role_id 2 is for standard users
        db.cursor.execute('''
            INSERT INTO users (username, password_hash, role_id) VALUES (%s, %s, %s)
        ''', (username, hashed_password, role_id))
        db.conn.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        db.close()

    return RedirectResponse(url="/location", status_code=303)

@app.post("/login")
async def form_login(request: Request, username: str = Form(...), password: str = Form(...)):
    if username and password:
        return RedirectResponse(url="/location", status_code=303)
    else:
        return templates.TemplateResponse("login.html", {"request": request, "msg": "Please enter both username and password"})

@app.get("/location", response_class=HTMLResponse)
def get_location_page(request: Request):
    return templates.TemplateResponse("location.html", {"request": request})

@app.post("/location")
def process_location(request: Request, location: str = Form(...)):
    response = RedirectResponse(url="/show-data", status_code=303)
    response.set_cookie(key="location_data", value=location)
    return response

@app.get("/show-data", response_class=HTMLResponse)
def show_data(request: Request):
    data = {
        "items": [
            {"name": "Item 1", "value": "Some value"},
            {"name": "Item 2", "value": "Another value"},
        ]
    }
    return templates.TemplateResponse("show_data.html", {"request": request, "data": data})

@app.get("/my-page", response_class=HTMLResponse)
async def get_my_page(request: Request):
    return templates.TemplateResponse("my_page.html", {"request": request})
