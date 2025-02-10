from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services.node_service import get_nodes_by_platform, get_power_health,batch_get_and_save_statuses,get_all_tty_node_statuses
from app.schemas.node_schemas import Node, NodeStatusResponse,TtyNodeStatus
import asyncio

router = APIRouter()


@router.get("/api/nodes_by_platform/{platform}", response_model=list[Node])
async def get_nodes(platform: str, db: Session = Depends(get_db)):
    return await get_nodes_by_platform(db, platform)


@router.get("/api/power_health/{ipmi}", response_model=NodeStatusResponse)
async def get_power_health_status(ipmi: str):
    return await get_power_health(ipmi)

@router.get("/api/nodes_status_by_platform/{platform}", response_model=bool)
async def get_and_save_nodes_status(platform: str, db: Session = Depends(get_db)):
    nodes = await get_nodes_by_platform(db, platform)
    return await batch_get_and_save_statuses(db, nodes)

@router.get("/api/tty_node_status", response_model=list[TtyNodeStatus])
def get_tty_node_statuses(db: Session = Depends(get_db)):
    return get_all_tty_node_statuses(db)