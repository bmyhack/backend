import logging
import os

# 设置日志级别
LOG_LEVEL = "INFO"

# 确保日志目录存在
log_directory = os.path.join(os.path.dirname(__file__), "../logs")
os.makedirs(log_directory, exist_ok=True)

# 日志文件路径
log_file_path = os.path.join(log_directory, "app.log")

# 配置日志记录器
logging.basicConfig(
    level=LOG_LEVEL,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),  # 控制台输出
        logging.FileHandler(log_file_path)  # 文件输出
    ]
)

logger = logging.getLogger(__name__)