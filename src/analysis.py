import json
import collections
with open('data.json', 'r') as data_file:    
    data = json.load(data_file)

maxfaces = 0

for frame in data:
    if maxfaces < len(frame["faces"]):
        maxfaces = len(frame["faces"])
attention = []
for frame in data:
    attentionPerFrame ={"frame": frame["frame"], "attentionIndex": len(frame["faces"])/float(maxfaces)}
    attention.append(attentionPerFrame)

with open('result.json', 'w+') as file:
    json.dump(attention, file, indent=4)


##orderedAttention = collections.OrderedDict(sorted(unorderedAttention.items()))
##
##attention = []
##for k, v in orderedAttention.iteritems():
##    attention.append({k: v})
##    
##with open('result.json', 'w+') as file:
##    json.dump(attention, file, indent=4)
##
##
##
#print collections.OrderedDict(attention)    
#with open('result.json', 'w+') as file:
 #   json.dump(attention, file, indent=4)
        
##        
##for frame in data:
##    for face in frame["faces"]:
##        for score in face["scores"]:
##            
##            emotions = {"totalsadness": 0, "totalneutral": 0, "totalcontempt": 0,
##                        "totaldisgust": 0, "totalanger": 0, "totalsurprise": 0,
##                        "totalfear": 0, "totalhappiness": 0}
##
##            emotions["totalsadness"] += face["scores"]["sadness"]
##            emotions["totalneutral"] += face["scores"]["neutral"]
##            emotions["totalcontempt"] += face["scores"]["contempt"]
##            emotions["totaldisgust"] += face["scores"]["disgust"]
##            emotions["totalanger"] += face["scores"]["anger"]
##            emotions["totalsurprise"] += face["scores"]["surprise"]
##            emotions["totalfear"] += face["scores"]["fear"]
##            emotions["totalhappiness"] += face["scores"]["happiness"]
##
##            for emotion, value in emotions.iteritems():
##                print(emotion, value/len(data))
##    
