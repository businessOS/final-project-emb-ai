import requests
import json

def emotion_detector(text_to_analyse):
    #URL of the emotion analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Contructinng the request payload in de expected format
    myobj =  { "raw_document": { "text": text_to_analyse } }
    # Custom header
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # sending a POST request to emotion analysis API
    response = requests.post(url, json=myobj, headers=header)
    formated_response = json.loads(response.text)
    status_code = response.status_code
    # Response error
    if status_code == 400: 
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion = None
    else:
        emotions = formated_response["emotionPredictions"][0]["emotion"]
        print(emotions)
        anger_score = emotions["anger"]
        disgust_score = emotions["disgust"]
        fear_score = emotions["fear"]
        joy_score = emotions["joy"]
        sadness_score = emotions["sadness"]
        dominant_emotion = max(emotions, key=emotions.get)

    # returning a dictionary containing emotion analysis result
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
