from asyncore import write
from email import contentmanager
from importlib.resources import contents, path
from mailbox import linesep
import os


import os
from pathlib import Path
from time import sleep

from django.forms import FilePathField
from isort import file
import hashlib
import time


def action(action):
    """To decide whether the the program should start with building a baseline
    or monitor existing baseline bsaed on user input
    takes A for building baseline and B for monitorin
    the fucntion returns True if A is chosen and False if B is chosen"""

    action = action.upper()
    if action == "A":
        return True
    if action == "B":
        return False


def file_paths(path):
    """list the contents of of dir in path provided by user"""
    path = Path(path)
    file_paths = []

    file_names = os.listdir(path)
    for file_name in file_names:
        file_path = os.path.join(path, file_name)
        file_paths.append(file_path)

    if already_exists(path):
        with open("directories.txt", "a") as f:
            f.write(str(path) + "\n")

    return file_paths


def hash(file_path):

    """create a baseline in file named baseline.txt within the working directory
    baseline has two parts, first half contains the path to the file and second half
    contains the contents of the file. the sections will be seprated by "|"."""

    h = hashlib.sha512()

    with open(file_path, "r") as f:
        content = f.read()
        h.update(content.encode("utf8"))
        hash = h.hexdigest()
        return hash


def baseline(file_paths):

    baseline = []
    for file_path in file_paths:
        file_hash = hash(file_path)
        baseline.append(str(file_path) + "|" + str(file_hash))

    return baseline


def already_exists(path):
    new_baseline = []
    with open("directories.txt", "r") as f:
        contents = f.read()
        if str(path) in contents:
            return False
            print("it worked")
        else:
            return True


def write_baseline(baseline):
    with open("baseline.txt", "a") as f:
        for line in baseline:
            f.write(str(line) + "\n")


def baseline_checksum(file_paths):
    """monitor the baseline and compare the hashes with new hashes taken from the current state of the files
    and rais alerts if a file is modified"""

    # so we load the directories file.
    # extract all the filepaths in the directories file into a single list
    # loop through the list and seperate the filepathas from the file hashes
    # Load the baseline as a list and check if the current state paths and hashes actually exist in the baseline.
    # check against currnet state if any of the contents of the paths in baseline have been modified
    # check if any of the files in baseline have been removed

    current_state = []
    with open("directories.txt", "r") as f:
        lines = f.readlines()
        directories = [line.rstrip() for line in lines]
    current_state_files = 

        for line in lines:
            current_state_paths = file_paths(line)
            current_state.append(current_state_paths)
    with open("baseline.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.split("|")
            file_path = line[0]
            file_hash = line[1].rstrip()
            new_hash = hash(line[0])
            # print(f'path {file_path}\n hash {file_hash}\n newhash {new_hash}\n')

            if new_hash != file_hash:
                print(f"NewHash {new_hash}\n OG Hash {file_hash}")
                print(f"{file_path} has been changed")


path = input("provide path to files:")


filepath = file_paths(path)
baseline_checksum(filepath)


# input = file_paths()
# checksum = baseline_checksum(input)


# f = dir_list()
# print(f)
