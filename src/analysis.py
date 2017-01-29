import json
import collections
with open('data.json', 'r') as data_file:    
    data = json.load(data_file)

maxfaces = 0

for frame in data:
    if maxfaces < len(frame["faces"]):
        maxfaces = len(frame["faces"])
        
frames = []
infoPerFrame = {}

for frame in data:
    totalSadness = 0
    totalNeutral = 0
    totalContempt = 0
    totalDisgust = 0
    totalAnger = 0
    totalSurprise = 0
    totalFear = 0
    totalHappiness = 0
    
    frames.append({"frame": frame["frame"]})
    infoPerFrame.update({"attentionIndex": len(frame["faces"])/float(maxfaces)})

    for face in frame["faces"]:
       for score in face["scores"]:
            totalSadness += face["scores"]["sadness"]
            totalNeutral += face["scores"]["neutral"]
            totalContempt += face["scores"]["contempt"]
            totalDisgust += face["scores"]["disgust"]
            totalAnger += face["scores"]["anger"]
            totalSurprise += face["scores"]["surprise"]
            totalFear += face["scores"]["fear"]
            totalHappiness += face["scores"]["happiness"]

    print totalNeutral
    print len(frame["faces"])
    emotions={}
    emotions["averageSadness"] = totalSadness/float(len(frame["faces"]))
    emotions["averageNeutral"] = totalNeutral/float(len(frame["faces"]))
    print emotions["averageNeutral"]
    emotions["averageContempt"] = totalContempt/float(len(frame["faces"]))
    emotions["averageDisgust"] = totalDisgust/float(len(frame["faces"]))
    emotions["averageAnger"] = totalAnger/float(len(frame["faces"]))
    emotions["averageSurprise"] = totalSurprise/float(len(frame["faces"]))
    emotions["averageFear"] = totalFear/float(len(frame["faces"]))
    emotions["averageHappiness"] = totalHappiness/float(len(frame["faces"]))
    
    infoPerFrame.update(emotions)       
    frames[int(frame["frame"])].update(infoPerFrame)

with open('result.json', 'w+') as file:
    json.dump(frames, file, indent=4)

