import customtkinter
import json


customtkinter.set_default_color_theme("green")

#open json file 
with open("config/configur.json") as f:
    app_conf = json.load(f)

time_pom = app_conf["time_pom"]
time_rest = app_conf["time_rest"]
long_rest = app_conf["long_rest"]
pomodor = 0
size_cycle = app_conf["size_cicle"]





