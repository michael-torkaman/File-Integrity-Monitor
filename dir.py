
with open ("asdf.txt", 'r') as f:
    for lines in f:
        line = lines.split("|")
        print(line[0])


