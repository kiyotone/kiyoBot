import os
import json
if os.path.exists(os.getcwd() +"/config.json"):

    with open("./config.json") as f:
        configData = json.load(f)
        print(configData["TOKEN"])


else:
    print("NO token found")
    pass