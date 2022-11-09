fname = input("Enter file name: ")
fh = open(fname)
lines = list()
words = list()
for line in fh:
    lines = line.split()
    for word in lines:
        if word not in words:
            words.append(word)

words.sort()
print(words)
