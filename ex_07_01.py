# Use words.txt as the file name
fh = open("words.txt")
print(fh)

for lx in fh:
    ly = lx.rstrip()
    print(ly.upper())
