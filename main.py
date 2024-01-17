import Tokenizing
import Stemming
import PositionalIndex
import queryAnalysis
import boolean
import views
import os

documents = []
tokenizedDocuments = []
stemmedDocuments = []
folder_path = './DocumentCollection'
file_names = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
sorted_file_names = sorted(file_names, key=lambda x: int(os.path.splitext(x)[0]))
print(f"file names: {sorted_file_names}")
for filename in sorted_file_names:
    with open(folder_path + '/' + filename, 'r') as file:
        content = file.read()
    documents.append(content)

for doc in documents:
    tokenizedDocuments.append(Tokenizing.tokenize(doc))

for innerList in tokenizedDocuments:
    tempList = []
    for token in innerList:
        tempList.append(Stemming.Stemmer(token))
    stemmedDocuments.append(tempList)

positional_index = PositionalIndex.createPositionalIndex(stemmedDocuments)

views.print_tf(positional_index)
views.print_log_tf(positional_index)
views.print_df_and_idf(positional_index)
views.print_tf_idf(positional_index)
views.print_doc_length()
views.print_normalized_tf_idf(positional_index)

print("\n=============POSITIONAL INDEX====================================================")
PositionalIndex.view_positional_index(positional_index)

choice = input("Press any key to input query. Press q to terminate the program: ")


def detect_boolean(query):
    not_index = query.find("not")
    # remove and or not
    query = query.replace("and", "")
    query = query.replace("or", "")
    query = query[:not_index - 3]
    return query.strip()


while choice != "q" and choice != "Q":
    query = input("Enter Query: ").lower()
    booleanList = ["and", "or", "not"]
    stemmed_query = []
    if any(operator in query for operator in booleanList):
        right_docs = boolean.boolean(query, positional_index)
        new_query = detect_boolean(query)
        print(f"query after removal : {new_query}")
        new_query = Tokenizing.tokenize(new_query.lower())
        for word in new_query:
            newStr = Stemming.Stemmer(word)
            stemmed_query.append(newStr)

    # print(new_query)
    else:
        query = Tokenizing.tokenize(query.lower())
        for word in query:
            newStr = Stemming.Stemmer(word)
            stemmed_query.append(newStr)
        right_docs = PositionalIndex.retrieve_matched_docs(stemmed_query, positional_index)
    query_frequencies = queryAnalysis.calculate_term_frequency(stemmed_query)
    query_logged_frequencies = queryAnalysis.calculate_log_term_frequency(query_frequencies)
    idf_dict = queryAnalysis.calculate_idf(positional_index)
    query_tf_idf_dict = queryAnalysis.calculate_tf_idf(stemmed_query, query_logged_frequencies, idf_dict)
    query_length = queryAnalysis.calculate_query_length(query_tf_idf_dict)
    query_normalized_tf_idf = queryAnalysis.calculate_normalized_tf_idf(query_length, query_tf_idf_dict)

    docs_normalized_tf_idf = views.create_normalized_tf_idf(positional_index)  # ok

    product_and_sum_dictionary = queryAnalysis.calculate_product_and_sum(query_normalized_tf_idf,
                                                                         docs_normalized_tf_idf, right_docs,
                                                                         stemmed_query)

    sorted_matched_docs = queryAnalysis.sort_matched_docs(product_and_sum_dictionary, right_docs)

    views.print_query_statistics(stemmed_query, query_frequencies, query_logged_frequencies, idf_dict,
                                 query_tf_idf_dict, query_normalized_tf_idf)
    views.print_query_product(product_and_sum_dictionary, stemmed_query)
    views.print_similarities_query_length_matched_docs(query_length, product_and_sum_dictionary, sorted_matched_docs)
    print("\n=================================================================================================")
    choice = input("Press any key to input query. Press q to terminate the program: ")
