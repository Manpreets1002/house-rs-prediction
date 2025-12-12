import logging
import os
from src.helper import TIMESTAMP

LOG_PATH = f"{TIMESTAMP}.log"

log_file_path = os.path.join("C:\\Users\\HP\\Github\\house-rs-prediction","logs")
os.makedirs(log_file_path, exist_ok= True)

LOG_FILE_PATH = os.path.join(log_file_path,LOG_PATH)

logging.basicConfig(
    filename = LOG_FILE_PATH,
    level = logging.INFO,
    format = "[ %(asctime)s ] - %(filename)s - %(lineno)d - %(levelname)s - %(message)s"
)