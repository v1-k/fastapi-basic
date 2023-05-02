from fastapi import APIRouter, Depends
from .. import oauth2

router = APIRouter(
    prefix="/protected",
    tags=['Protected API']
)


@router.get("/")
def get(current_user: str = Depends(oauth2.get_current_user)):
    return "protected route"
