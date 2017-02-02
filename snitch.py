import ConfigParser, os

config = ConfigParser.ConfigParser()
config.read("config/config.cnf")

url = config.get("snitch", "url")
service_names_array = config.get("snitch", "service_names").split(',')

for service in service_names_array:
    bashCommand = "service " + service + " status | grep \"Active: active (running)\""
    os.system(bashCommand)
