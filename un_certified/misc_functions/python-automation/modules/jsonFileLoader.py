import os
import json
from tkinter import filedialog
from datetime import datetime
from pytz import timezone
from jsonpath_ng.ext import parse


mst = timezone("MST")
# print("Time in MST:", datetime.now(mst))

today = datetime.now(mst)
print("today>>>>>", today)
srcDirPath = filedialog.askdirectory()
datestring = today.strftime("%m-%d-%YT%H:%M:%S")
print("Date String>>>>>", datestring)
targetFilePath = "/Users/shivaadityagoparaju/app/lib/github/AUTOPILOT-app-offnet/resources/itential/transformations/"
targetDirName = targetFilePath + datestring + "/"
print("targetDirName>>>", targetDirName)
targetDir = os.mkdir(targetDirName)
#programNameAsFileName = "OFFNET-"

for file_name in [file for file in os.listdir(srcDirPath) if file.endswith(".json")]:
    print("file_name>>>", file_name)
    with open(os.path.join(srcDirPath, file_name), "r+") as json_file:
        json_data = json.load(json_file)
        print("json_data>>>>>>>>>>>>>", json_data)
        # text = json_file.read()
        # print('text>>>>>>>>>>>>>', text)
        originalFileName = json_data["name"]
        modifiedFileName = "OFFNET-" + originalFileName + ".jst.json"
        modifiedWfName = "OFFNET-" + originalFileName
        json_data["name"] = modifiedWfName
        print("modifiedWfName>>>", modifiedWfName)
        modifiedTargetFilePath = targetDirName + modifiedFileName
        print("modifiedTargetFilePath>>>", modifiedTargetFilePath)
        originalFileName = modifiedFileName
        print("originalFileName>>>", originalFileName)
    with open(modifiedTargetFilePath, "w") as f:
        json.dump(json_data, f)
