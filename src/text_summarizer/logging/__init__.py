import os
import sys
import logging
from datetime import datetime 

LOG_FILE=f"{datetime.now().strftime('%d_%m_%Y__%H_%M_%S')}.log"
logging_str_formate = "[%(asctime)s: %(name)s - %(levelname)s:  %(module)s: line %(lineno)d, %(message)s]"
log_dir = "logs"
log_filepath = os.path.join(log_dir,LOG_FILE)
os.makedirs(log_dir,exist_ok=True)
logging.basicConfig(
    level= logging.INFO,
    format= logging_str_formate,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("text_summarizer_logger")
