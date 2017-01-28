import json
import sys
import requests
import msconf
import dirconf


# Format the given URL as DATA for MS COGNITIVE REQUEST
def format_url(URL):
    return json.dumps({"url": URL})


# Format the given IMAGE FILE as OCTET DATA for MS REQUEST
def format_image(IMAGE):
    return open(IMAGE, 'rb').read()


# RETURN the RESPONSE from the MS COGNITIVE API
# Urls
def process_url(URL):
    # DEBUG
    print 'PROCESSING URL: ' + URL
    print 'DATA: ' + format_url(URL)

    # SEND REQUEST and GET RESPONSE
    with requests.session() as post_request:
        get_request = post_request.post(msconf.SERVICE,
                                        headers=msconf.HEADER_URL,
                                        data=format_url(URL))

    # RETURN LOADED JSON DATA
    return json.loads(get_request.content)


# RETURN the RESPONSE from the MS COGNITIVE API
# Binary data
def process_image(IMAGE):
    print 'PROCESSING IMAGE: ' + IMAGE

    # SEND REQUEST and GET RESPONSE
    with requests.session() as post_request:
        get_request = post_request.post(msconf.SERVICE,
                                        headers=msconf.HEADER_IMG,
                                        data=format_image(IMAGE))

    return json.loads(get_request.content)

if __name__ == '__main__':
    faces = process_image(dirconf.IMAGES + '/press.jpg')
    for face in faces:
        print face

    # faces = process_url(msconf.TEST_URL)
    # for face in faces:
    #     print face
