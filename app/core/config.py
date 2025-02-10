import os

# 配置文件，用于存储项目的各种配置信息
# 例如数据库连接信息，API 密钥等

# 数据库配置
DATABASE_URL = f"sqlite:///{os.path.join(os.path.dirname(__file__), '../db/sys.db')}"

# 其他配置
DEBUG = True