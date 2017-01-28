import json
import sys
import os
import dirconf

import msuplink

if __name__ == '__main__':

    image_list = []
    responses = []

    for image in os.listdir(dirconf.IMAGES):
        if image.endswith('.jpg'):
            image_list.append(image)

    print 'PROCESSING ' + str(len(image_list)) + ' IMAGES'

    for image in image_list:
        response = msuplink.process_image(os.path.join(dirconf.IMAGES,
                                                       image))

        if len(response) == 1:
            print 'ERROR'
        else:
            responses.append({'frame': image[:6], 'faces': response})

    response.append({'count': len(responses)})

    with open(os.path.join(dirconf.DATA, 'summary.json'), 'w+') as summary:
        json.dump(responses, summary, indent=4)
