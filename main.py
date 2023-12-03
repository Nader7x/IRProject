import Tokenizing
import Stemming
import PositionalIndex
import queryAnalysis

import views

documents = []
tokenizedDocuments = []
stemmedDocuments = []

for i in range(1, 11):
    with open('./DocumentCollection/' + str(i) + ".txt", 'r') as file:
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


while choice != "q" and choice != "Q":
    query = input("Enter Query: ").lower()
    query = Tokenizing.tokenize(query)

    stemmed_query = []
    for word in query:
        newStr = Stemming.Stemmer(word)
        stemmed_query.append(newStr)
    print(f"stemmed-> {stemmed_query}")

    query_frequencies = queryAnalysis.calculate_term_frequency(stemmed_query)
    query_logged_frequencies = queryAnalysis.calculate_log_term_frequency(query_frequencies)
    idf_dict = queryAnalysis.calculate_idf(positional_index)
    query_tf_idf_dict = queryAnalysis.calculate_tf_idf(stemmed_query, query_logged_frequencies, idf_dict)
    query_length = queryAnalysis.calculate_query_length(query_tf_idf_dict)
    query_normalized_tf_idf = queryAnalysis.calculate_normalized_tf_idf(query_length, query_tf_idf_dict)

    docs_normalized_tf_idf = views.create_normalized_tf_idf(positional_index) #ok
    right_docs = PositionalIndex.retrieve_matched_docs(stemmed_query, positional_index)
    product_and_sum_dictionary = queryAnalysis.calculate_product_and_sum(query_normalized_tf_idf,
                                                                         docs_normalized_tf_idf, right_docs,
                                                                         stemmed_query)
    print(f"outer product -> {product_and_sum_dictionary}")
    print(f"right docs--> {right_docs}")
    print(f"docs_normalized_tf_idf--> {docs_normalized_tf_idf}")
    sorted_matched_docs = queryAnalysis.sort_matched_docs(product_and_sum_dictionary, right_docs)

    views.print_query_statistics(stemmed_query, query_frequencies, query_logged_frequencies, idf_dict,
                                 query_tf_idf_dict, query_normalized_tf_idf)
    views.print_query_product(product_and_sum_dictionary, stemmed_query)
    views.print_similarities_query_length_matched_docs(query_length, product_and_sum_dictionary, sorted_matched_docs)
    print("\n=================================================================================================")
    choice = input("Press any key to input query. Press q to terminate the program: ")