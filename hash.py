from base64 import encode
import hashlib

h =hashlib.sha512()

with open ("baseline.txt", 'r') as f:
    contents = f.read()
    h.update(contents.encode('utf8'))
    hash = h.hexdigest()

print(hash)


 


# inputFile = ("baseline.txt")
# openedFile = open(inputFile)
# readFile = openedFile.read()

# md5Hash = hashlib.md5(readFile)
# md5Hashed = md5Hash.hexdigest()

# sha1Hash = hashlib.sha1(readFile)
# sha1Hashed = sha1Hash.hexdigest()

# print ("File Name: %s" % inputFile)
# print ("MD5: %r" % md5Hashed)
# print ("SHA1: %r" % sha1Hashed)