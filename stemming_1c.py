import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Download NLTK tokenizer models
nltk.download('punkt')

def stem_text(text):
    # Initialize the Porter Stemmer
    porter_stemmer = PorterStemmer()
    
    # Tokenize the text into words
    words = word_tokenize(text)
    
    # Apply stemming to each word
    stemmed_words = [porter_stemmer.stem(word) for word in words]
    
    # Join the stemmed words back into a single string
    stemmed_text = ' '.join(stemmed_words)
    
    return stemmed_text

# Example text
text = "NLTK is a leading platform for building Python programs to work with human language data."

# Perform stemming
stemmed_text = stem_text(text)
# Print stemmed text
print(stemmed_text)