from fastapi import HTTPException

# 自定义错误处理类
class CustomError(HTTPException):
    def __init__(self, status_code: int, detail: str):
        super().__init__(status_code=status_code, detail=detail)


# 示例错误处理函数
def handle_custom_error():
    raise CustomError(status_code=400, detail="自定义错误信息")