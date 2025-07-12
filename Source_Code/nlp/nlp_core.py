# nlp/nlp_core.py

import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from textblob import TextBlob

# These downloads only need to run once (on first execution)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

class SimpleNLPProcessor:
    def __init__(self):
        self.text = ""

    def set_text(self, input_text):
        print("📝 Received text for processing.")
        self.text = input_text

    def tokenize(self):
        print("🔍 Tokenizing text...")
        tokens = word_tokenize(self.text)
        print(f"Tokens: {tokens}")
        return tokens

    def parse(self, tokens):
        print("🔧 Parsing tokens (POS tagging)...")
        parsed = pos_tag(tokens)
        print(f"Parsed: {parsed}")
        return parsed

    def recognize_intent(self):
        print("💡 Recognizing intent (basic sentiment analysis)...")
        blob = TextBlob(self.text)
        sentiment = blob.sentiment
        print(f"Sentiment polarity: {sentiment.polarity}, subjectivity: {sentiment.subjectivity}")
        return sentiment

    def generate_text(self):
        print("🗣️ Generating response (basic placeholder)...")
        return "📨 Response generated based on text analysis."