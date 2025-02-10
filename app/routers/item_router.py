from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..services.item_service import get_all_servers
from ..schemas.item_schemas import Node
from ..db.database import get_db

router = APIRouter()


@router.get("/api/allserver")
def get_all_server_info(db: Session = Depends(get_db)):
    servers = get_all_servers(db)
    return servers