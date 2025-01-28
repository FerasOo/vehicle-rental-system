from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.routes_user import router as user_router
from routes.routes_vehicle import router as vehicle_router
from routes.routes_rental import router as rental_router
from routes.routes_branches import router as branch_router
from routes.routes_websocket import router as websocket_router
from routes.routes_auth import router as auth_router
from routes.routes_frontend import router as frontend_router
from kafka_config.init_kafka import init_kafka_topics
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Vehicle Rental API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add API prefix to all backend routes
app.include_router(user_router, prefix="/api")
app.include_router(vehicle_router, prefix="/api")
app.include_router(rental_router, prefix="/api")
app.include_router(branch_router, prefix="/api")
app.include_router(websocket_router)  # Keep websocket without prefix
app.include_router(auth_router)       # Keep auth without prefix
app.include_router(frontend_router)   # Keep frontend without prefix

# Mount static files
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

# Initialize Kafka topics when the application starts
@app.on_event("startup")
async def startup_event():
    init_kafka_topics()

# cd 2100503-project
# uvicorn app:app --reload