import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import TreebankWordTokenizer

nltk.download('wordnet')
nltk.download('omw-1.4')   # for better lemmatization accuracy

lemmatizer = WordNetLemmatizer()
tokenizer = TreebankWordTokenizer()

text = "He was running and studying various studies related to happiness and sadness."

words = tokenizer.tokenize(text)

lemmatized_words = [lemmatizer.lemmatize(word, pos='v') for word in words]

print("Original Words:", words)
print("Lemmatized Words:", lemmatized_words)

