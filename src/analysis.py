import json
import collections
with open('summary.json', 'r') as data_file:    
    data = json.load(data_file)

maxfaces = 0

for frame in data:
    if maxfaces < len(frame["faces"]):
        maxfaces = len(frame["faces"])
        
frames = []
infoPerFrame = {}
videoEmotions = {"videoSadness": 0, "videoNeutral": 0, "videoContempt": 0,
                 "videoDisgust": 0, "videoAnger": 0, "videoSurprise": 0,
                 "videoFear": 0, "videoHappiness": 0}
videoDisgust = 0
videoFear = 0
videoSurprise = 0
videoSadness = 0
videoNeutral = 0
videoHappiness = 0
videoContempt = 0
videoAnger = 0

i = 0

for frame in data:
    totalSadness = 0
    totalNeutral = 0
    totalContempt = 0
    totalDisgust = 0
    totalAnger = 0
    totalSurprise = 0
    totalFear = 0
    totalHappiness = 0

    if len(frame["faces"])!=0:
        frames.append({"frame": frame["frame"]})
        infoPerFrame.update({"attentionIndex": len(frame["faces"])/float(maxfaces)})

        for face in frame["faces"]:
            totalSadness += face["scores"]["sadness"]
            totalNeutral += face["scores"]["neutral"]
            totalContempt += face["scores"]["contempt"]
            totalDisgust += face["scores"]["disgust"]
            totalAnger += face["scores"]["anger"]
            totalSurprise += face["scores"]["surprise"]
            totalFear += face["scores"]["fear"]
            totalHappiness += face["scores"]["happiness"]

        emotions={}
        emotions["averageSadness"] = format(totalSadness/float(len(frame["faces"])),'.15f')
        videoSadness += float(emotions["averageSadness"])
        emotions["averageNeutral"] = format(totalNeutral/float(len(frame["faces"])),'.15f')
        videoNeutral += float(emotions["averageNeutral"])
        emotions["averageContempt"] = format(totalContempt/float(len(frame["faces"])),'.15f')
        videoContempt += float(emotions["averageContempt"])
        emotions["averageDisgust"] = format(totalDisgust/float(len(frame["faces"])),'.15f')
        videoDisgust += float(emotions["averageDisgust"])
        emotions["averageAnger"] = format(totalAnger/float(len(frame["faces"])),'.15f')
        videoAnger += float(emotions["averageAnger"])
        emotions["averageSurprise"] = format(totalSurprise/float(len(frame["faces"])),'.15f')
        videoSurprise += float(emotions["averageSurprise"])
        emotions["averageFear"] = format(totalFear/float(len(frame["faces"])),'.15f')
        videoFear += float(emotions["averageFear"])
        emotions["averageHappiness"] = format(totalHappiness/float(len(frame["faces"])),'.15f')
        videoHappiness += float(emotions["averageHappiness"])
        
        infoPerFrame.update(emotions)       
        frames[i].update(infoPerFrame)
        i = i + 1

videoEmotions["videoDisgust"] = videoDisgust/float(len(data))
videoEmotions["videoFear"] = videoFear/float(len(data))
videoEmotions["videoSurprise"] = videoSurprise/float(len(data))
videoEmotions["videoSadness"] = videoSadness/float(len(data))
videoEmotions["videoNeutral"] = videoNeutral/float(len(data))
videoEmotions["videoHappiness"] = videoHappiness/float(len(data))
videoEmotions["videoContempt"] = videoContempt/float(len(data))
videoEmotions["videoAnger"] = videoAnger/float(len(data))

averages = {"averages": frames, "videoAverages": videoEmotions}

with open('averages.json', 'w+') as file:
    json.dump(averages, file, indent=4)
    
#with open('result.json', 'w+') as file:
#    json.dump(frames, file, indent=4)


