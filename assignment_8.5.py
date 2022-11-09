fname = input("Enter file name: ")

if len(fname) < 1:
    fname = "mbox-short.txt"
    
fh = open(fname)
count = 0
for lines in fh:
    lines = lines.rstrip()
    words = lines.split()
    
    if len(lines) < 1:
        continue
    if words[0] != 'From':
        continue
    count += 1
    print(words[1])

print("There were", count, "lines in the file with From as the first word")

