from fastapi.routing import APIRouter

from rz_fastapp.settings import settings

router = APIRouter()

@router.get("/health")
def health_check() -> None:
    """
    Checks the health of a project.

    It returns 200 if the project is healthy.
    """
    
    return {"message": f"Hello {settings.environment}"}
