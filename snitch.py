import ConfigParser
import os

config_file = "config/config-1.cnf"

if not os.path.isfile(config_file):
    raise Exception("Config file missing")

config = ConfigParser.ConfigParser()
config.read(config_file)

url = config.get("snitch", "url")
service_names_array = config.get("snitch", "service_names").split(',')

for service in service_names_array:
    bashCommand = "service " + service + " status | grep \"Active: active (running)\""
    os.system(bashCommand)
