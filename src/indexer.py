import json
import sys
import os
import dirconf
import msaudio
import msuplink

if __name__ == '__main__':

    image_list = []
    text_list = []
    responses = []

    for image in os.listdir(dirconf.IMAGES):
        if image.endswith('.jpg'):
            image_list.append(image)

    for text in msaudio.translate_all():
        text_list.append(text)

    print 'PROCESSING ' + str(len(image_list)) + ' IMAGES'

    for i, image in enumerate(image_list):
        response = msuplink.process_image(os.path.join(dirconf.IMAGES,
                                                       image))

        if len(response) == 1:
            print 'ERROR'
        else:
            responses.append({'frame': image[:5], 'faces': response, 'speech': text_list[i]})

    with open(os.path.join(dirconf.DATA, 'summary.json'), 'w+') as summary:
        json.dump(responses, summary, indent=4)
