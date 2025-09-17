import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag, ne_chunk

# Download necessary resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('maxent_ne_chunker')
nltk.download('words')

def ner(text):
    words = word_tokenize(text)
    tagged_words = pos_tag(words, lang='eng')
    named_entities = ne_chunk(tagged_words)
    return named_entities

text = "Apple is a company based in California, United States. Steve Jobs was one of its founders."

named_entities = ner(text)
print(named_entities)
