# python stemming.py
from nltk.stem import PorterStemmer
from nltk.tokenize import TreebankWordTokenizer
ps = PorterStemmer()
tokenizer = TreebankWordTokenizer()

text = "He was running and studying various studies related to happiness and sadness."

# Tokenize without using `word_tokenize()`
words = tokenizer.tokenize(text)

# Apply stemming
stemmed_words = [ps.stem(word) for word in words]

print("Original Words:", words)
print("Stemmed Words:", stemmed_words)

from nltk.stem import LancasterStemmer
ls = LancasterStemmer()

print(ls.stem("happiness"))  # Output: happi
print(ls.stem("running"))    # Output: run

from nltk.stem import SnowballStemmer
snow = SnowballStemmer(language='english')

print(snow.stem("studies"))  # Output: studi

