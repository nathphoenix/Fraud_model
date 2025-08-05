import os
import os.path
from api.app import app
from dotenv import load_dotenv
import logging



 


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


if __name__ == "__main__":
    logger_folder = "app_log/app.log"
    if not os.path.isdir("app_log"):
        os.mkdir("app_log")
    if not os.path.exists(logger_folder):
      log_file = os.path.join(os.getcwd(), 'app_log', 'app.log')
      f = open(log_file, 'a')
      f.close()
    logFormatStr = '[%(asctime)s] p%(process)s {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s'
    logging.basicConfig(format = logFormatStr, filename = logger_folder, level=logging.DEBUG)
    formatter = logging.Formatter(logFormatStr,'%m-%d %H:%M:%S')
    fileHandler = logging.FileHandler("summary.log")
    fileHandler.setLevel(logging.DEBUG)
    fileHandler.setFormatter(formatter)
    streamHandler = logging.StreamHandler()
    streamHandler.setLevel(logging.DEBUG)
    streamHandler.setFormatter(formatter)
    app.logger.addHandler(fileHandler)
    app.logger.addHandler(streamHandler)
    app.logger.info("Logging is set up.")
    app.run(host='0.0.0.0', port=80)
    
 
