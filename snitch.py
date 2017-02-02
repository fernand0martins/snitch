import ConfigParser
import os
import subprocess
import requests

config_file = "config/config.cnf"

if not os.path.isfile(config_file):
    raise Exception("Config file missing")

config = ConfigParser.ConfigParser()
config.read(config_file)

url = config.get("snitch", "url")
service_names_array = config.get("snitch", "service_names").split(',')

for service in service_names_array:
    bashCommand = "/bin/systemctl status " + service + " | grep -c \"Active: active\""

    result = subprocess.check_output(bashCommand, shell=True)

    if result == 0:
         raise Exception("Service" + service + " is not running")

requests.get(url)