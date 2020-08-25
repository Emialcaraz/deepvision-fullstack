from typing import Dict

from app.apis.api_a.mainmod import main_func as main_func_a
from app.apis.api_b.mainmod import main_func as main_func_b
from fastapi import APIRouter, Depends
from app.core.auth import get_current_user


router = APIRouter()


@router.get("/api/anomalies/", tags=["anomalies"])
async def view_a(auth=Depends(get_current_user)):
    return main_func_a()


@router.get("/api/anomalies/csvfile", tags=["csvfile"])
async def view_b(num: int, auth=Depends(get_current_user)) -> Dict[str, int]:
    return main_func_b(num)
