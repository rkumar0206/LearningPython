# Opening a file
# for opening a file we use open() method
# the open() method takes two parameters i.e. fileName and mode

# There are four different methods (modes) for opening a file:

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists

# In addition you can specify if the file should be handled as binary or text mode
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

# --------------------------- Read Only Mode -----------------------------------
# open file at different location
file = open("R:\\MyFile.txt", "r")
print(file.read())  # prints the content inside the file

# read only the parts if the file
print(file.read(5))  # prints only the first 5 characters of the file

# read only one line of the file
print(file.readline())  # this will return the one line of the file.
print(file.readline())  # by writing the readline() method again you can print the next line.
file.close()

# using readlines() method returns a list of remaining lines of the entire file.
# All these reading methods return empty values when the end of file (EOF) is reached.
file = open("R:\\MyFile.txt", "r")
print(file.readlines())
file.close()

# we can read file line by line
for f in file:
    print(f)
file.close()  # closing the file.

# -------------------------------------------------------------------------------------


# ------------------------------ Writing or creating file--------------------------------

# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists

file2 = open("R:\\MyFile.txt", "a")  # it will append the text at the end of the file content
file2.write("\nThis line is appended programmatically.")
file2.close()

# if opened a file using this method, then we don't need to explicitly call the close() method of file
with open("R:\\MyFile.txt", "r") as file2:
    print(file2.read())

# we can open a file in w - write mode, which will overwrite the content of the file or will create a new file if does not exist
with open("R:\\testing_w_method.txt", "w", encoding='utf-8') as file2:
    file2.write(
        "Opening a file using w method will overwrite the content of the file.\nOr will create a new file if does not exist")

with open("R:\\testing_w_method.txt", "r") as file2:
    print(file2.read())

# -------------------------------------------------------------------------------------


# --------------------- Working with the cursor --------------------------------

# we can get the current position of the cursor by using tell() method

with open("R:\\Myfile.txt", "r", encoding='utf-8') as file:
    file.read(5)
    print("Current position of the cursor is  : " + str(file.tell()))

# Bringing the cursor position to starting point using seek() method
with open("R:\\Myfile.txt", "r", encoding='utf-8') as file:
    file.read(5)
    print("Current position of the cursor is  : " + str(file.tell()))
    print("Bringing the cursor position at 0")
    file.seek(0)
    print("Current position after using seek(0) method : " + str(file.tell()))

# -------------------------------------------------------------------------------------


# Here is the complete list of methods in text mode with a brief description:
# Credit : https://www.programiz.com/python-programming/file-operation

# Method	         Description
# close()	             Closes an opened file. It has no effect if the file is already closed.
# detach()	        Separates the underlying binary buffer from the TextIOBase and returns it.
# fileno()	            Returns an integer number (file descriptor) of the file.
# flush()	            Flushes the write buffer of the file stream.
# isatty()	            Returns True if the file stream is interactive.
# read(n)           	Reads at most n characters from the file. Reads till end of file if it is negative or None.
# readable()	    Returns True if the file stream can be read from.
# readline(n=-1)	Reads and returns one line from the file. Reads in at most n bytes if specified.
# readlines(n=-1)	Reads and returns a list of lines from the file. Reads in at most n bytes/characters if specified.
# seek(offset,from=SEEK_SET)	Changes the file position to offset bytes, in reference to from (start, current, end).
# seekable()	    Returns True if the file stream supports random access.
# tell()	                Returns the current file location.
# truncate(size=None)	Resizes the file stream to size bytes. If size is not specified, resizes to current location.
# writable()	        Returns True if the file stream can be written to.
# write(s)	        Writes the string s to the file and returns the number of characters written.
# writelines(lines)	Writes a list of lines to the file.
