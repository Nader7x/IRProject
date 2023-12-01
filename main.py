
# Tokenization using NLTK
from nltk import word_tokenize, sent_tokenize

import Tokenizer

sent = "GeeksforGeeks is a great learning platform.\
It is one of the best for Computer Science students."
print(word_tokenize(sent))
print(sent_tokenize(sent))
Tokenizer.myfunction()