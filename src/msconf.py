API_KEY = 'd070ced621a441978e1dd1c43a606c3b'
SERVICE = 'https://westus.api.cognitive.microsoft.com/emotion/v1.0/recognize'


HEADER_URL = {'Ocp-Apim-Subscription-Key': API_KEY,
              'Content-Type': 'application/json',
              'Accept': 'application/json'}

HEADER_IMG = {'Ocp-Apim-Subscription-Key': API_KEY,
              'Content-Type': 'application/octet-stream',
              'Accept': 'application/json'}

TEST_URL = 'https://thumbs.dreamstime.com/z/young-people-13305611.jpg'
TEST_IMG = '/Users/copper/Developer/Gits/cambridgehack2017/data/images/test.jpg'
