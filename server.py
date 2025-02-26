from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

def format_response_decorator(function):
    def modify_output(*args, **kwargs):
        result = function(*args, **kwargs)
        if isinstance(result, tuple) and isinstance(result[0], dict):
            emotions = result[0]
            response_text = (
                f"For the given statement, the system response is 'anger': {emotions['anger']}, "
                f"'disgust': {emotions['disgust']}, 'fear': {emotions['fear']}, "
                f"'joy': {emotions['joy']} and 'sadness': {emotions['sadness']}. "
                f"The dominant emotion is {emotions['dominant_emotion']}."
            )
            return response_text, result[1]
        return result
    return modify_output

@app.route('/')
def home():
    return render_template('index.html')

@app.get("/emotionDetector")
@format_response_decorator
def detect_emotions():
    text_to_analyze = request.args.get("textToAnalyze")

    if text_to_analyze:
        result = emotion_detector(text_to_analyze)
        return ({
            "anger": result["anger"],
            "disgust": result["disgust"],
            "fear": result["fear"],
            "joy": result["joy"],
            "sadness": result["sadness"],
            "dominant_emotion": result["dominant_emotion"]
        }, 200)
    else:
        return ({"error": "Something went wrong"}, 400)

if __name__ == "__main__":
    app.run(host='localhost', port=5000)
