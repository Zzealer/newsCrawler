import os
from lxml import etree

path = '/media/jsir/Windows/Users/jiang/Desktop/ed HPC/ttds/project/crawler/dataset/reuters'
files = []
for r, d, f in os.walk(path):
    for file in f:
        if '.xml' in file:
            files.append(os.path.join(r, file))

for f in files:
    dom = etree.parse(f)
    xsl = etree.parse('/media/jsir/Windows/Users/jiang/Desktop/ed HPC/ttds/project/crawler/check.xsl')

# TRANSFORM XML
    transform = etree.XSLT(xsl)
    result = transform(dom)

# SAVE OUTPUT TO FILE
    with open(f, 'wb') as fi:
        fi.write(result)


