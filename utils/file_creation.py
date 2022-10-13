import os
from os import path

def create_file(fpath):
    if not(path.isfile(fpath)):
        f = open(fpath, 'w')
        f.write("I create this File using Python File Creation")
        f.close()
        print("File Created Successfully")
    else:
        print("File Exist!")
def file_path(filename):
    path = os.path.abspath(filename)
    return path

docs = 'newtext.txt'
fp = file_path(docs)

create_file(fp)

