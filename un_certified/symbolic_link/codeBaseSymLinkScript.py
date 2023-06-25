# Python program to explain symlink method 
#Install the dependencies
import re
# importing os module for symlink
import os


os.chdir("/Users/shivaadityagoparaju/app/lib/github/AUTOPILOT-adapter-workmate")
current_working_directory = os.system("pwd")
print(current_working_directory);

mytext = "/Users/shivaadityagoparaju/app/lib/github/AUTOPILOT-adapter-workmate"
myex = re.compile(r"(AUTOPILOT-)")
final_str = re.sub(myex, '',mytext)
print(final_str)