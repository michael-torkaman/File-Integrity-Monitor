

from encodings import utf_8
from importlib.resources import contents
from pathlib import Path
import hashlib



path = "C:/Users/MIchael/Documents/Projects/FIM/files/a"
contents = ""

with open(path, 'r') as f:
    cn = str(f.read())
    cntnt = str(cn)
    hash = hashlib.sha512(cntnt.encode('utf8')).hexdigest()

print(hash)

