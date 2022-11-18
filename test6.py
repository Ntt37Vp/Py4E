import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('https://data.pr4e.org/romeo.txt')

# Read the lines
# for line in fhand:
#     print(line.decode().strip())

counts = {}
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)
