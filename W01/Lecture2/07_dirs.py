import os

for x in os.listdir('.'):
    print (x)

for x in os.listdir('E:\\2019\\1-2019\\PIoT\\Lectures\\_code-repo\\week02\\files'):
    print (x)

# to find if the item is a file or directory

for x in os.listdir('.'):
    if os.path.isfile(x): print ('f-', x)
    elif os.path.isdir(x): print ('d-', x)
    elif os.path.islink(x): print ('l-', x)
    else: print ('---', x)

# recursive walk

for x in os.walk('.'):
    print (x)
