from fastapi import FastAPI

from routes.health_route import router as health_router


# API documentation tags
tags_metadata = [
    {
        "name": "General",
        "description": "General application information and welcome endpoints.",
    },
    {
        "name": "Health",
        "description": "Application health checks and service availability.",
    },
]


# Initialize FastAPI application
app = FastAPI(
    title="Finance-Tracker API",
    description="""
    # Finance-Tracker – AI-Powered Personal Finance Management System

    Finance-Tracker helps users manage their personal finances through
    transaction tracking, expense analysis, investments,
    savings recommendations and automated reminders.

    ## Features
    - Transaction management
    - Merchant and person classification
    - Expense and income tracking
    - Monthly financial reports
    - Investment tracking
    - Payment reminders
    - AI-powered financial insights
    """,
    version="1.0.0",
    openapi_tags=tags_metadata,
    docs_url="/docs",
    redoc_url="/redoc",
)


# Register API routers
app.include_router(health_router)


# Root endpoint
@app.get(
    "/",
    tags=["General"],
    summary="Welcome to Finance-Tracker",
    description="Returns a welcome message from the Finance-Tracker API.",
)
async def root():
    return {
        "message": "Welcome to Finance-Tracker API"
    }