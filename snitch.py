import ConfigParser
import os
import subprocess
import requests
import time


def date():
    return time.strftime("%I:%M:%S")


def main():
    script_dir = os.path.dirname(__file__)
    config_file = os.path.join(script_dir, "config/config.cnf")

    if not os.path.isfile(config_file):
        print(date() + ": Snitch config failed to load.")
        raise Exception("Config file missing")

    config = ConfigParser.ConfigParser()
    config.read(config_file)

    url = config.get("snitch", "url")
    service_names_array = config.get("snitch", "service_names").split(',')

    for service in service_names_array:
        bashCommand = "/bin/systemctl status " + service + " | grep -c \"Active: active\""

        result = subprocess.check_output(bashCommand, shell=True)

        if result == 0:
            print (date() + ": Snitch failed.")
            raise Exception("Service" + service + " is not running")

    requests.get(url)
    print(date() + ": Snitch done.")

    return

main()
