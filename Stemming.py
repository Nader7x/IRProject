import nltk
def Stemmer(string):
    return nltk.PorterStemmer().stem(string)