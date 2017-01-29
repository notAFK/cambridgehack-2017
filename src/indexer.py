import json
import sys
import os
import dirconf
import msuplink
import msaudio
import mstext


if __name__ == '__main__':

    image_list = []
    responses = []

    for image in os.listdir(dirconf.IMAGES):
        if image.endswith('.jpg'):
            image_list.append(image)

    text_list = []
    keyphrase_list = []
    for text in msaudio.translate_all():
        text_list.append(mstext.process_text(text, 'f003a623c8f246b783e1f9c7076e4372'))
        keyphrase_list.append(mstext.process_keyphrases(text, 'f003a623c8f246b783e1f9c7076e4372'))

    print 'PROCESSING ' + str(len(image_list)) + ' IMAGES'

    for i, image in enumerate(image_list):
        response = msuplink.process_image(os.path.join(dirconf.IMAGES,
                                                       image))

        if len(response) == 1:
            print 'ERROR'
        else:
            responses.append({'frame': image[:5], 'faces': response, 'speech': text_list[i], 'keyphrases': keyphrase_list[i]})

    with open(os.path.join(dirconf.DATA, 'summary.json'), 'w+') as summary:
        json.dump(responses, summary, indent=4)
