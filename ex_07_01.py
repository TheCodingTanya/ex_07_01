# Use words.txt as the file name
fname = input("words.txt: ", "r")
fh = open(fname)
a = fh.read().strip().upper()
print(a)
