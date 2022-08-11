from email import contentmanager
from importlib.resources import path
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

def file_paths():
    """list the contents of of dir in path provided by user"""
    path = input("provide path to files:")
    path = Path(path)
    file_paths = []

    file_names = os.listdir(path)
    for file_name in file_names:
        file_path = os.path.join(path, file_name)
        file_paths.append(file_path)
    return file_paths


def hash(file_path):
    
    """ create a baseline in file named baseline.txt within the working directory
    baseline has two parts, first half contains the path to the file and second half
    contains the contents of the file. the sections will be seprated by "|"."""
    
    h =hashlib.sha512()

    with open(file_path, 'r') as f:
        content = f.read()
        h.update(content.encode('utf8'))
        hash = h.hexdigest()
        return hash




def baseline(file_paths):

    baseline = []
    for file_path in file_paths:
        file_hash = hash(file_path)
        baseline.append(str(file_path)+"|"+str(file_hash))
    
    return baseline

def write_baseline(baseline):
    with open("baseline.txt", 'a') as f:
        for line in baseline:
            f.write(str(line) + "\n")


def baseline_checksum(file_path, baseline):
    """monitor the baseline and compare the hashes with new hashes taken from the current state of the files
    and rais alerts if a file is modified"""


    #so first we load the baseline
    # we seperate the file paths and the hashes and loop through them 
    # for every file address we calculate a new hash and compare it to the baseline hash
    # then we setup some alarms
    while True: 
        time.sleep(1)
        #Current state is the hash and filepaths the files to be monitored in their currnet state
        current_state = baseline(file_path)
        # for filepath_filehash in current_state:

        with open('baseline.txt', 'r') as f:
            for lines in f:
                if lines not in current_state:
                    print("file has been removed")

                    
                    
                line = lines.split("|")
                filepath = line[0]
                filehash = line[1]

                
                


            
    
        

    
        


        
file_path = file_paths()
baselines = baseline(file_path)
write_baseline(baselines)

baseline_checksum(file_path, baselines)


# f = dir_list()
# print(f)

