#!/usr/bin/python

import datetime
import json
import os
import console

def getJson():
    fileJson = ""
    path = os.path.join(os.path.dirname(__file__), "font.json")
    with open(path) as f:
        content = f.read()
        fileJson = json.loads(content)
    return fileJson

font = getJson()

# date = datetime.datetime.now()

def splitTime(data):
    time = []
    buffer = []
    legth = 0
    for letter in data:
        if(letter == ":" or letter == "." or letter == "["):
            pass
        else:
            time.append(int(letter))
            legth += 1

    return time, legth

space = " "

def getTime(_time):
    returnString = ""
    for h in range(0, len(font[0])):
        printLine = ""
        for index, d in enumerate(_time):
                
            printLine += font[d][h] + space
            # 0 + 1 
            if((index + 1) % 2 == 0 and (index+1) != len(_time)):
                printLine += font[10][h] + space

        returnString += printLine + '\n'
    return returnString

def getCurrentTime():
    date = str(datetime.datetime.now()).split(" ")
    time = str(date[1])
    time = time[0:time.find(".")]
    return time

def showTime(time):
    time, length = splitTime(time)

    t = getTime(time)
    console.print(t)
 
def clear():
    console.print(console.clear("screen"))

if __name__ == "__main__":
    lastTime = ""
    date = getCurrentTime()
    lastTime = date
    showTime(date)
    while(True):
        date = getCurrentTime()
        if(date != lastTime):
            lastTime = date
            clear()
            showTime(date)

    