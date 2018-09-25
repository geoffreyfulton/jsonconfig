import json


def dumpstrm(fd):
    print(json.load(fd))

def dumpdata(filename):
    with open(filename) as json_file:
        print(json.load(json_file))

def getdata(filename):
    data = None
    if filename:
        with open(filename) as json_file:
            data = json.load(json_file)
    return data
