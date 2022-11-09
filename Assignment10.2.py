# Write a program to read through the mbox-short.txt and figure out the
# distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and
# then splitting the string a second time using a colon.
#  Once you have accumulated the counts for each hour,
#  print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
count = dict()

for lines in handle:
    if lines.startswith('From '):
        words = lines.split()
        time = words[5]
        hours = time[:2]
        count[hours] = count.get(hours, 0) + 1

for key, val in sorted(count.items()):
    print(key,val)
