from sqlalchemy import Column, Integer, String, ForeignKey, CHAR, TIMESTAMP, text, UniqueConstraint, Index
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()

class Node(Base):
    __tablename__ = "nodelist"

    uuid = Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    customer = Column(String)
    locate = Column(String)
    platform = Column(String)
    supplier = Column(String)
    devicetype = Column(String)
    serialnumber = Column(String)
    ipmi = Column(String)
    timestamp = Column(Integer, default=lambda: int(__import__('time').time()))

class NodeStatus(Base):
    __tablename__ = "ts_node_status"

    ts_status_id = Column(Integer, primary_key=True, autoincrement=True)
    ts_node_id = Column(CHAR(36), ForeignKey('nodelist.uuid'), nullable=False)
    ts_power_status = Column(Integer, nullable=False, default=1)
    ts_health_state = Column(Integer, nullable=False, default=0)
    ts_health_CPU = Column(Integer, nullable=False, default=0)
    ts_health_MEM = Column(Integer, nullable=False, default=0)
    ts_health_PSU = Column(Integer, nullable=False, default=0)
    ts_health_FAN = Column(Integer, nullable=False, default=0)
    ts_health_HDD = Column(Integer, nullable=False, default=0)
    ts_last_check_time = Column(Integer, nullable=False, server_default=text('UNIX_TIMESTAMP(CURRENT_TIMESTAMP)'), onupdate=text('UNIX_TIMESTAMP(CURRENT_TIMESTAMP)'))

    __table_args__ = (
        UniqueConstraint('ts_node_id', 'ts_last_check_time', name='uk_ts_node_last_check'),
        Index('idx_ts_node_id', 'ts_node_id'),
        Index('idx_ts_last_check_time', 'ts_last_check_time'),
        {'mysql_engine': 'InnoDB'}
    )
