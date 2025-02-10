from sqlalchemy.orm import Session
from ..db.models import Node


def get_all_servers(db: Session):
    return db.query(Node).all()