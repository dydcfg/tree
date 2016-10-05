#!/usr/bin/env python3
import subprocess
import sys
import os
from os import listdir, walk
from os.path import isdir, isfile, dirname, abspath

# YOUR CODE GOES here

MID_LEVEL_DIR = '│   '
MID_LEVEL_SPACE = "    "
LAST_LEVEL = '├── '
LAST_LEVEL_LAST_ITEM = '└── '


def addPrefix(prefix):
    s = ""
    for x in prefix:
        s = s + x
    return s


def tree(dirPath, prefix=[]):
    if(len(prefix) == 0):
        print(dirPath)
    elements = sorted(listdir(dirPath))
    nElement = len(elements)
    nDirs = 0
    nFiles = 0
    count = 0
    for item in elements:
        count = count + 1
        if not item.startswith('.'):
            s = addPrefix(prefix)
            if(isdir(dirPath + '/' + item)):
                nDirs = nDirs + 1
                prefix.append(MID_LEVEL_DIR)
                if(count == nElement):
                    prefix[-1] = MID_LEVEL_SPACE
                    print(s + LAST_LEVEL_LAST_ITEM + item)
                else:
                    print(s + LAST_LEVEL + item)
                x, y = tree(dirPath=dirPath + '/' + item, prefix=prefix)
                nDirs = nDirs + x
                nFiles = nFiles + y
                del prefix[-1]

            else:
                nFiles = nFiles + 1
                if(count == nElement):
                    print(s + LAST_LEVEL_LAST_ITEM + item)
                else:
                    print(s + LAST_LEVEL + item)

    return nDirs, nFiles

if __name__ == '__main__':
    # just for demo
    # subprocess.run(['tree'] + sys.argv[1:])
    if len(sys.argv) == 2 and isdir(sys.argv[1]):
        nDirs, nFiles = tree(sys.argv[1])
    else:
        nDirs, nFiles = tree(".")
    print("\n" + str(nDirs) + " directories, " + str(nFiles) + " files")
