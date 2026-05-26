'''
Module that storages functions intended to detect emotions from 
input text given by a client
'''
import json
import requests

def emotion_detector(text_to_analyze):
    '''
    Main function intended to detect the dominant emotion from text analysis.
    It returns a dictionary with emotions and their respective scores, and 
    the dominant emotion with the maximum score.
    '''
    url = (
        "https://sn-watson-emotion.labs.skills.network/v1/"
        "watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    my_input = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = my_input, headers=header, timeout=5)
    formatted_response = json.loads(response.text)
    output = formatted_response["emotionPredictions"][0]["emotion"]
    output['dominant_emotion'] = dominant_emotion(output)
    return output

def dominant_emotion(emotions):
    '''
    Auxiliary function that returns the dominant emotion according to
    the maximum values between scores.
    '''
    max_score = 0
    dom_emotion = ""
    for k,v in emotions.items():
        if v > max_score:
            max_score = v
            dom_emotion = k
    return dom_emotion
