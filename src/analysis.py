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

if len(data[0]["faces"])==0:
    frames.append({"frame": data[0]["frame"]})
    infoPerFrame.update({"attentionIndex": 0, "averageSadness": 0, "averageNeutral": 0,
                         "averageContempt": 0, "averageDisgust": 0, "averageAnger": 0,
                         "averageSurprise": 0, "averageFear": 0, "averageHappiness": 0})
    frames[i].update(infoPerFrame)
    i = i + 1

    for frame in data[1:]:
        
        totalSadness = 0
        totalNeutral = 0
        totalContempt = 0
        totalDisgust = 0
        totalAnger = 0
        totalSurprise = 0
        totalFear = 0
        totalHappiness = 0

        frames.append({"frame": frame["frame"]})
        if len(frame["faces"])!=0:
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
        else:
            prevIndex = data.index(frame)-1
            infoPerFrame.update({"attentionIndex": len(data[prevIndex]["faces"])/float(maxfaces)/2.0})
            
            for face in data[prevIndex]["faces"]:
                totalSadness += face["scores"]["sadness"]/2.0
                totalNeutral += face["scores"]["neutral"]/2.0
                totalContempt += face["scores"]["contempt"]/2.0
                totalDisgust += face["scores"]["disgust"]/2.0
                totalAnger += face["scores"]["anger"]/2.0
                totalSurprise += face["scores"]["surprise"]/2.0
                totalFear += face["scores"]["fear"]/2.0
                totalHappiness += face["scores"]["happiness"]/2.0

        emotions={}
        if len(frame["faces"])==0 & len(data[prevIndex]["faces"])==0:
            emotions["averageSadness"] = 0
            emotions["averageNeutral"] = 0
            emotions["averageContempt"] = 0
            emotions["averageDisgust"] = 0
            emotions["averageAnger"] = 0
            emotions["averageSurprise"] = 0
            emotions["averageFear"] = 0
            emotions["averageHappiness"] = 0
        elif len(frame["faces"])!=0:
            length = len(frame["faces"])
            emotions["averageSadness"] = format(totalSadness/float(length),'.15f')
            videoSadness += float(emotions["averageSadness"])
            emotions["averageNeutral"] = format(totalNeutral/float(length),'.15f')
            videoNeutral += float(emotions["averageNeutral"])
            emotions["averageContempt"] = format(totalContempt/float(length),'.15f')
            videoContempt += float(emotions["averageContempt"])
            emotions["averageDisgust"] = format(totalDisgust/float(length),'.15f')
            videoDisgust += float(emotions["averageDisgust"])
            emotions["averageAnger"] = format(totalAnger/float(length),'.15f')
            videoAnger += float(emotions["averageAnger"])
            emotions["averageSurprise"] = format(totalSurprise/float(length),'.15f')
            videoSurprise += float(emotions["averageSurprise"])
            emotions["averageFear"] = format(totalFear/float(length),'.15f')
            videoFear += float(emotions["averageFear"])
            emotions["averageHappiness"] = format(totalHappiness/float(length),'.15f')
            videoHappiness += float(emotions["averageHappiness"])
        else:
            length = len(data[prevIndex]["faces"])
                
            emotions["averageSadness"] = format(totalSadness/float(length)/2.0,'.15f')
            videoSadness += float(emotions["averageSadness"])
            emotions["averageNeutral"] = format(totalNeutral/float(length)/2.0,'.15f')
            videoNeutral += float(emotions["averageNeutral"])
            emotions["averageContempt"] = format(totalContempt/float(length)/2.0,'.15f')
            videoContempt += float(emotions["averageContempt"])
            emotions["averageDisgust"] = format(totalDisgust/float(length)/2.0,'.15f')
            videoDisgust += float(emotions["averageDisgust"])
            emotions["averageAnger"] = format(totalAnger/float(length)/2.0,'.15f')
            videoAnger += float(emotions["averageAnger"])
            emotions["averageSurprise"] = format(totalSurprise/float(length)/2.0,'.15f')
            videoSurprise += float(emotions["averageSurprise"])
            emotions["averageFear"] = format(totalFear/float(length)/2.0,'.15f')
            videoFear += float(emotions["averageFear"])
            emotions["averageHappiness"] = format(totalHappiness/float(length)/2.0,'.15f')
            videoHappiness += float(emotions["averageHappiness"])
            
        infoPerFrame.update(emotions)       
        frames[i].update(infoPerFrame)
        i = i + 1

