from pydantic import BaseModel


class NodeBase(BaseModel):
    customer: str
    locate: str
    platform: str
    supplier: str
    devicetype: str
    serialnumber: str
    ipmi: str
    timestamp: int


class NodeCreate(NodeBase):
    pass


class Node(NodeBase):
    id: int

    class Config:
        from_attributes = True


class NodeStatusResponse(BaseModel):
    power_status: int
    health_state: int
    health_CPU: int
    health_MEM: int
    health_PSU: int
    health_FAN: int
    health_HDD: int

class TtyNodeStatus(BaseModel):
    status_id: int
    node_id: str
    power_status: int
    health_state: int
    health_CPU: int
    health_MEM: int
    health_PSU: int
    health_FAN: int
    health_HDD: int
    last_check_time: int

    class Config:
        from_attributes = True