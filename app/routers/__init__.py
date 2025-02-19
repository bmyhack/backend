from pathlib import Path
from importlib import import_module
from fastapi import APIRouter

# 创建主路由器
router = APIRouter()

# 获取当前目录
current_dir = Path(__file__).parent

# 自动导入路由
for route_file in current_dir.glob("*.py"):
    if route_file.stem == "__init__":
        continue
    
    # 导入模块
    module_path = f"app.routers.{route_file.stem}"
    module = import_module(module_path)
    
    # 如果模块中有 router 属性，则将其包含到主路由器中
    if hasattr(module, "router"):
        router.include_router(module.router)