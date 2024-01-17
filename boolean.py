import re
import copy
import Tokenizing
from PositionalIndex import retrieve_matched_docs
import Stemming


def boolean(query,positional_index):
    result = re.split(r'(\b(?:and|or|not)\b)', query)
    result = [item.strip() for item in result if item.strip()]
    not_indices = [i for i in range(len(result)) if result[i] == 'not'] # get the indices of the not
    for i in sorted(not_indices, reverse=True):
        stemmed_query = []
        query = Tokenizing.tokenize(result[i + 1].lower())
        for word in query:
            newStr = Stemming.Stemmer(word)
            stemmed_query.append(newStr)
        retrieved_docs = retrieve_matched_docs(stemmed_query, positional_index)
        # inverse the retrieved docs to get the not
        retrieved_docs = list(set(range(1, 11)) - set(retrieved_docs))
        result = result[:i] + result[i + 2:]
        # insert the retrieved docs in the place of the not
        result.insert(i, retrieved_docs)
    or_indices = [i for i in range(len(result)) if result[i] == 'or'] # get the indices of the or
    for i in sorted(or_indices, reverse=True):
        before = []
        after = []
        before_stemmed_query = []
        if type(result[i - 1]) == list:
            before = result[i - 1]
        else:
            query = Tokenizing.tokenize(result[i - 1].lower())
            for word in query:
                newStr = Stemming.Stemmer(word)
                before_stemmed_query.append(newStr)
                retrieved_docs = retrieve_matched_docs(before_stemmed_query, positional_index)
                before = retrieved_docs.copy()
        if type(result[i + 1]) == list:
            after = result[i + 1]
        else:
            query = Tokenizing.tokenize(result[i + 1].lower())
            after_stemmed_query = []
            for word in query:
                newStr = Stemming.Stemmer(word)
                after_stemmed_query.append(newStr)
                retrieved_docs = retrieve_matched_docs(after_stemmed_query, positional_index)
                after = retrieved_docs.copy()
        # union the two lists
        union = list(set(before) | set(after))
        result = result[:i - 1] + result[i + 2:]
        # insert the union in the place of the or
        result.insert(i - 1, union)
    and_indices = [i for i in range(len(result)) if result[i] == 'and'] # get the indices of the and
    for i in sorted(and_indices, reverse=True):
        before = []
        after = []
        before_stemmed_query = []
        if type(result[i - 1]) == list:
            before = result[i - 1]
        else:
            query = Tokenizing.tokenize(result[i - 1].lower())
            for word in query:
                newStr = Stemming.Stemmer(word)
                before_stemmed_query.append(newStr)
                retrieved_docs = retrieve_matched_docs(before_stemmed_query, positional_index)
                before = retrieved_docs.copy()
        if type(result[i + 1]) == list:
            after = result[i + 1]
        else:
            query = Tokenizing.tokenize(result[i + 1].lower())
            after_stemmed_query = []
            for word in query:
                newStr = Stemming.Stemmer(word)
                after_stemmed_query.append(newStr)
                retrieved_docs = retrieve_matched_docs(after_stemmed_query, positional_index)
                after = retrieved_docs.copy()
        # intersection the two lists
        intersection = list(set(before) & set(after))
        result = result[:i - 1] + result[i + 2:]
        # insert the intersection in the place of the and
        result.insert(i - 1, intersection)
    return result[0]
