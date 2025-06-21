# python tokenization.py
from nltk.tokenize import PunktSentenceTokenizer, TreebankWordTokenizer

# Sample text
text = "Hello there! Let's fix the tokenization issue."

# Sentence tokenizer
sent_tokenizer = PunktSentenceTokenizer()
sentences = sent_tokenizer.tokenize(text)
print("Sentences:", sentences)

# Word tokenizer
word_tokenizer = TreebankWordTokenizer()
for sentence in sentences:
    words = word_tokenizer.tokenize(sentence)
    print("Words:", words)



