from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from ..services.node_service import get_all_servers
from ..schemas.node_schemas import Node
from ..db.database import get_db
from ..core.logger import logger  # 假设你有一个 logger 模块

router = APIRouter()

@router.get("/api/allserver")
def get_all_server_info(db: Session = Depends(get_db)):
    try:
        servers = get_all_servers(db)
        logger.info("Successfully retrieved server information.")
        return servers
    except SQLAlchemyError as e:
        logger.error(f"Database error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")