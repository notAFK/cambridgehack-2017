with open(dirconf.DATA + "/vs.log", 'a') as file:
		file.write("Entering Pydub \n")
		
from pydub import AudioSegment
from pydub.utils import make_chunks
import dirconf



myaudio = AudioSegment.from_file(dirconf.UPLOAD+"/movie.wav" , "wav")
chunk_length_ms = 2000 # pydub calculates in millisec
chunks = make_chunks(myaudio, chunk_length_ms) #Make chunks of one sec

#Export all of the individual chunks as wav files

with open(dirconf.DATA + "/vs.log", 'a') as file:
		file.write("Starting Chunking \n")

for i, chunk in enumerate(chunks):
    chunk_name = dirconf.AUDIO + "/chunk1{:04d}.wav".format(i)
    print "exporting", chunk_name
    chunk.export(chunk_name, format="wav")

with open(dirconf.DATA + "/vs.log", 'a') as file:
		file.write("Successful! \n")
