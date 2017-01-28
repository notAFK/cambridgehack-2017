# -*- coding: utf-8 -*-
import sys
import os
import subprocess
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
start = 0
if (len(sys.argv) > 2):
	end = (int(sys.arg[-1])) * 1000
else:
	end = 5000 #define frame to capture

increment = end
vidcap = cv2.VideoCapture(sys.argv[1])
success,image = vidcap.read()
dir_path = ("/data")


while success:
	frame_count = str(end/1000)
	success,image = vidcap.read()
	print "##############################"
	print "Start duration: " + str(start)
	print "End duration: " + str(end)
	print "##############################"
	vidcap.set(0, end)
	output = cv2.imwrite("data/" + "000" + frame_count + ".jpg", image)
	end = end + increment
	command = " ffmpeg -i " + sys.argv[1] + " -f segment -strftime 1 -segment_time 5 -segment_format wav " + "data/frame_" + frame_count + ".wav"

	subprocess.call(command, shell=True)
 	#if (end >= 40000):
 		#break






'''import http.client, urllib.parse, json
API_KEY = '28f7463c76344a06ace7b80405d27e6c'
PARAMS = ""

headers = {"Ocp-Apim-Subscription-Key": apiKey}

AccessTokenHost = "https://api.cognitive.microsoft.com/"
path = "/sts/v1.0/issueToken"

print "Connecting to server to get access token"

conn = http.client.HTTPSConnection(AccessTokenHost)
conn.request("POST", path, PARAMS, headers)
response = conn.getresponse()

print (response.status, response.reason)

data = response.read()
conn.close()

accesstoken = data.decode("UTF-8")
print "Access token: " + accesstoken

conn = http.clinet.HTTPSConnection("https://speech.platform.bing.com/recognize?scenarios=catsearch&appid=f84e364c-ec34-4773-a783-73707bd9a585&locale=en-US&device.os=wp7&version=3.0&format=json&requestid=" + accesstoken + "")
headers = {"Content-Type: audio/wav",

}'''
