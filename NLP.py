import nltk
nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Sample text for analysis
text = "I really enjoyed this movie. The acting was great and the plot was engaging."

# Calculate the sentiment score for the text
score = sia.polarity_scores(text)

# Print the sentiment score
print("negative = ", score["neg"])
print("neutral = ", score["neu"])
print("positive = ", score["pos"])
print("compound = ", score["compound"])

