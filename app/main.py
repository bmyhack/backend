from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .routers import item_router,node_router

app = FastAPI()

# 挂载静态文件目录
app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(item_router.router)
app.include_router(node_router.router)

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)