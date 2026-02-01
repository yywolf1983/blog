import sys

if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    print("murl.py url")
    exit()


import urllib3

http = urllib3.PoolManager()

page = http.request('GET',url)

print(page.status)

from lxml import etree
from lxml.etree import HTMLParser
from requests.utils import requote_uri,unquote
import re

html = etree.HTML(page.data,etree.HTMLParser())

ret = html.xpath('//a/@href')

name = url.split("/")
filename = unquote(name[-2])
print(filename)

fo = open(filename+".m3u8", "w")
for i in ret:
    if re.search(r'wav|flac|tar.gz|.gpg',i):
        #print(requote_uri(url)+i+"\n")
        fo.write(requote_uri(url)+i+"\n")

fo.close()
