from fastapi import APIRouter
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from database import vehicles_collection, branches_collection, rentals_collection


router = APIRouter()



# Initialize templates
templates = Jinja2Templates(directory="frontend/templates")

# Add route for serving the frontend
@router.get("/", response_class=HTMLResponse)
async def serve_frontend(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.get("/auth/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("auth/login.html", {"request": request})

@router.get("/auth/register", response_class=HTMLResponse)
async def register_page(request: Request):
    return templates.TemplateResponse("auth/register.html", {"request": request})

# API endpoints for stats
@router.get("/api/stats/available-vehicles")
async def get_available_vehicles_count():
    count = vehicles_collection.count_documents({"availability_status": "AVAILABLE"})
    return count

@router.get("/api/stats/branch-count")
async def get_branch_count():
    count = branches_collection.count_documents({})
    return count

@router.get("/api/stats/active-rentals")
async def get_active_rentals_count():
    count = rentals_collection.count_documents({"rental_status": "APPROVED"})
    return count

@router.get("/vehicles")
async def vehicles_page(request: Request):
    return templates.TemplateResponse("vehicles.html", {"request": request})

@router.get("/branches")
async def branches_page(request: Request):
    return templates.TemplateResponse("branches.html", {"request": request})

