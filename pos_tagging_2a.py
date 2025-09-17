import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger_eng')

def pos_tagging(text):
    """Tokenizes the input text and applies POS tagging"""
    # Tokenize the text
    words = word_tokenize(text)
    
    # Apply POS tagging
    tagged_words = pos_tag(words)
    
    return tagged_words

# Example text
text = "NLTK is a powerful tool for processing human language data."

# Perform POS tagging
tagged_text = pos_tagging(text)

# Print the POS-tagged text
print(tagged_text)
