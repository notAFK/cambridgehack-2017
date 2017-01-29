import json
import requests


# Create standard header for Microsoft Text An. API
def write_header(key):
    HEADER = {'Ocp-Apim-Subscription-Key': key,
              'Content-Type': 'application/json',
              'Accept': 'application/json'}
    return HEADER


# Prepare the document files for upload.
def write_doc_string(mytext):
    # Standard data format for MS Text An. API request.
    DATA = {
     "documents": [
         {
             "language": "en",
             "id": "1",
             "text": mytext
             }]}
    return json.dumps(DATA)


def process_text(mytext, apikey):
    if not mytext:
        return "null"
    with requests.session() as shortname:
        answer = shortname.post('https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment', headers=write_header(apikey), data=write_doc_string(mytext))
    returndict = json.loads(answer.content)
    print returndict
    try:
        return returndict['documents'][0]['score']
    except:
        return "null"


def process_keyphrases(mytext, apikey):
    if not mytext:
        return "null"
    with requests.session() as shortname:
        answer = shortname.post('https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/keyPhrases', headers=write_header(apikey), data=write_doc_string(mytext))
    returndict = json.loads(answer.content)
    print returndict
    try:
        return returndict['documents'][0]['keyPhrases']
    except:
        return "null"
