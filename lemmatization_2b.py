import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Download necessary resources
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

def lemmatize_text(text):
    # Initialize the lemmatizer
    lemmatizer = WordNetLemmatizer()
    
    # Tokenize the text
    tokens = word_tokenize(text)
    
    # Lemmatize each token
    lemmatized_text = ' '.join([lemmatizer.lemmatize(word) for word in tokens])
    
    return lemmatized_text

# Example text
text = "The cats are chasing mice and playing in the garden"

# Perform lemmatization
lemmatized_text = lemmatize_text(text)

# Print results
print("Original Text:", text)
print("Lemmatized Text:", lemmatized_text)
