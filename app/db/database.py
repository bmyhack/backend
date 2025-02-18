from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..core.config import DATABASE_URL

# 创建数据库引擎
# engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# # 创建会话工厂
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# # 依赖项，用于获取数据库会话
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# 创建数据库引擎，添加一些额外的连接参数
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
    pool_size=10,  # 连接池大小
    max_overflow=20,  # 最大溢出连接数
    pool_timeout=30,  # 连接池获取连接超时时间
    pool_recycle=1800,  # 连接池中连接的回收时间
    echo=True  # 打印SQL语句，调试时使用
)

# 创建会话工厂
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# 依赖项，用于获取数据库会话
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
