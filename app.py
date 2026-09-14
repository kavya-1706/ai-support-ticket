from flask import Flask, request, jsonify
import joblib
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)

model = joblib.load("models/ticket_classifier.pkl")
analyzer = SentimentIntensityAnalyzer()
def get_sentiment(text):
    score = analyzer.polarity_scores(text)["compound"]

    if score >= 0.05:
        return "positive"
    elif score <= -0.05:
        return "negative"
    else:
        return "neutral"

def get_priority(text, sentiment):
    urgent_words = [
        "urgent",
        "immediately",
        "stolen",
        "fraud",
        "blocked",
        "emergency"
    ]

    text = text.lower()

    if sentiment == "negative" and any(word in text for word in urgent_words):
        return "high"

    if sentiment == "negative":
        return "medium"

    return "low"


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    text = data["text"]

    category = model.predict([text])[0]
    sentiment = get_sentiment(text)
    priority = get_priority(text, sentiment)

    return jsonify({
        "category": category,
        "sentiment": sentiment,
        "priority": priority
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)