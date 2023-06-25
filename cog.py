#Below are 
import os
import json
from tkinter import filedialog
from datetime import datetime
from pytz import timezone
from jsonpath_ng.ext import parse

#Below calling modules directory to call child/dependency functions
from modules import arrayItemsMatch, jsonFileLoader



class Parent:
    def jsonPathUpdater(jsonData):
        jpExpression = parse(
                    "$.[?(@.name[:] =~ 'childJob')].variables.incoming.workflow"
                )
        for match in jsonData['tasks']:
            print("match>>>>>>>>>>", match)
            jpExpression.find(jsonData)
            targetFilePath = "/Users/shivaadityagoparaju/app/lib/github/AUTOPILOT-app-offnet/resources/itential/workflows/"
            targetDir = os.makedirs(targetFilePath, exist_ok=True)
            print("targetDirName>>>", targetDir)
            matchedValue = match.value
            print('NewMatchedValue>>>>>.?', matchedValue)
            split_strings = matchedValue.split()
            split_strings.insert(0, "OFFNET-")
            matchedValue = "".join(split_strings)
            print('NewMatchedValue2>>>>>.', matchedValue)
            # matchedValue = ("OFFNET-" + matchedValue)
            jpExpression.update(jsonData, matchedValue)
            print('jsonData2>>>>>.', jsonData)
            originalFileName = jsonData["name"]
            modifiedFileName = "OFFNET-" + originalFileName + ".json"
            modifiedTargetFilePath = targetFilePath + modifiedFileName
            print("modifiedTargetFilePath>>>", modifiedTargetFilePath)
        with open(modifiedTargetFilePath, "w") as f:
            return json.dump(jsonData, f)

            # print(json.dumps(jsonData, indent=2))
            #return json.dumps(jsonData, indent=2)

class Child(Parent):
    def jsonFileLoader():
        mst = timezone("MST")
        # print("Time in MST:", datetime.now(mst))
        #today = datetime.now(mst)
        #print("today>>>>>", today)
        srcDirPath = filedialog.askdirectory()
        #datestring = today.strftime("%m-%d-%YT%H:%M:%S")
        #print("Date String>>>>>", datestring)
        #targetFilePath = "/Users/shivaadityagoparaju/app/lib/github/AUTOPILOT-app-offnet/resources/itential/workflows/"
        #targetDir = os.makedirs(targetFilePath, exist_ok=True)
        #print("targetDirName>>>", targetDir)
        #targetDir = os.mkdir(targetDirName)
        for file_name in [
            file for file in os.listdir(srcDirPath) if file.endswith(".json")
        ]:
            print("file_name>>>", file_name)
            with open(os.path.join(srcDirPath, file_name), "r+") as json_file:
                json_data = json.load(json_file)
                print("json_data>>>>>>>>>>>>>", json_data)
                originalFileName = json_data["name"]
                modifiedFileName = "OFFNET-" + originalFileName + ".json"
                modifiedWfName = "OFFNET-" + originalFileName
                json_data["name"] = modifiedWfName
                print("modifiedWfNameData>>>", json_data)
                jsonData = json_data
                print('jsonData>>>>>>>>>>>>>>>>>>>>>', jsonData)
                callJpUpdateFn = Parent.jsonPathUpdater(jsonData)

    if __name__ == "__main__":
        jsonFileLoader()
