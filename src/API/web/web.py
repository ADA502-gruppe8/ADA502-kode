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
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/make-user")
async def make_user(username: str = Form(...), password: str = Form(...)):
    hashed_password = hash_password(password)
    # Update the DSN with your actual database connection string details
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
    
    # Assuming you have a template named 'location.html' in your 'templates' directory
    return RedirectResponse(url="/location", status_code=303)

@app.post("/login")
async def form_login(request: Request, username: str = Form(...), password: str = Form(...)):  # Added request: Request here
    if username and password:  # Checks that username and password are not empty
        return RedirectResponse(url="/location", status_code=303)
    else:
        # If either field is empty, redirect back to the login page with a message
        return templates.TemplateResponse("login.html", {"request": request, "msg": "Fuck u mate"})

@app.get("/location", response_class=HTMLResponse)
def get_location_page(request: Request):
    return templates.TemplateResponse("location.html", {"request": request})

@app.post("/location")
def process_location(request: Request, location: str = Form(...)):
    # Here, 'location' will be a string containing either the entered location or the GPS coordinates
    # Process the location data, e.g., find the closest station or do something with the coordinates

    # After processing, you may want to pass some data to the 'show_data' page
    # You can do this by setting a cookie, using session, or appending a query parameter (less secure)
    response = RedirectResponse(url="/show-data", status_code=303)
    # Example: setting a cookie (make sure to have proper security measures for real applications)
    response.set_cookie(key="location_data", value=location)
    return response

@app.get("/show-data", response_class=HTMLResponse)
def show_data(request: Request):
    # Example data to be displayed on the page
    data = {
        "items": [
            {"name": "Item 1", "value": "Some value"},
            {"name": "Item 2", "value": "Another value"},
            # ... more data items
        ]
    }
    return templates.TemplateResponse("show_data.html", {"request": request, "data": data})

@app.get("/my-page", response_class=HTMLResponse)
async def get_my_page(request: Request):
    return templates.TemplateResponse("my_page.html", {"request": request})