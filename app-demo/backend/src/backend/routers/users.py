from typing import Annotated
from backend.models import User
from backend.routers.auth import get_current_user_from_cookie
from fastapi import APIRouter, Depends

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me")
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_user_from_cookie)],
):
    return current_user
