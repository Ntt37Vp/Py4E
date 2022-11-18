from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# ignore ssl cert errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# retrieve all tr tags

tags = soup('span')
num_list = []

for tag in tags:
    num = int(tag.contents[0])
    num_list.append(num)

print(sum(num_list))
