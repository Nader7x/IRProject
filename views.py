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
                list_row.append(1 + math.log10(positional_index[term]["positionsAndTermFrequency"][i]['termFrequency']))
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
        list_row.append(math.log10(N/df))
        tf_table.add_row(list_row)
    print(tf_table)


my_map = {}


def print_tf_idf(positional_index):
    print("tf*idf")
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
                list_row.append(tf * idf)
                # if i in my_map:
                #     my_map += math.pow(tf*idf,2)
            else:
                list_row.append(0)
        tf_table.add_row(list_row)
    print(tf_table)