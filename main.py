import os

print("What file(s) would you like to remove?")
user = input()

print("What file type?")
type = input()

basepath = "C:\\Users\\raifa\\Downloads"
for filename in os.listdir(basepath):
    if user in filename and type in filename:
        file_path = basepath + '\\' + filename
        print(file_path)
        if os.path.isfile(file_path):
            os.remove(file_path)
            print("File has successfully been deleted.")
            print("")
        else:
            print("This file does not exist.")

