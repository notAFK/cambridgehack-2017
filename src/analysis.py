import json
import dirconf
import collections

import sys

with open(dirconf.DATA + '/summary.json', 'r') as data_file:
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
analyticsKeys = ["attentionIndex", "averageSadness", "averageNeutral",
                 "averageContempt", "averageDisgust", "averageAnger",
                 "averageSurprise", "averageFear", "averageHappiness"]
videoDisgust = 0
videoFear = 0
videoSurprise = 0
videoSadness = 0
videoNeutral = 0
videoHappiness = 0
videoContempt = 0
videoAnger = 0

i = 0

for key in analyticsKeys:
  infoPerFrame[key] = 0
frames.append({"frame": data[0]["frame"], "info": infoPerFrame, "keyphrases":
              frame["keyphrases"], "speech": frame["speech"]})
if len(data[0]["faces"]) == 0:
    infoPerFrame = {}
    for key in analyticsKeys:
      infoPerFrame[key] = 0
    frames[0]["info"] = infoPerFrame
    i = i + 1

else:
  totalSadness = 0
  totalNeutral = 0
  totalContempt = 0
  totalDisgust = 0
  totalAnger = 0
  totalSurprise = 0
  totalFear = 0
  totalHappiness = 0
  noFaces = len(data[0]["faces"])
  for face in data[0]["faces"]:
      totalSadness += face["scores"]["sadness"]
      totalNeutral += face["scores"]["neutral"]
      totalContempt += face["scores"]["contempt"]
      totalDisgust += face["scores"]["disgust"]
      totalAnger += face["scores"]["anger"]
      totalSurprise += face["scores"]["surprise"]
      totalFear += face["scores"]["fear"]
      totalHappiness += face["scores"]["happiness"]

      infoPerFrame = {"attentionIndex": noFaces/float(maxfaces),
                      "averageSadness": totalSadness/float(noFaces),
                      "averageNeutral": totalNeutral/float(noFaces),
                      "averageContempt": totalContempt/float(noFaces),
                      "averageDisgust": totalDisgust/float(noFaces),
                      "averageAnger": totalAnger/float(noFaces),
                      "averageSurprise": totalSurprise/float(noFaces),
                      "averageFear": totalFear/float(noFaces),
                      "averageHappiness": totalHappiness/float(noFaces)}
      frames[0]["info"] = infoPerFrame

totalVideo = {}
for key in analyticsKeys:
  totalVideo[key] = 0

for index,frame in enumerate(data[1:]):
    totalSadness = 0
    totalNeutral = 0
    totalContempt = 0
    totalDisgust = 0
    totalAnger = 0
    totalSurprise = 0
    totalFear = 0
    totalHappiness = 0
    infoPerFrame = {}
    for key in analyticsKeys:
      infoPerFrame[key] = 0
    frames.append({"frame": frame["frame"], "info": infoPerFrame, "keyphrases":
                  frame["keyphrases"], "speech": frame["speech"]})
    if len(frame["faces"])!=0:
        noFaces = len(frame["faces"])
        for face in frame["faces"]:
            totalSadness += face["scores"]["sadness"]
            totalNeutral += face["scores"]["neutral"]
            totalContempt += face["scores"]["contempt"]
            totalDisgust += face["scores"]["disgust"]
            totalAnger += face["scores"]["anger"]
            totalSurprise += face["scores"]["surprise"]
            totalFear += face["scores"]["fear"]
            totalHappiness += face["scores"]["happiness"]
        infoPerFrame = {"attentionIndex": noFaces/float(maxfaces),
                        "averageSadness": totalSadness/float(noFaces),
                        "averageNeutral": totalNeutral/float(noFaces),
                        "averageContempt": totalContempt/float(noFaces),
                        "averageDisgust": totalDisgust/float(noFaces),
                        "averageAnger": totalAnger/float(noFaces),
                        "averageSurprise": totalSurprise/float(noFaces),
                        "averageFear": totalFear/float(noFaces),
                        "averageHappiness": totalHappiness/float(noFaces)}

        for key, emotion in infoPerFrame.iteritems():
          totalVideo[key] += infoPerFrame[key]
    else:
        infoPerFrame = {}
        for key in analyticsKeys:
          infoPerFrame[key] = frames[index+1]["info"][key]/2.0

    frames[index+1]["info"] = infoPerFrame

for key in analyticsKeys:
  totalVideo[key] = totalVideo[key] / float(len(data))

ss = totalVideo
h = ss.pop('attentionIndex')
lol = ((sorted(ss, key=ss.__getitem__)[-1])
       .split("average")[1]).capitalize()
totalVideo["mostCommonPercentage"] = sorted(ss.values())[-1]
totalVideo["mostCommon"] = lol
totalVideo["maxFaces"] = maxfaces
totalVideo["attentionIndex"] = h
averages = {"averages": frames, "videoAverages": totalVideo}

with open(dirconf.WEBSITE + '/' + sys.argv[1], 'w+') as file:
    json.dump(averages, file, indent=4)
