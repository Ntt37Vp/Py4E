name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

senders = dict()

for lines in handle:
    lines = lines.rstrip()
    words = lines.split()

    if len(lines) < 1:
        continue
    if words[0] != 'From':
        continue
    senders[words[1]] = senders.get(words[1], 0) + 1

largest = -1
sender = None
for key,value in senders.items():
    if value > largest:
        largest = value
        sender = key
        
print(sender, largest)
