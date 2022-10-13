# Scripts - Writing program to automate a task

import os
import time


def cur_directory():
    cwd = os.getcwd()  # cwd - Current Write Directory
    print(cwd)


def file_path(filename):
    path = os.path.abspath(filename)
    print(path)


t = time.time()  # returns seconds
docs = 'newtext.txt'
print(time.ctime(t))
cur_directory()
file_path(docs)
