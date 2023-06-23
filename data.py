import json

data = json.load(open("data.json"))

def makeListOfAlbums(data=data):
    templist = []
    for i in data:
        templist.append(i["name"])
    return templist

def loadData(selection,data=data):
    name = data[selection]["name"]
    artist = data[selection]["artist"]
    cover = data[selection]["image"]
    bandcamp = data[selection]["bandcamp"]
    description = data[selection]["description"]
    tags = data[selection]["tags"]
    if "realartists" in data[selection]:
        realartists = data[selection]["realartists"]
    else:
        realartists = []
    return name, artist, cover, bandcamp, description, tags, realartists


def insertNewRecord(name, artist, cover, bandcamp, description, tags, realartists):
    tempdata = {
        'name': name,
        'artist': artist,
        'image': cover,
        'description': description,
        'bandcamp': bandcamp,
        'tags': tags,
        'realartists': realartists
    }
    data.append(tempdata)
    print(data)
    writeJsonFile()


def writeJsonFile(): 
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)