"""
This module is a Flask web application for emotion detection wit Watson NLP.

credits to copilot for the docstrings
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    """
    Renders the home page with the input form for emotion detection.
    """
    return render_template('index.html')

@app.get("/emotionDetector")
def detect_emotions():
    """
    Detects emotions in the given text using the emotion_detector function.
    Returns a formatted response with the detected emotions 
    or an error message if the input is invalid.

    Returns:
        str: Formatted response text or error message.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    result = emotion_detector(text_to_analyze)
    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again.", 400

    response_text = (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, "
        f"'joy': {result['joy']} and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    return response_text, 200

if __name__ == "__main__":
    app.run(host='localhost', port=5000)
