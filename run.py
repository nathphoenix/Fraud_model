from app import app
from api.db import db
from api.ma import ma
from api.oa import oauth
import os
import logging
#this run.py is created for heroku platform
db.init_app(app)
    # this runs in the background and it tell that marshmallow object what flask app it should be talking to
ma.init_app(app)
oauth.init_app(app)
print('RUNNING HERE')
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


@app.before_first_request
def create_tables():
    db.create_all()