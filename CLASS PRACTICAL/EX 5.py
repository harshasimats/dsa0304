# Program to perform word stemming using Porter Stemmer

from nltk.stem import PorterStemmer
import nltk

# Create Porter Stemmer object
stemmer = PorterStemmer()

# List of words
words = [
    "playing",
    "played",
    "plays",
    "studies",
    "studying",
    "connected",
    "connection",
    "easily",
    "running",
    "runner"
]

print("Porter Stemmer")
print("-" * 35)

for word in words:
    stem = stemmer.stem(word)
    print(word, "->", stem)