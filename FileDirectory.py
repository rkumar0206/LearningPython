import os

# get current working directory
print("Current working directory : " + os.getcwd())

# changing directory
# os.chdir("R:\\NewPythonFolder")

# listing directory and files
print(os.listdir())
print(os.listdir("R:\\"))  # list of files and directories by specifying path

# making new directory
os.mkdir("test")
print("made a new file test")

# renaming a file
os.rename('test', 'test_renamed')
print("Renamed test to test_renamed")

# checking if the file exists or not
if os.path.exists("test_renamed"):
    print("The file exits")
else:
    print("The file doesn't exists")

# we can remove a directory using rmdir('dir_name') method and for removing a file we can
# use remove('file_name') method

os.rmdir('test_renamed')
print("'test_renamed file has been removed.")

# checking if the file exists or not
if os.path.exists("test_renamed"):
    print("The file exits")
else:
    print("The file doesn't exists")
