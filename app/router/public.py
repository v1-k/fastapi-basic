from fastapi import APIRouter

router = APIRouter(
    prefix="/public",
    tags=['Public API']
)


@router.get("")
def get():
    return {"public": "public"}
