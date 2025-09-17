import nltk
# Download the necessary tokenization models punkt or punkt_lab 
nltk.download('punkt_tab') 
from nltk.tokenize import sent_tokenize
def tokenize_sentences(text):
    sentences = sent_tokenize(text)
    return sentences
# Example text
text = """NLTK is a leading platform for building Python programs to work with 
human language data. It provides easy-to-use interface to over 50 corpora and lexical 
resources such as WordNet, along with a suite of text processing libraries for 
classification,tokenization, stemming, tagging, parsing, and semantic reasoning, 
wrappers for industrial-strength NLP libraries, and an active discussion forum."""
# Tokenize sentences
sentences = tokenize_sentences(text)
# Print tokenized sentences
for i, sentence in enumerate(sentences):
    print(f"Sentence {i+1}: {sentence}")