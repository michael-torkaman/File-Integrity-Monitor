from email import contentmanager
import os


import os
from pathlib import Path

from django.forms import FilePathField
from isort import file



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


def baseline(file_paths):
    
    """ create a baseline in file named baseline.txt within the working directory
    baseline has two parts, first half contains the path to the file and second half
    contains the contents of the file. the sections will be seprated by "|".
    """
   


    for file_path in file_paths:
        
        
        with open(file_path, 'r') as f:
            content = f.read()

        with open("baseline.txt", 'a') as f:
            f.write(str(file_path) + "|" + str(content)+"\n")
        

    
        


        
baseline()
    


# f = dir_list()
# print(f)

