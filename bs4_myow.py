import urllib.request
from bs4 import BeautifulSoup

#ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#something = input("Press enter -")
html = urllib.request.urlopen("http://www.dr-chuck.com/page1.htm")
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
for tag in tags:
    print(tag.get('href', None))