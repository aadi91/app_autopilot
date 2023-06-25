from jsonpath_ng.ext import parse
import json
import os
#cwd = os.getcwd()

file = '/Users/shivaadityagoparaju/Library/CloudStorage/OneDrive-StratfordUniversity/Aditya/DataScience/Python/MyPythonProject/GitHub/python-automation/fixtures/SiteSurveyBE-Concert_OrderStatus-UTL.json'

#open the file

with open(os.path.join(file), "r+") as data:
    json_data = json.load(data)
    
def jsonPathFinder(json_data):
  jpExpression = parse("$.[?(@.name[:] =~ 'childJob')].variables.incoming.workflow")
foundJsonData = jpExpression.find(json_data)
print('foundJsonData>>>>>>>', foundJsonData)
  return foundJsonData
