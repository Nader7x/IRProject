from prettytable import PrettyTable
import math

N = 10


def print_tf(positional_index):
    print("Term Frequency(TF)")
    terms = sorted(positional_index.keys())

    tf_table = PrettyTable()
    tf_table.field_names = ["Terms", "d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "d10"]

    for term in terms:
        list_row = [term]
        keys_of_term_frequency = positional_index[term]["positionsAndTermFrequency"].keys()
        for i in range(1, 11):
            if i in keys_of_term_frequency:
                list_row.append(positional_index[term]["positionsAndTermFrequency"][i]['termFrequency'])
            else:
                list_row.append(0)
        tf_table.add_row(list_row)
    print(tf_table)


def print_log_tf(positional_index):
    print("w tf(1+ log tf)")
    terms = sorted(positional_index.keys())

    tf_table = PrettyTable()
    tf_table.field_names = ["Terms", "d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "d10"]

    for term in terms:
        list_row = [term]
        keys_of_term_frequency = positional_index[term]["positionsAndTermFrequency"].keys()
        for i in range(1, 11):
            if i in keys_of_term_frequency:
                list_row.append(round(1 + math.log10(positional_index[term]["positionsAndTermFrequency"][i]['termFrequency']), 9))
            else:
                list_row.append(0)
        tf_table.add_row(list_row)
    print(tf_table)


def print_df_and_idf(positional_index):
    terms = sorted(positional_index.keys())

    tf_table = PrettyTable()
    tf_table.field_names = ["Terms", "df", "idf"]

    for term in terms:
        list_row = [term]
        df = positional_index[term]["doc_frequency"]
        list_row.append(df)
        list_row.append(round(math.log10(N/df), 9))
        tf_table.add_row(list_row)
    print(tf_table)


my_map = {}


def print_tf_idf(positional_index):
    global my_map
    print("tf * idf")
    terms = sorted(positional_index.keys())

    tf_table = PrettyTable()
    tf_table.field_names = ["Terms", "d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "d10"]

    for term in terms:
        list_row = [term]
        keys_of_term_frequency = positional_index[term]["positionsAndTermFrequency"].keys()
        for i in range(1, 11):
            if i in keys_of_term_frequency:
                df = positional_index[term]["doc_frequency"]
                idf = math.log10(N / df)
                tf = 1 + math.log10(positional_index[term]["positionsAndTermFrequency"][i]['termFrequency'])
                list_row.append(round(tf * idf, 9))
                if i in my_map:
                    my_map[i] += math.pow(tf * idf, 2)
                else:
                    my_map[i] = math.pow(tf * idf, 2)
            else:
                list_row.append(0)
        tf_table.add_row(list_row)
    print(tf_table)



def print_doc_length():
    global my_map
    doc_length_table = PrettyTable()
    doc_length_table.field_names = ["docs", "length"]
    for i in range(1, 11):
        doc_length_table.add_row([f"doc {str(i)} length", round(math.sqrt(my_map[i]), 9)])
    print(doc_length_table)


def print_normalized_tf_idf(positional_index):
    global my_map
    print("Normalized tf.idf")
    terms = sorted(positional_index.keys())

    tf_table = PrettyTable()
    tf_table.field_names = ["Terms", "d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "d10"]

    for term in terms:
        list_row = [term]
        keys_of_term_frequency = positional_index[term]["positionsAndTermFrequency"].keys()
        for i in range(1, 11):
            if i in keys_of_term_frequency:
                df = positional_index[term]["doc_frequency"]
                idf = math.log10(N / df)
                tf = 1 + math.log10(positional_index[term]["positionsAndTermFrequency"][i]['termFrequency'])
                doc_len = math.sqrt(my_map[i])
                list_row.append(round((tf * idf)/doc_len, 9))
            else:
                list_row.append(0)
        tf_table.add_row(list_row)
    print(tf_table)


def create_normalized_tf_idf(positional_index):
    global my_map
    terms = sorted(positional_index.keys())
    dictionary = {}

    for term in terms:
        list_row = [0]
        keys_of_term_frequency = positional_index[term]["positionsAndTermFrequency"].keys()
        for i in range(1, 11):
            if i in keys_of_term_frequency:
                df = positional_index[term]["doc_frequency"]
                idf = math.log10(N / df)
                tf = 1 + math.log10(positional_index[term]["positionsAndTermFrequency"][i]['termFrequency'])
                doc_len = math.sqrt(my_map[i])
                list_row.append((tf * idf)/doc_len)
            else:
                list_row.append(0)
        dictionary[term] = list_row
    return dictionary


def print_query_statistics(stemmed_words_list, tf_raw_dict, logged_tf_dict, idf_dict, tf_idf_dict, normalized_dict):
    print("\n=======================================================================\n")
    print("Query Statistics")
    table = PrettyTable()
    table.field_names = ["Terms", "tf raw", "logged tf", "idf", "tf-idf", "normalized"]
    for word in stemmed_words_list:
        row_list = [word, tf_raw_dict[word], round(logged_tf_dict[word], 9), round(idf_dict[word], 9), round(tf_idf_dict[word], 9), round(normalized_dict[word], 9)]
        table.add_row(row_list)
    print(table)


def print_query_product(product_dict, stemmed_words_list):
    print("product (query * matched docs)")
    table = PrettyTable()
    docs = sorted(dict(product_dict).keys())
    attribute_names = ["terms"]
    for id in docs:
        attribute_names.append("doc" + str(id))
    table.field_names = attribute_names

    row_list = []
    for word in stemmed_words_list:
        row_list.clear()
        row_list.append(word)
        for docId in product_dict:
            row_list.append(round(product_dict[docId]['map'][word], 9))
        table.add_row(row_list)

    row_list = ["sum"]
    for docId in product_dict:
        row_list.append(round(product_dict[docId]['sum'], 9))
    table.add_row(row_list)
    print(table)


def print_similarities_query_length_matched_docs(query_length, product_dict, matched_docs):
    print(f"Query Length: {round(query_length, 9)}")
    docs = sorted(dict(product_dict).keys())
    for docId in docs:
        print(f"Similarity(q, doc{docId})  = {round(product_dict[docId]['sum'], 9)}")

    print(matched_docs)
    document_list = ["doc"+str(docId) for docId in matched_docs]
    print(f"Returned Docs : {document_list}")
