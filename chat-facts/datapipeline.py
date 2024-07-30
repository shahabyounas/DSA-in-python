import nltk
from nltk.text import Text
from nltk import word_tokenize
from nltk.corpus import stopwords

from io import StringIO
import multiprocessing as mp

"""
Pipeline steps
1 - Tokenization
2 - Cleaning
3 - Normalization
4 - Lemmatization
5 - Steaming
"""
class DataPipeLine:
    
    def __init__(self):
        self.cpu_count = mp.cpu_count
    
    
    def byte_to_string(self, raw):
        if raw:
            return StringIO(raw.getvalue().decode('utf-8'))
        raise 'no data found'

    
    def tokenize_text(self, text):
        return word_tokenize(text)
    
    def clean_text(self, tokens):
        str = ''
        sents = nltk.sent_tokenize(tokens)
        for r in sents:
            l = r.lower()
            ll = l.split(':')
            last = ll[-1].lower()
            str += last
    
        stop_words = stopwords.words('english')
        tokens = word_tokenize(str)
        stop_words_removed = [w for w in tokens if w not in stop_words and w.isalpha()]
        return stop_words_removed