from jikanpy import Jikan
import json
import time


def writeToLocal(filename, res):
    json.dump(res, open(filename, 'w'))


def openFromLocal(filename):
    data = json.load(open(filename))
    return data
    
def compileTop(res):
    topDict = {
        "A":{},
        "B":{},
        "C":{},
        "D":{},
        "E":{},
        "F":{},
        "G":{},
        "H":{},
        "I":{},
        "J":{},
        "K":{},
        "L":{},
        "M":{},
        "N":{},
        "O":{},
        "P":{},
        "Q":{},
        "R":{},
        "S":{},
        "T":{},
        "U":{},
        "V":{},
        "W":{},
        "X":{},
        "Y":{},
        "Z":{}
    }

    for i in res:
        title = i['title_english']
        if not title:
            title = i['title']
        rank = i['rank']
        try:
            alpha = title[0].upper()
        except Exception as e:
            print(e)
            print(i)

        try:
            if topDict[alpha]['rank'] > rank:
                topDict[alpha] = i
        except:
            if alpha in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" and rank:
                topDict[alpha] = i
            

    for a in topDict:
        try:
            if topDict[a]['title_english']:
                print(f"{a}: {topDict[a]['title_english']} - #{topDict[a]['rank']}")
            else:
                print(f"{a}: {topDict[a]['title']} - #{topDict[a]['rank']}")
        except:
            print(f"{a}: Skipped...")


def consumeAPI(pages=2):
    jikan = Jikan()
    topAnime = []
    for i in range(1, pages+1):
        try:
            topAnime += jikan.top(type='anime', page=i)['data']
        except:
            print("Rate limited. Waiting a while before sending request...")
            time.sleep(5)
            topAnime += jikan.top(type='anime', page=i)['data']
        time.sleep(0.5)
    return topAnime

def main():
    filename = 'topanime.json'

    try:
        topAnime = openFromLocal(filename)
    except:
        print('Local file is not found, creating...')
        topAnime = consumeAPI(pages=20)
        writeToLocal(filename, topAnime)
        print(f"Local file created. It can be found at {filename}.")

    compileTop(topAnime)

if __name__ == "__main__":
    main()