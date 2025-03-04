"""A Flask app that detects emotions in input text."""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

# A more descriptive app name.
app = Flask('EmotionDetector')


@app.route('/emotionDetector', methods=['GET', 'POST'])
def emotion_detection():
    """Detects the dominant emotion from the input text."""
    input_text = request.args.get('textToAnalyze')  # Renamed `input` to `input_text`

    if input_text is None:  # Check if input is not provided
        return "Invalid text! Please try again.", 400  # Return a 400 error for invalid input

    response = emotion_detector(input_text)

    dominant_emotion = response.pop('dominant_emotion', None)

    if dominant_emotion is not None:
        output = (f"For the given statement, the system response is {response}. "
                  f"The dominant emotion is {dominant_emotion}")
        output = output.replace('{', '').replace('}', '')  # Clean output for display
        print(output)
        return output, 200  # Return with a successful response code (200)

    return "Invalid text! Please try again!", 400
@app.route('/')
def home():
    """Renders the home page."""
    return render_template('index.html'), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # Ensures app runs on all available network interfaces
