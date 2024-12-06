# Application of Hashing in NLP for Document Similarity

This project implements a solution to find the most similar text document with respect to a query text using hashing. The similarity between two text documents is computed using a specific formula involving word probabilities in the documents.

## Problem Overview

Given a set of text documents, we need to compute the similarity between each document and a query text. The similarity is computed based on the following formula:

\[
s(d1, d2) = \sum_{w \in V} p(w|d1) \log \left(\frac{p(w|d1)}{p(w|d2)}\right)
\]

Where:
- \( V \) is the vocabulary (all the unique words across all documents).
- \( p(w|d) \) is the probability of word \( w \) in document \( d \), computed as:
  
  \[
  p(w|d) = \frac{\text{count of } w \text{ in } d + 1}{\text{total number of words in } d + 2}
  \]

The documents and the query text are represented using a hash table, and for each query word, the probability is computed from the hash table to calculate the similarity score between the documents.

## Problem Steps

1. **Data Representation**: Each document is represented as a hash table where the key is the word, and the value is the frequency of that word in the document.
2. **Word Probability**: For each document, calculate the probability of each word using the formula:
   \[
   p(w|d) = \frac{\text{count of } w + 1}{\text{total number of words} + 2}
   \]
3. **Similarity Computation**: For a given query, compute the similarity score between the query and each document using the provided formula.
4. **Result**: The document with the highest similarity score to the query will be considered the most similar.

## Example Documents

### Document 1:
"The London Stock Exchange plans to launch its first marketing effort aimed at encouraging non-British corporations to seek a listing in London, said Mr Michael Lawrence, the exchange's new chief executive."

### Document 2:
"Mr Lawrence, who took charge in February, was outlining the changes he intends to put in place at the stock exchange."

### Document 3:
"The New York Stock Exchange and the US-based National Association of Securities Dealers Automated Quotation System share exchange have both had extensive marketing operations for years and have been successful in persuading leading multinational companies to seek listings in the US."

## Requirements

- Python 3.x

### Required Libraries

- Numpy
- Collections

You can install the required libraries using:

```bash
pip install numpy collections
# Application of Hashing in NLP for Document Similarity

This project implements a solution to find the most similar text document with respect to a query text using hashing. The similarity between two text documents is computed using a specific formula involving word probabilities in the documents.

## Problem Overview

Given a set of text documents, we need to compute the similarity between each document and a query text. The similarity is computed based on the following formula:

\[
s(d1, d2) = \sum_{w \in V} p(w|d1) \log \left(\frac{p(w|d1)}{p(w|d2)}\right)
\]

Where:
- \( V \) is the vocabulary (all the unique words across all documents).
- \( p(w|d) \) is the probability of word \( w \) in document \( d \), computed as:
  
  \[
  p(w|d) = \frac{\text{count of } w \text{ in } d + 1}{\text{total number of words in } d + 2}
  \]

The documents and the query text are represented using a hash table, and for each query word, the probability is computed from the hash table to calculate the similarity score between the documents.

## Problem Steps

1. **Data Representation**: Each document is represented as a hash table where the key is the word, and the value is the frequency of that word in the document.
2. **Word Probability**: For each document, calculate the probability of each word using the formula:
   \[
   p(w|d) = \frac{\text{count of } w + 1}{\text{total number of words} + 2}
   \]
3. **Similarity Computation**: For a given query, compute the similarity score between the query and each document using the provided formula.
4. **Result**: The document with the highest similarity score to the query will be considered the most similar.

## Example Documents

### Document 1:
"The London Stock Exchange plans to launch its first marketing effort aimed at encouraging non-British corporations to seek a listing in London, said Mr Michael Lawrence, the exchange's new chief executive."

### Document 2:
"Mr Lawrence, who took charge in February, was outlining the changes he intends to put in place at the stock exchange."

### Document 3:
"The New York Stock Exchange and the US-based National Association of Securities Dealers Automated Quotation System share exchange have both had extensive marketing operations for years and have been successful in persuading leading multinational companies to seek listings in the US."

## Requirements

- Python 3.x

### Required Libraries

- Numpy
- Collections

You can install the required libraries using:

```bash
pip install numpy collections

documents = [
    "The London Stock Exchange plans to launch its first marketing effort aimed at encouraging non-British corporations to seek a listing in London, said Mr Michael Lawrence, the exchange's new chief executive.",
    "Mr Lawrence, who took charge in February, was outlining the changes he intends to put in place at the stock exchange.",
    "The New York Stock Exchange and the US-based National Association of Securities Dealers Automated Quotation System share exchange have both had extensive marketing operations for years and have been successful in persuading leading multinational companies to seek listings in the US."
]

query = "Mr Lawrence, who took charge in February, was outlining the changes he intends to put in place at the stock exchange."

similar_document = find_most_similar_document(documents, query)
print(f"The most similar document is: {similar_document}")
