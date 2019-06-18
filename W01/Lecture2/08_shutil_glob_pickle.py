# shutil: for more details read:
# https://docs.python.org/3/library/shutil.html

import shutil
import os
source = os.listdir(".")
destination = "files/newfolder/"
for files in source:
    if files.endswith(".txt"):
        shutil.copy(files,destination)


# globbing : another way to find out the contents of a directory

import glob

import glob
import os

CWD = os.getcwd()

for name in glob.glob(CWD+'/*'):
    print(name)

# pickling

import pickle
emp = {1:"A",2:"B",3:"C",4:"D",5:"E"}
pickling_on = open("files/Emp.txt","wb")
pickle.dump(emp, pickling_on)
pickling_on.close()

pickle_off = open("files/Emp.txt","rb")
emp = pickle.load(pickle_off)
print(emp)