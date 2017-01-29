import json
import sys
import os
import dirconf
import msuplink
import msaudio
import mstext
import time


if __name__ == '__main__':

    image_list = []
    responses = []

    for image in os.listdir(dirconf.IMAGES):
        if image.endswith('.jpg'):
            image_list.append(image)

    print "IMAGE LIST: ", image_list

    text_list = []
    keyphrase_list = []
    for text in msaudio.translate_all():
        text_list.append(mstext.process_text(text, '7109a293e5ef43538b6c6e14ee4e7b6d'))
        keyphrase_list.append(mstext.process_keyphrases(text, '7109a293e5ef43538b6c6e14ee4e7b6d'))

    print 'PROCESSING ' + str(len(image_list)) + ' IMAGES'

    for i, image in enumerate(image_list):
        response = msuplink.process_image(os.path.join(dirconf.IMAGES,
                                                       image))

        if i >= len(text_list):
            i = len(text_list)-1

        if len(response) == 1:
            responses.append({'frame': image.split('.')[0][1:], 'faces': [], 'speech': text_list[i], 'keyphrases': keyphrase_list[i]})
        else:
            responses.append({'frame': image.split('.')[0][1:], 'faces': response, 'speech': text_list[i], 'keyphrases': keyphrase_list[i]})

#        time.sleep(4)

    print 'RESPONSES: ' + str(len(responses))

    with open(os.path.join(dirconf.DATA, 'summary.json'), 'w+') as summary:
        json.dump(responses, summary, indent=4)
