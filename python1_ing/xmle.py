"""parsowanie xml"""

from lxml import etree

xml = etree.parse("minilinux-rewritten.xml")

print(xml)

wlaczone = xml.xpath('.//*[@enabled="true"]')


for w in (wlaczone):
    #print(w.tag, w.attrib['enabled'])
    print(w.tag,w.get("enabled","missing"))
    print('  ',w.find("elementname").text)
    