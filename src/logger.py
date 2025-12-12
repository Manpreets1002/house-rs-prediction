import logging
import os
from src.helper import TIMESTAMP

LOG_PATH = f"{TIMESTAMP}.log"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_file_path = os.path.join(BASE_DIR,"logs")
os.makedirs(log_file_path, exist_ok= True)

print(log_file_path)
LOG_FILE_PATH = os.path.join(log_file_path,LOG_PATH)

logging.basicConfig(
    filename = LOG_FILE_PATH,
    level = logging.INFO,
    format = "[ %(asctime)s ] - %(filename)s - %(lineno)d - %(levelname)s - %(message)s"
)