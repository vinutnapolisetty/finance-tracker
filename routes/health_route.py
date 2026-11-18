from fastapi import APIRouter

from schemas.health_response import HealthResponse
from services.health_service import check_application_health


router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get(
    "",
    response_model=HealthResponse,
    summary="Check application health",
    description="""
    Checks whether the Finance-Tracker application is running.
    Returns the application status and a descriptive message.
    """,
    responses={
        200: {
            "description": "Application is running successfully."
        }
    },
)
async def health_check():

    return check_application_health()