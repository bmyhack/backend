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


class Node(NodeBase):
    id: int

    class Config:
        from_attributes = True