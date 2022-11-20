import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter location: ')
print('Retrieving ', url)
count = 0
sum = 0

url_handle = urllib.request.urlopen(url)
data = url_handle.read().decode()
print('Retrieved', len(data), 'characters')

js = json.loads(data)
items = js["comments"]

for item in items:
    # print(item["count"])
    count += 1
    sum += item["count"]

print('Count: ', count)
print('Sum: ', sum)
