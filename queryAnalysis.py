import math

N = 10


def calculate_term_frequency(stemmed_query):
    dictionary = {}
    for word in stemmed_query:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    return dictionary


def calculate_log_term_frequency(doc_freq_dictionary):
    dictionary = dict(doc_freq_dictionary).copy()

    for word in dictionary:
        dictionary[word] = 1 + math.log10(dictionary[word])
    return dictionary


def calculate_idf(positional_index):
    terms = sorted(positional_index.keys())
    dictionary = {}
    for term in terms:
        df = positional_index[term]["doc_frequency"]
        dictionary[term] = math.log10(N / df)

    return dictionary


def calculate_tf_idf(stemmed_words, logged_tf_dict, idf_dict):
    dictionary = {}
    for word in stemmed_words:
        dictionary[word] = logged_tf_dict[word] * idf_dict[word]
    return dictionary


def calculate_query_length(tf_idf_dict):
    query_length = 0
    for word in tf_idf_dict:
        query_length += math.pow(tf_idf_dict[word], 2)
    return math.sqrt(query_length)


def calculate_normalized_tf_idf(query_length, tf_idf_dict):
    dictionary = dict(tf_idf_dict).copy()
    for word in dictionary:
        dictionary[word] = dictionary[word]/query_length
    return dictionary


def calculate_product_and_sum(normalized_query_dict, normalized_docs_dict, matched_docs_list, stemmed_query_list):
    dictionary = {}

    for docsId in matched_docs_list:
        dictionary[docsId] = {'map': {}, 'sum': 0}

    for docId in matched_docs_list:
        for word in stemmed_query_list:
            dictionary[docId]['map'][word] = normalized_query_dict[word] * normalized_docs_dict[word][docId]
            dictionary[docId]['sum'] += (normalized_query_dict[word] * normalized_docs_dict[word][docId])
    return dictionary


def sort_matched_docs(prod_and_sum_dict, right_docs):
    print(f"prod-> {prod_and_sum_dict}")
    print(f"right-> {right_docs}")
    docs_list = []
    for docId in right_docs:
        docs_list.append((prod_and_sum_dict[docId]['sum'], docId))
    docs_list.sort(key=lambda x: (x[0], x[1]), reverse=True)
    print(f"docs_list --> {docs_list}")
    sorted_list = []
    for pair in docs_list:
        sorted_list.append(pair[1])
    return sorted_list