else:
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
        if len(frame["faces"])!=0:
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
        else:
            prevIndex = data.index(frame)-1
            infoPerFrame.update({"attentionIndex": len(data[prevIndex]["faces"])/float(maxfaces)/2})
            
            for face in data[prevIndex]["faces"]:
                totalSadness += face["scores"]["sadness"]/2.0
                totalNeutral += face["scores"]["neutral"]/2.0
                totalContempt += face["scores"]["contempt"]/2.0
                totalDisgust += face["scores"]["disgust"]/2.0
                totalAnger += face["scores"]["anger"]/2.0
                totalSurprise += face["scores"]["surprise"]/2.0
                totalFear += face["scores"]["fear"]/2.0
                totalHappiness += face["scores"]["happiness"]/2.0

        emotions={}
        if len(frame["faces"])==0 & len(data[prevIndex]["faces"])==0:
            emotions["averageSadness"] = 0
            emotions["averageNeutral"] = 0
            emotions["averageContempt"] = 0
            emotions["averageDisgust"] = 0
            emotions["averageAnger"] = 0
            emotions["averageSurprise"] = 0
            emotions["averageFear"] = 0
            emotions["averageHappiness"] = 0
        elif len(frame["faces"])!=0:
            length = len(frame["faces"])
            emotions["averageSadness"] = format(totalSadness/float(length),'.15f')
            videoSadness += float(emotions["averageSadness"])
            emotions["averageNeutral"] = format(totalNeutral/float(length),'.15f')
            videoNeutral += float(emotions["averageNeutral"])
            emotions["averageContempt"] = format(totalContempt/float(length),'.15f')
            videoContempt += float(emotions["averageContempt"])
            emotions["averageDisgust"] = format(totalDisgust/float(length),'.15f')
            videoDisgust += float(emotions["averageDisgust"])
            emotions["averageAnger"] = format(totalAnger/float(length),'.15f')
            videoAnger += float(emotions["averageAnger"])
            emotions["averageSurprise"] = format(totalSurprise/float(length),'.15f')
            videoSurprise += float(emotions["averageSurprise"])
            emotions["averageFear"] = format(totalFear/float(length),'.15f')
            videoFear += float(emotions["averageFear"])
            emotions["averageHappiness"] = format(totalHappiness/float(length),'.15f')
            videoHappiness += float(emotions["averageHappiness"])
        else:
            length = len(data[prevIndex]["faces"])
                
            emotions["averageSadness"] = format(totalSadness/float(length)/2.0,'.15f')
            videoSadness += float(emotions["averageSadness"])
            emotions["averageNeutral"] = format(totalNeutral/float(length)/2.0,'.15f')
            videoNeutral += float(emotions["averageNeutral"])
            emotions["averageContempt"] = format(totalContempt/float(length)/2.0,'.15f')
            videoContempt += float(emotions["averageContempt"])
            emotions["averageDisgust"] = format(totalDisgust/float(length)/2.0,'.15f')
            videoDisgust += float(emotions["averageDisgust"])
            emotions["averageAnger"] = format(totalAnger/float(length)/2.0,'.15f')
            videoAnger += float(emotions["averageAnger"])
            emotions["averageSurprise"] = format(totalSurprise/float(length)/2.0,'.15f')
            videoSurprise += float(emotions["averageSurprise"])
            emotions["averageFear"] = format(totalFear/float(length)/2.0,'.15f')
            videoFear += float(emotions["averageFear"])
            emotions["averageHappiness"] = format(totalHappiness/float(length)/2.0,'.15f')
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

