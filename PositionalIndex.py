def createPositionalIndex(stemmed_documents):
    positional_index = {}
    # Enumerate function: takes each entry inside a list and gives it an id starting from 1
    for doc_id, document in enumerate(stemmed_documents, start=1):
        for position, term in enumerate(document, start=1):
            # If the term is seen for the first time in collection, create its entry in the index
            if term not in positional_index:
                positional_index[term] = {"doc_frequency": 0, "positionsAndTermFrequency": {}}

            # If the term is seen for the first time inside the document, then create its list positions and append
            if doc_id not in positional_index[term]["positionsAndTermFrequency"]:
                positional_index[term]["positionsAndTermFrequency"][doc_id] = {"positions": [], "termFrequency": 0}
                positional_index[term]["doc_frequency"] += 1

            # Append the positions into the list
            positional_index[term]["positionsAndTermFrequency"][doc_id]["positions"].append(position)
            positional_index[term]["positionsAndTermFrequency"][doc_id]["termFrequency"] += 1
    return positional_index


def view_positional_index(positional_index):
    for term, info in positional_index.items():
        print(f"<{term}, {info['doc_frequency']};")
        for doc_id, positions in info["positionsAndTermFrequency"].items():
            print(f"  doc{doc_id}: {', '.join(map(str, positions['positions']))};")
        print(">")


def is_consecutive(id, query, positional_index):
    answer = positional_index[query[0]]["positionsAndTermFrequency"][id]["positions"]
    for i in range(1, len(query)):
        list1 = answer.copy()
        answer.clear()
        list2 = positional_index[query[i]]["positionsAndTermFrequency"][id]["positions"]
        answer = [value + 1 for value in list1 if value + 1 in list2]
        if len(answer) == 0:
            return False
    return True


def retrieve_matched_docs(query, positional_index):
    #Documents that contains all the words
    matchedDocs = []
    for i in range(1, 11):
        valid = True
        for word in query:
            if word not in positional_index:
                return []
            if i not in positional_index[word]["positionsAndTermFrequency"].keys():
                valid = False
        if valid:
            if is_consecutive(i, query, positional_index):
                matchedDocs.append(i)

    return matchedDocs