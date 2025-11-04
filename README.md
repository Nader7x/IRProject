# Information Retrieval System

A comprehensive document information searching and retrieval system that implements positional indexing, TF-IDF ranking, and boolean query processing with support for phrase queries.

## Overview

This project is an Information Retrieval (IR) system that allows users to search through a collection of documents using advanced techniques including:
- **Positional Indexing**: Maintains term positions within documents for phrase queries
- **TF-IDF Weighting**: Term Frequency-Inverse Document Frequency for document relevance ranking
- **Boolean Queries**: Support for AND, OR, and NOT operators
- **Cosine Similarity**: Vector space model for similarity calculations between queries and documents
- **Stemming & Tokenization**: Text preprocessing using NLTK

## Features

- 📚 **Positional Index Construction**: Build inverted index with term positions
- 🔍 **Multiple Query Types**: 
  - Simple keyword queries
  - Phrase queries (consecutive word matching)
  - Boolean queries (AND, OR, NOT operators)
- 📊 **TF-IDF Ranking**: Rank documents by relevance using normalized TF-IDF weights
- 📈 **Query Statistics**: Display detailed statistics including:
  - Term frequency (raw and logged)
  - Inverse document frequency (IDF)
  - TF-IDF weights
  - Normalized vectors
  - Cosine similarity scores
- 🎯 **Ranked Results**: Returns documents sorted by relevance

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Dependencies

Install required packages:

```bash
pip install nltk prettytable
```

Or install from the requirements file:

```bash
pip install -r REQUIREMENTS
```

### NLTK Data

After installing NLTK, download required data:

```python
import nltk
nltk.download('punkt')
```

## Usage

### Running the System

1. **Start the program**:
```bash
python main.py
```

2. **Wait for index construction**: The system will:
   - Load documents from `DocumentCollection/` folder
   - Tokenize and stem the documents
   - Build the positional index
   - Display various TF-IDF statistics tables

3. **Enter queries**: When prompted, enter your search query

4. **View results**: The system displays:
   - Query statistics
   - Product of query and document vectors
   - Similarity scores
   - Ranked list of matching documents

5. **Continue or exit**: Press any key to enter another query, or press 'q' to quit

### Query Examples

#### Simple Queries
```
Enter Query: mercy worser
```
Returns documents containing "mercy" and "worser" as a phrase.

#### Boolean Queries

**AND operator**:
```
Enter Query: mercy and caeser
```
Returns documents containing both terms.

**OR operator**:
```
Enter Query: antony or brutus
```
Returns documents containing either term.

**NOT operator**:
```
Enter Query: caeser not brutus
```
Returns documents containing "caeser" but not "brutus".

**Complex boolean queries**:
```
Enter Query: antony and caeser not brutus
```
Combines multiple operators.

## Project Structure

```
IRProject/
├── main.py                 # Main entry point and query processing loop
├── Tokenizing.py          # Text tokenization using NLTK
├── Stemming.py            # Word stemming using Porter Stemmer
├── PositionalIndex.py     # Positional index construction and retrieval
├── queryAnalysis.py       # Query processing and TF-IDF calculations
├── boolean.py             # Boolean query parser and processor
├── views.py               # Display utilities for statistics tables
├── DocumentCollection/    # Folder containing text documents (1.txt - 10.txt)
├── REQUIREMENTS           # Python dependencies
└── README.md              # This file
```

## Components Description

### main.py
- Orchestrates the entire IR system
- Loads and preprocesses documents
- Handles user interaction and query loop
- Coordinates query processing and result display

### Tokenizing.py
- Uses NLTK's word tokenizer
- Splits text into individual tokens
- Handles punctuation and special characters

### Stemming.py
- Implements Porter Stemmer algorithm via NLTK
- Reduces words to their root form
- Example: "running" → "run", "mercy" → "merci"

### PositionalIndex.py
- **createPositionalIndex()**: Builds the inverted index with positions
- **view_positional_index()**: Displays the positional index structure
- **is_consecutive()**: Checks if query terms appear consecutively in a document
- **retrieve_matched_docs()**: Returns documents matching a phrase query

### queryAnalysis.py
- **calculate_term_frequency()**: Counts term occurrences in query
- **calculate_log_term_frequency()**: Applies 1 + log₁₀(tf) weighting
- **calculate_idf()**: Computes inverse document frequency
- **calculate_tf_idf()**: Multiplies TF and IDF components
- **calculate_normalized_tf_idf()**: Normalizes by vector length
- **calculate_product_and_sum()**: Computes query-document similarity
- **sort_matched_docs()**: Ranks documents by similarity score

### boolean.py
- Parses boolean queries with AND, OR, NOT operators
- Implements boolean operations on document sets:
  - **AND**: Intersection of document sets
  - **OR**: Union of document sets
  - **NOT**: Complement of document set
- Handles operator precedence

### views.py
- Uses PrettyTable for formatted output
- Displays various statistics tables:
  - Term Frequency (TF)
  - Weighted Term Frequency (1 + log TF)
  - Document Frequency (DF) and IDF
  - TF-IDF weights
  - Normalized TF-IDF
  - Query statistics
  - Similarity scores

## Technical Details

### Algorithms & Techniques

1. **Tokenization**: NLTK word tokenizer splits text into tokens

2. **Stemming**: Porter Stemmer reduces words to root form

3. **Positional Indexing**: 
   - Structure: `{term: {doc_frequency, positionsAndTermFrequency: {doc_id: {positions: [], termFrequency}}}}`
   - Enables phrase query support

4. **TF-IDF Weighting**:
   - TF: `1 + log₁₀(term_frequency)` (logarithmic scaling)
   - IDF: `log₁₀(N / document_frequency)` where N = 10 documents
   - Weight: `TF × IDF`

5. **Vector Space Model**:
   - Documents and queries represented as vectors
   - Normalized by Euclidean length
   - Similarity: Cosine similarity (dot product of normalized vectors)

6. **Boolean Retrieval**:
   - Parses queries using regex
   - Processes NOT first, then OR, then AND
   - Returns document IDs matching boolean conditions

### Data Flow

1. **Indexing Phase**:
   ```
   Documents → Tokenization → Stemming → Positional Index
   ```

2. **Query Processing**:
   ```
   Query → Tokenization → Stemming → Boolean Processing (if applicable)
   ↓
   Document Retrieval → TF-IDF Calculation → Normalization
   ↓
   Similarity Calculation → Ranking → Results
   ```

## Document Collection

The system includes 10 sample documents in the `DocumentCollection/` folder containing Shakespeare-related terms and phrases. You can add your own documents by:

1. Creating text files named `11.txt`, `12.txt`, etc.
2. Placing them in the `DocumentCollection/` folder
3. Updating the `N` constant in `queryAnalysis.py` and `views.py` to reflect the new document count

## Limitations

- Current implementation assumes exactly 10 documents (hardcoded in several places)
- Boolean queries require proper spacing around operators
- Case-insensitive queries only
- No support for wildcards or regular expressions in queries
- Phrase queries must have consecutive terms

## Future Enhancements

- Dynamic document collection size
- Support for document addition/removal without restart
- Query expansion and spell checking
- Relevance feedback
- Web interface
- Support for larger document collections
- Advanced query syntax (wildcards, fuzzy matching)
- Multi-language support

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

This project is available for educational purposes.

## Authors

Developed as part of an Information Retrieval course project.