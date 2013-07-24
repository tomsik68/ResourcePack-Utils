'''
Created on Jul 24, 2013

@author: Tomsik68
'''
import sys
import os
from zipfile import ZipFile
import re
import json

if __name__ == '__main__':
    pass
_version_ = '0.1'
_authors_ = 'Tomsik68'
def printHelp():
    help = '''Usage: 
    python '''+__file__+''' [-a | -e | -i | -pmm] [PARAMETERS]
Options:
    -a - Analyze - Displays information about specified resource pack
        Required parameter: Filename
        | Example: pack1.zip
    -am - Auto-Merge. Automatically merges two resource packs. Can do the work for you. BUT ONLY IN SOME CASES!
        Required parameter: Filename #1
        | Example: pack1.zip
        Required parameter: Filename #2
        | Example: pack2.zip
    -e - Extracts resources from desired pack by pattern(s)
        Required parameter: Filename
        | Example: pack1.zip
        Required parameter: Pattern(Regular Expression)
        | Example: assets/minecraft/textures/*
    -i - Installs the resource pack into your minecraft folder
        Required parameter: Filename
        | Example: pack.zip
    -pmm - Pack Metas Merge. Merges .mcmeta files from two different packs. This is useful for languages.
        Required parameter: Filename #1
        | Example: pack1.zip
        Required parameter: Filename #2
        | Example: pack2.zip
        Optional parameter: Output file
        | Example: pack.mcmeta
        | Default value: pack.mcmeta
Example:
    We have pack1.zip and pack2.zip. We want sounds from pack1 and textures from pack2.
    '''
    print help
def createPackMeta(description):
    return json.dump()
def analyze(params):
    zipFile = ZipFile(params[0])
    try:
        files = zipFile.infolist()
        mcmeta = 'pack.mcmeta'
        for entry in files:
            if entry.filename.find('pack.mcmeta') != -1:
                mcmeta = entry.filename
        metaJSON = zipFile.read(mcmeta)
        meta = json.loads(metaJSON)
        print "Pack Description: "+str(meta["pack"]["description"])
        print "Pack Version: "+str(meta["pack"]["pack_format"])
    except KeyError:
        print params[0]+" is probably invalid pack, as it doesn't contain pack.mcmeta"
def extract(params):
    patterns = []
    first = True
    for param in params:
        if not first:
            print "Pattern: " + param
            patterns.append(param)
        first = False
    zipFile = ZipFile(params[0])
    files = zipFile.infolist()
    print str(len(files)) + " files, " + str(len(patterns)) + " patterns"
    toExtract = []
    for entry in files:
        for pattern in patterns:
            if re.match(pattern, entry.filename):
                toExtract.append(entry)
    print "Extracting " + str(len(toExtract)) + " entries..."
    zipFile.extractall('myresourcepack/', toExtract)
    print "Finished!"
def install(params):
    pass
def automerge(params):
    pass
class OperatingSystem():
    def getWorkingDir(self):
        pass
    @classmethod
    def getPlatform(cls):
        name = sys.platform
        if name.find('linux') != -1 or name.find('unix') != -1:
            return Linux()
        elif name.find('win') != -1:
            return Windows()
        elif name.find('mac') != -1 or name.find('osx') != -1:
            return Mac()
class Windows(OperatingSystem):
    def getWorkingDir(self):
        pass
class Mac(OperatingSystem):
    def getWorkingDir(self):
        pass
class Linux(OperatingSystem):
    def getWorkingDir(self):
        return os.getenv('user.home', '/home/root/')
title = '------MineCraft ResourcePack inspector v' + _version_ + ' by ' + _authors_ + '------'
print title 
if len(sys.argv) < 2:
    printHelp()
# parse arguments
operation = None
parameters = []
index = 0
for arg in sys.argv:
    if index > 0:
        if arg == '-a':
            operation = analyze
        elif arg == '-am':
            operation = automerge
        elif arg == '-e':
            operation = extract
        elif arg == '-i':
            operation = install
        else:
            parameters.append(arg)
    index += 1
if operation is not None:
    operation.__call__(parameters)
dashes = ''
rang = range(len(title))
for i in rang:
    dashes += '-'
print dashes