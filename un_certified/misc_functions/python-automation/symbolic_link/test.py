# Python program to explain symlink method 
# importing os module for symlink
import os
import os.path
import re


src_dir = "/Users/shivaadityagoparaju/app/lib/github"
target_path = "/Users/shivaadityagoparaju/app/pronghorn/itential-premium-20202_2020.2.7/node_modules/@ctl/"


os.chdir(src_dir)
print("Current Working Directory " , os.getcwd())

rootdir = os.getcwd()

#os.chdir("/Users/shivaadityagoparaju/app/pronghorn/itential-premium-20202_2020.2.7/node_modules/@ctl")

#for file in os.listdir(rootdir):
 #   d = os.path.join(rootdir, file)
  #  if os.path.isdir(d):
   #    print('Directory Name>>>>>>>>>>>>', d)

directory_contents = os.listdir(rootdir)
print('DIRCONTENT??????', directory_contents)

for item in directory_contents:
    myex = re.compile(r"(AUTOPILOT-)")
    final_str = re.sub(myex, '', item)
    target_dir = (os.path.join(target_path, final_str))
    isdir = os.path.isdir(target_dir)
    isdirexist = os.path.exists(target_dir)
    if isdir and isdirexist:
        symlinknew = os.path.islink(target_dir)
        symlinkresult = symlinknew
        print('symlink>>>>>>>>', symlinkresult)

    #if (symlinkresult is True):
     #   print('True?????????')
    #else:
     #   print('Doesnt Exist>>>>>>>> or Not Directory>>>>>>>>>')
    
    #elif (symlinkresult is False):
     #   print('False?????????')
    #else:
     #   print('Else Block>>>>>>>>>>')

# Path 
#path = 'D:/Pycharm projects/GeeksforGeeks/Nikhil/test_nikhil.txt'
#isFile = os.path.isfile(path) 
#print(isFile)


#path_of_the_directory = os.getcwd()
#print("Files and directories in a specified path:")
#for dirname in os.listdir(path_of_the_directory):

 #   f = os.path.join(path_of_the_directory, dirname)
#if dirname():
 #       print(dirname.name)

#directory_list = os.listdir(path_of_the_directory)
#print("Files and directories in  current working directory :") 
#print(directory_list)
