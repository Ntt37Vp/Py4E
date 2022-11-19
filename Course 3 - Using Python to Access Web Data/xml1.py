import xml.etree.ElementTree as ET

data = '''<person>
<name>Dr Chuck</name>
<phone type="intl">
    +1 734 303 4456
</phone>
<email hide="email@email.com"/>
</person>'''

tree = ET.fromstring(data)

print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
