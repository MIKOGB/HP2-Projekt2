import json
import ds18x20
import onewire
import machine
import time


pico_id = machine.unique_id()


with open("config.json", "r") as config_file:
    config_data = json.load(config_file)