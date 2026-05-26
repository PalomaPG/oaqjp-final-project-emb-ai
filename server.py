from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

# app initialization
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detect_emotion():
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    fmt_response = (
        f"For the given statement, the system response is 'anger': {response["anger"]}, " 
        f"'disgust': {response["disgust"]}, 'fear': {response["fear"]}, 'joy': {response["joy"]} "
        f"and 'sadness': {response["sadness"]}. The dominant emotion is <b>{response["dominant_emotion"]}</b>"
        )
    return fmt_response


@app.route("/")
def render_index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)