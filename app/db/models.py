from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Node(Base):
    __tablename__ = "node"

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer = Column(String)
    locate = Column(String)
    platform = Column(String)
    supplier = Column(String)
    devicetype = Column(String)
    serialnumber = Column(String)
    ipmi = Column(String)
    timestamp = Column(Integer, default=lambda: int(
        __import__('time').time()))
    
class NodeStatus(Base):
    __tablename__ = "tty_node_status"
    status_id = Column(Integer, primary_key=True, autoincrement=True)
    node_id = Column(Integer, ForeignKey('node.id'))
    power_status = Column(Integer)
    health_state = Column(Integer)
    health_CPU = Column(Integer)
    health_MEM = Column(Integer)
    health_PSU = Column(Integer)
    health_FAN = Column(Integer)
    health_HDD = Column(Integer)
    last_check_time = Column(Integer, default=lambda: int(
        __import__('time').time()))