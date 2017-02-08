![cc17](http://imgur.com/fL1OpNK.jpg)
# Cognitive Crowds - \#hackcambridge2017
---

###### Acquire TED-grade presentation skills from the audience sentiment analysis feedback, powered by Microsoft Cognitive Services

Description
===

### Inspiration
As we've been to some hackathons by now, we got pretty used to presenting in front of a large audience. However, we're still very far from professional presenters, such as TED talks spekers. Of course, the best feedback you can have on your presentation is the public's reaction. But how can you measure your impact on the public, especially if you are busy managing the stress of giving the talk?

### What it does
Using a camera, you can record the audicence while you are giving a presentation, and then upload that video on Cognitive Services web dashboard. It extracts frames every 2 seconds and continuously analyses the public's emotions, plotting them against the presentation audio/video. It calculates the attention of the public for each frame, plotting it so that you are able to see when exactly in your talk there was an attention drop. You can also check if people reacted to what you said in the way you wanted. For example, if you said a joke 20 seconds in, but there was no indication of an increase in happiness around that timestamp, it could mean there is room for improvement.

### How we built it
We created a web dashboard in HTML, javascript and CSS, powered by PHP as backed. It processes the upload and then executes three python scripts that split the video in key frames and key audio's, perform the API calls to Microsoft Cognitive services and get the emotion analysis for all the frames and the sentiment analysis for the text, and format everything in a JSON file, while also calculating the attention and other analytics. Then, back in the web dashboard, the JSON file is read into multiple javascript functions that plot the results.

### Challenges we ran into
Biggest challenge was getting opencv to run. There were numerous dependencies to compile from source, not available as binaries, and it did not work from the first time. Also, we ran into problems making it work on Windows, which made testing harder, because on Macs we had problems getting the apache server to work properly. Another big problem was the initial limitation of API calls, which only allowed a maximum of 20 seconds of video. In the morning we received an Azure API key from Microsoft, which allowed us to implement a working solution. Moreover, customising the audio/video player was a problem, and integrating it with the graphs, in order to properly show the data at apropriate times.

Documentation
===

References
===

### License
MIT License

### Video demo
<iframe width="560" height="315" src="https://www.youtube.com/embed/tZiVKev7SwI" frameborder="0" allowfullscreen></iframe>

### MS CS API
