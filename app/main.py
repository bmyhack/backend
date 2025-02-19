# 标准库导入
from typing import List

# 第三方库导入
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# 应用程序内部模块导入
from .routers import router

# 创建FastAPI应用实例
app = FastAPI()

# 挂载静态文件目录
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# 包含路由
app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
