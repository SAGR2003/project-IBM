from flask import Flask
import requests

app = Flask(__name__)

URL = ("https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict")
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}


def emotion_detector(text_to_analyze):
    """
    Detects emotions in the given text using an external API.
    """
    response = requests.post(
        URL,
        headers = HEADERS,
        json = {"raw_document": {"text": text_to_analyze}}
    )

    if response.status_code == 200:
        data = response.json()
        emotions = data['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotions, key=emotions.get)

        return {
            'anger': emotions['anger'],
            'disgust': emotions['disgust'],
            'fear': emotions['fear'],
            'joy': emotions['joy'],
            'sadness': emotions['sadness'],
            'dominant_emotion': dominant_emotion            
        }
    else:
        return {"error": "Failed to get a response from the API"}