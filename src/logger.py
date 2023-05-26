# logging everything inside the file
import logging 
import os
from datatime import datetime

c= f"{datetime.now().strfile('%m_%d_%Y_%H_%M_%S')}.log"   #textfile created in this format
log_path = os.path.join(os.getcwd(),'logs',LOG_FILE) #log folder is created and every file is named after logs and the log file name
os.makedirs(logs_path,exist_ok = True)

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE )
logging.basicConfig(
filename = LOG_FILE_PATH ,
		format = "[%(asctime)s] %(lineno)d %(name)s- %(levelname)s-%(messag)s",
		level = logging.INFO
)