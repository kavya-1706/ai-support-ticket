# AI Support Ticket Classifier

An end-to-end NLP application that classifies banking customer support tickets into one of 77 categories, analyzes sentiment (positive, negative, or  neutral), and assigns a priority level (high, medium, or low). The trained Machine Learning model (Support Vector Classifier) is exposed through a Flask REST API, and containerized using Docker.

## Features

* This project classifies customer support tickets into 77 banking-related categories using a labelled dataset (Banking77).
* It uses TF-IDF for text feature extraction
* Linear SVM (SVC) is used for category classification, achieving 89% test accuracy.
* Sentiment analysis is done using VADER (Valence Aware Dictionary and sEntiment Reasoner), and rule-based logic is used to assign the priority.
* The trained model is deployed using a Flask REST API and containerized using Docker.

## Dataset

The project uses the Banking77 dataset, which contains customer queries belonging to 77 banking support categories.

The dataset is divided into:

* Training samples: 9,993
* Test samples: 3,076
* Categories: 77

## Machine Learning Approach

### 1. TF-IDF

TF-IDF (Term Frequency-Inverse Document Frequency) converts customer support text into numerical features that can be used by the machine learning model.

### 2. Linear Support Vector Machine (Support Vector Classifier)

A Linear Support Vector Machine is used to classify tickets into the 77 intent categories.

The model achieved around 89% accuracy on the test dataset.

### 3. Sentiment Analysis

VADER (Valence Aware Dictionary and sEntiment Reasoner) is used to classify the sentiment of each ticket as:

* Positive
* Neutral
* Negative

Sentiment is classified using VADER based on the compound score: 
scores >= 0.05 are classified as positive.
scores <= -0.05 are classified as negative.
scores between -0.05 and 0.05 are classified as neutral.

### 4. Priority Assignment

Priority is assigned using simple business rules:

* High: negative sentiment combined with urgent terms such as `fraud`, `stolen`, `blocked`, `emergency`, etc.
* Medium: negative sentiment without an urgent keyword
* Low: positive or neutral sentiment


## Installation

Clone the repository and install the required packages:

pip install -r requirements.txt

## Run Locally

Start the Flask API:

python app.py

The API will be available at:

http://127.0.0.1:5000


## API Usage

### Endpoint

POST /predict

### Request (example)

{
  "text": "I haven't received my card yet"
}


### Response (example)

{
  "category": "card_arrival",
  "priority": "low",
  "sentiment": "neutral"
}

### Using cURL

curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d "{\"text\":\"I haven't received my card yet\"}"

## Docker

Build the Docker image:

docker build -t ai-support-ticket .

Run the container:

docker run -p 5000:5000 ai-support-ticket


The API can then be accessed at:

http://127.0.0.1:5000

