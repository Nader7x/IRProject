import Tokenizing
import Stemming
import PositionalIndex
from prettytable import PrettyTable

import views

documents = []
tokenizedDocuments = []
stemmedDocuments = []

for i in range(1, 11):
    with open('./DocumentCollection/' + str(i) + ".txt", 'r') as file:
        content = file.read()
    documents.append(content)

print(documents)

for doc in documents:
    tokenizedDocuments.append(Tokenizing.tokenize(doc))


for innerList in tokenizedDocuments:
    tempList = []
    for token in innerList:
        tempList.append(Stemming.Stemmer(token))
    stemmedDocuments.append(tempList)

print(stemmedDocuments)


positional_index = PositionalIndex.createPositionalIndex(stemmedDocuments)


print(positional_index)


query = input("Enter positional query: ").lower()

query = Tokenizing.tokenize(query)

print(query)

stemmedQuery = []
for word in query:
    newStr = Stemming.Stemmer(word)
    stemmedQuery.append(newStr)

print(stemmedQuery)

right_docs = PositionalIndex.retrieve_matched_docs(stemmedQuery, positional_index)


# views.print_tf(positional_index)
# views.print_log_tf(positional_index)
# views.print_df_and_idf(positional_index)
views.print_tf_idf(positional_index)




