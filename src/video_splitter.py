# -*- coding: utf-8 -*-
import sys
import os
import dirconf
import subprocess
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2


vidcap = cv2.VideoCapture(sys.argv[1])

start = 0
if (len(sys.argv) > 2):
	end = (int(sys.arg[-1])) * 1000
else:
	end = 0 #define frame to capture

	frame_count = end/1000
	print vidcap.grab()

	success,image = vidcap.read()
	print "##############################"
	print "Start duration: " + str(start)
	print "End duration: " + str(end)
	print "##############################"
	vidcap.set(0, end)
	output = cv2.imwrite(dirconf.IMAGES + "/1{:04d}".format(frame_count)  + ".jpg", image)
	start = end
	end = end + 2000

increment = end
vidcap = cv2.VideoCapture(sys.argv[1])
success,image = vidcap.read()

with open(dirconf.DATA + "/vs.log", 'w+') as file:
	file.write("Reading camera input")

while success:
	frame_count = end/1000
	success,image = vidcap.read()
	print "##############################"
	print "Start duration: " + str(start)
	print "End duration: " + str(end)
	print "##############################"
	vidcap.set(cv2.cv.CV_CAP_PROP_POS_MSEC, end)
	with open(dirconf.DATA + "/vs.log", 'a') as file:
		file.write("Reporting from within frame chunker")
	output = cv2.imwrite(dirconf.IMAGES + "/1{:04d}".format(frame_count) + ".jpg", image)
	start = end
	end = end + increment
 	#if (end >= 40000):
 		#break
with open(dirconf.DATA + "/vs.log", 'a') as file:
		file.write("Out of chunker")

with open(dirconf.DATA + "/vs.log", 'a') as file:
		file.write("Got to ffmpeg\n")


command = "/usr/local/bin/ffmpeg -i " + sys.argv[1] + " " + dirconf.UPLOAD + "/movie.wav"
subprocess.call(command, shell=True)

with open(dirconf.DATA + "/vs.log", 'a') as file:
		file.write("Generated WAV \n")

with open(dirconf.DATA + "/vs.log", 'a') as file:
		file.write("SECOND AFTER GEN WAV \n")

total_time = len(os.listdir(dirconf.IMAGES))
# total_time = int((total_time*2)/5)

for i in range(total_time):

 	split_command = "/usr/local/bin/ffmpeg -i  " + dirconf.UPLOAD + "/movie.wav -vcodec copy -acodec copy -ss 00:"+ "{:02d}".format(int(i/30)) + ":"+ "{:02d}".format(int((i*2)%60)) +" -t 00:00:02 "  + dirconf.AUDIO + "/output1{:04d}.wav".format(i)

 	with open(dirconf.DATA + "/vs.log", 'a') as file:
 	 	 	file.write(split_command + "\n")

 	subprocess.call(split_command, shell=True)

with open(dirconf.DATA + "/vs.log", 'a') as file:
		file.write("Success! \n")