import os

acc = 0
deletions = 0

print("Do you want to delete copies? Y/N?")
copy = input()

print("What file(s) would you like to remove? \nIf you are removing copies, please type in the full filename.")
user = input()

print("What file type?")
type = input()

basepath = "C:\\Users\\raifa\\Downloads"

if copy == "Y":
    for filename in os.listdir(basepath):
        if user in filename and (user + type) != filename:
            file_path = basepath + '\\' + filename
            print(file_path)
            if os.path.isfile(file_path):
                os.remove(file_path)
                print("File has successfully been deleted.")
                print("")
                acc += 1
        elif (user + type) == filename:
            acc += 1
            if acc == 1:
                print("There are no copies of this file.")
else:
    for filename in os.listdir(basepath):
        if user in filename and type in filename:
            file_path = basepath + '\\' + filename
            print(file_path)
            if os.path.isfile(file_path):
                os.remove(file_path)
                print("File has successfully been deleted.")
                print("")
                deletions += 1
        else:
            acc += 1
            if acc == len(os.listdir(basepath)) + deletions:
                print("This file does not exist.")
