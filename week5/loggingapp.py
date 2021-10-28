import configparser
import logging

from logging.handlers import RotatingFileHandler
from flask import Flask, url_for

app = Flask(__name__)

@app.route("/")
def root():
    this.route = url_for(".root")
    app.longer.info("Logging a test message from " + this_route)
    return "Hello Napier from config file"

def init(app):
    config = configparser.ConfigParser()
    try:
        config_location = "etc/logging.cfg"
        config.read(config_location)

        app.config["DEBUG"] = config.get("logging", "debug")
        app.config["ip_address"] = config.get("config", "ip_address")
        app.config["port"] = config.get("config", "port")
        app.config["url"] = config.get("config", "url")

        app.config["log_file"] = config.get("logging", "name")
        app.config["log_location"] = config.get("logging", "location")
        app.config["log_level"] = config.get("logging", "level")
    except:
        print("Could not read configs from: ", config_location)

def logs(app):
    log_pathname = app.config["log_location"] + app.config["log_file"]
    file_handler = RotatingFileHandler(log_pathname, maxBytes=1024 * 1024 * 10, backupCount = 1024)
    file_handler.setLevel(app.config["log_level"] )
    formatter = logging.Formatter("%(levelname)s | %(asctime)s | %(module)s | %(funcName)s | %(message)s")
    file_handler.setFormatter(formatter)
    app.longer.setLevel( app.config["log_level"] )
    app.longer.addHandler(file_handler)

init(app)
logs(app)

if __name__ == "__main__":
    init(app)
    logs(app)
    app.run(
            host=app.config["ip_address"],
            port=int(app.config["port"]))
