import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag, RegexpParser

# Download necessary resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger_eng')

def chunk_sentence(sentence):
    words = word_tokenize(sentence)
    tagged_words = pos_tag(words, lang='eng')
    
    # Define grammar for chunking
    grammar = r"""
    NP: {<DT|JJ|NN.*>+}        # Noun Phrases
    PP: {<IN><NP>}             # Prepositional Phrases
    VP: {<VB.*><NP|PP|CLAUSE>+$} # Verb Phrases
    CLAUSE: {<NP><VP>}         # Clauses
    """
    
    parser = RegexpParser(grammar)
    chunked_sentence = parser.parse(tagged_words)
    return chunked_sentence

sentence = "The quick brown fox jumps over the lazy dog"
chunked_sentence = chunk_sentence(sentence)
print(chunked_sentence)
