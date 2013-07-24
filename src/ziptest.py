'''
Created on Jul 24, 2013

@author: jasku
'''
from zipfile import ZipFile
import re
expression = 'mods/jammyfurniture/gui/\w*er.png'
zf = ZipFile('zip.zip')
files = zf.infolist()
toExtract = []
for entry in files:
    if re.match(expression, entry.filename):
        toExtract.append(entry)
zf.extractall('extracted/', toExtract)