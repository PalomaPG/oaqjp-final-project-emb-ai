import requests
import json

def emotion_detector(text_to_analyze):
  url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
  header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
  input = { "raw_document": { "text": text_to_analyze } }
  response = requests.post(url, json = input, headers=header)
  formatted_response = json.loads(response.text)
  output = formatted_response["emotionPredictions"][0]["emotion"]
  output['dominant_emotion'] = dominant_emotion(output)
  return output
  
def dominant_emotion(emotions):
  max_score = 0
  dom_emotion = ""
  for k,v in emotions.items():
    if v > max_score:
      max_score = v
      dom_emotion = k
  return dom_emotion
