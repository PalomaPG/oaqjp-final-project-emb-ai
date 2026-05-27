''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

# app initialization
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detect_emotion():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows a descriptive text
        explaining the result and the dominant emotion.
    '''
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    if isinstance(response, str):
        return response

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    fmt_response = (
        f"For the given statement, the system response is 'anger': {response['anger']}, " 
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} "
        f"and 'sadness': {response['sadness']}. The dominant emotion is " 
        f"<b>{response['dominant_emotion']}.</b>"
    )
    return fmt_response

@app.route("/")
def render_index_page():
    ''' 
        This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
