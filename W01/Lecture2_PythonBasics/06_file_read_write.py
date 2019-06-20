# read whole file

f = open("files/demofile.txt", "r")
print(f.read())

# read parts of it

f1 = open("files/demofile.txt", "r")
print(f1.read(20))

# write to a file, it is "a" mode and not "w"

f2 = open("files/demofile.txt", "a")
f2.write("Quote by - Jeffrey Martín, HonorCode")

# create new files
#f = open("files/myfile.txt", "x")

# seek 

# Open a file
fo = open("files/foo.txt", "r+")
print ("Name of the file: ", fo.name)

line = fo.readlines()
print ("Read Line: %s" % (line))

# Again set the pointer to the beginning
fo.seek(0, 0)
line = fo.readline()
print ("Read Line: %s" % (line))

# Close opened file
fo.close()

