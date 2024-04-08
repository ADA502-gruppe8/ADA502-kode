from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="API/web/templates")


# Dummy function for hashing a password
def hash_password(password: str) -> str:
    return "hashed_" + password 

@app.get("/", response_class=HTMLResponse)
def get_login_page(request: Request, msg: str = None):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/make-user")
async def make_user(username: str = Form(...), password: str = Form(...)):
    hashed_password = hash_password(password)
    # Assuming '2' is the ID for 'user' role in your database
    role_id = 2
    # Insert the new user with the user role into the database
    try:
        # Your database query to insert a new user goes here.
        # Replace the next line with your actual database operation
        # e.g., await database.execute(query, values={"username": username, "hashed_password": hashed_password, "role_id": role_id})
        pass  # Placeholder for the actual database insert operation
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Could not create user: {str(e)}")
    return RedirectResponse(url="/login", status_code=303)  # Redirecting to the login page after successful registration

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