import aiohttp
import ssl
from sqlalchemy.orm import Session
from app.db.models import Node
from app.schemas.node_schemas import NodeStatusResponse,TtyNodeStatus
from ..db.models import NodeStatus
import asyncio

async def get_nodes_by_platform(db: Session, platform: str):
    return db.query(Node).filter(Node.platform == platform).all()


# async def get_power_health(ipmi: str):
#     ssl_context = ssl.create_default_context()
#     ssl_context.check_hostname = False
#     ssl_context.verify_mode = ssl.CERT_NONE
#     async with aiohttp.ClientSession() as session:
#         async with session.get(f"https://{ipmi}/api/power-health", ssl=ssl_context) as response:
#             if response.status == 200:
#                 data = await response.json()
#                 return NodeStatusResponse(**data)
#             return None

async def get_power_health(ipmi: str):
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://{ipmi}/api/power-health", ssl=ssl_context) as response:
                if response.status == 200:
                    data = await response.json()
                    return NodeStatusResponse(**data)
    except (aiohttp.ClientError, asyncio.TimeoutError):
        # 捕获网络请求错误和超时错误
        return NodeStatusResponse(
            power_status=0,
            health_state=1,
            health_CPU=1,
            health_MEM=1,
            health_PSU=1,
            health_FAN=1,
            health_HDD=1
        )
    return NodeStatusResponse(
        power_status=0,
        health_state=1,
        health_CPU=1,
        health_MEM=1,
        health_PSU=1,
        health_FAN=1,
        health_HDD=1
    )
# async def batch_get_and_save_statuses(db: Session, nodes):
#     tasks = []
#     for node in nodes:
#         task = asyncio.create_task(get_power_health(node.ipmi))
#         tasks.append((node, task))

#     for node, task in tasks:
#         status = await task
#         if status:
#             new_status = NodeStatus(
#                 node_id=node.id,
#                 power_status=status.power_status,
#                 health_state=status.health_state,
#                 health_CPU=status.health_CPU,
#                 health_MEM=status.health_MEM,
#                 health_PSU=status.health_PSU,
#                 health_FAN=status.health_FAN,
#                 health_HDD=status.health_HDD
#             )
#             db.add(new_status)
#     db.commit()
#     return True

async def batch_get_and_save_statuses(db: Session, nodes):
    tasks = []
    for node in nodes:
        task = asyncio.create_task(get_power_health(node.ipmi))
        tasks.append((node, task))

    for node, task in tasks:
        status = await task
        if status and (status.power_status == 0 or status.health_state == 1):
            new_status = NodeStatus(
                node_id=node.id,
                power_status=status.power_status,
                health_state=status.health_state,
                health_CPU=status.health_CPU,
                health_MEM=status.health_MEM,
                health_PSU=status.health_PSU,
                health_FAN=status.health_FAN,
                health_HDD=status.health_HDD
            )
            db.add(new_status)
    db.commit()
    return True

def get_all_tty_node_statuses(db: Session):
    results = db.query(
        NodeStatus.status_id,
        Node.locate,  # 查询 locate 字段
        NodeStatus.power_status,
        NodeStatus.health_state,
        NodeStatus.health_CPU,
        NodeStatus.health_MEM,
        NodeStatus.health_PSU,
        NodeStatus.health_FAN,
        NodeStatus.health_HDD,
        NodeStatus.last_check_time
    ).join(
        Node, Node.id == NodeStatus.node_id
    ).all()

    statuses = []
    for result in results:
        status = TtyNodeStatus(
            status_id=result[0],
            node_id=result[1],  # 使用 locate 字段
            power_status=result[2],
            health_state=result[3],
            health_CPU=result[4],
            health_MEM=result[5],
            health_PSU=result[6],
            health_FAN=result[7],
            health_HDD=result[8],
            last_check_time=result[9]
        )
        statuses.append(status)

    return statuses