import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# ignore SSL cert error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# user inputs for url, iteration count and target position
url = input('Enter - ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))


print('Retrieving: ', url)

for i in range(count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    print('Retrieving: ', tags[position-1].get('href', None))
    url = tags[position-1].get('href', None)

