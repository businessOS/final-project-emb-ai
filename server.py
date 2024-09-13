"""Emotion analyzer route server"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotions Analyzer")

@app.route("/emotionDetector")
def emotion_analyzer():
    """Retrieve the text to analyze from the request arguments."""
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    if response['anger'] is None:
        return "Invalid input! Try again."

    # Return a formatted string with the emotions score
    return response

@app.route("/")
def render_index_page():
    """Main route"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
