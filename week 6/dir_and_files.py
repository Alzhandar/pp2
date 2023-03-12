import os
from string import ascii_uppercase
# Write a Python program to list only directories, files and all directories, files in a specified path.
def listDirs(p):
    directories = []
    for x in os.scandir(path=p):
        if x.is_dir():
            directories.append(x.name)
    print(directories)
def listFiles(p):
    directories1=[]
    for x in os.scandir(path=p):
        if x.is_file():
            directories1.append(x.name)
def listDirsAndFiles(p):
    files_and_dirs = []
    for x in os.scandir(path=p):
        files_and_dirs.append(x.name)
    print(files_and_dirs)
# Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path
def checkPath(p):

    # check for existence

    exist_status = os.access(path = p, mode = os.F_OK)

    print(f"Existence: {exist_status}")

    # check for readibility 

    read_status = os.access(path = p, mode = os.R_OK)

    print(f"Readibility: {read_status}")

    # check for writability 

    write_status = os.access(path = p, mode = os.W_OK)

    print(f"Writability: {write_status}")

    # check for executability

    exec_status = os.access(path = p, mode = os.X_OK)

    print(f"Executability: {exec_status}")
# Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.
def find_file_and_directory(p):
    if os.path.exists(path=p):
        # Get the file name and directory of the path
        file_name = os.path.basename(path=p)
        directory = os.path.dirname(path=p)
        return (file_name, directory)
    else:
        print(f"The path '{p}' does not exist.")
# Write a Python program to count the number of lines in a text file.
def count_lines(fileName):
    filer=open(fileName,'r')
    return len(fileName)
# Write a Python program to write a list to a file.
def writeToFile(filename,l):
    file = open(filename, 'a')
    file.write(str(l))
    file.close()

    file = open(filename, 'r')
    print(file.read())
# Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
def generate_files():
    for ch in ascii_uppercase:
        file=open(f"./generate/{ch}.txt",'x')
        file.close()
    print("files A-Z")
# Write a Python program to copy the contents of a file to another file
def copy_file(src_file, dst_file):
    with open(src_file, 'r') as src:
        with open(dst_file, 'w') as dst:
            dst.write(src.read())
# Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.
def delete_file(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            print(f"{path} has been deleted.")
        else:
            print(f"{path} cannot be deleted: permission denied.")
    else:
        print(f"{path} does not exist.")
generate_files()