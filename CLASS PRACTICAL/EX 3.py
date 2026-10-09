# Program to perform morphological analysis using NLTK

import nltk
from nltk.stem import WordNetLemmatizer

# Download required NLTK data if missing
for resource in ('wordnet', 'omw-1.4'):
    try:
        nltk.data.find(f'corpora/{resource}')
    except LookupError:
        nltk.download(resource, quiet=True)

# Create lemmatizer
lemmatizer = WordNetLemmatizer()

# List of words with their appropriate part-of-speech for accurate lemmatization
words = ["running", "flies", "studies", "better", "children"]
part_of_speech = {
    "running": "v",
    "flies": "v",
    "studies": "v",
    "better": "a",
    "children": "n",
}

print("Morphological Analysis:")
print("-" * 40)

for word in words:
    lemma = lemmatizer.lemmatize(word, pos=part_of_speech.get(word, "n"))
    print("Word:", word, "-> Lemma:", lemma)