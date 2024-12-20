**Application of Hashing in NLP**

Write Python program for the problem below.  

You are given a set of text documents and your goal is to find the most similar text document with respect to a query text. The similarity is computed between two text documents, d1 and d2 as follows:

similarityd1,d2= w∈Vp(w)d1 log⁡(pd1pd2)

Where V is the vocabulary (all the words), pd is the probability of the word w in d.

p(w)d=(number of times w present in d)+1(total number of words in d)+2

Your objective is to represent each document in a hash table and when the query comes in, search for each query word in each of the documents to find the probability. Finally compute the similarity score.
"""

'''Here is the updated code to extract the text files
from the zip file, store each document in a dictionary
with word frequencies, and store these dictionaries in a hash table'''

import zipfile

# Initialize an empty hash table
hash_table = {}

# Open the zip file
with zipfile.ZipFile('/content/Document.zip', 'r') as zip_ref:
    # Iterate over each file in the zip file
    for file in zip_ref.namelist():
        # Check if the file is a text file
        if file.endswith('.txt'):
            # Extract the document ID from the file name
            doc_id = file.split('.')[0]
            # Initialize an empty dictionary for the document
            doc_dict = {}
            # Open the file and read its contents
            with zip_ref.open(file, 'r') as f:
                text = f.read().decode('utf-8')
                # Split the text into words
                words = text.lower().split()
                # Iterate over each word
                for word in words:
                    # Increment the word's frequency in the dictionary
                    doc_dict[word] = doc_dict.get(word, 0) + 1
            # Sort the dictionary by keys (words)
            doc_dict = dict(sorted(doc_dict.items()))
            # Store the dictionary in the hash table
            hash_table[doc_id] = doc_dict

# Print the hash table
for doc_id, doc_dict in hash_table.items():
    print(f"Document {doc_id}:")
    for word, freq in doc_dict.items():
        print(f"{word}: {freq}")
    print()

# Initialize an empty dictionary for the query text
query_dict = {}

# Open the query text file
with open('/content/Query.txt', 'r') as f:
    # Read the contents of the file
    text = f.read()
    # Split the text into words
    words = text.lower().split()
    # Iterate over each word
    for word in words:
        # Increment the word's frequency in the dictionary
        query_dict[word] = query_dict.get(word, 0) + 1

# Sort the dictionary by keys (words)
query_dict = dict(sorted(query_dict.items()))

# Print the query dictionary
print("Query Dictionary:")
for word, freq in query_dict.items():
    print(f"{word}: {freq}")

# Initialize an empty array to store the total number of words in each text file
total_words_array = []

# Iterate over each document dictionary in the hash table
for doc_id, doc_dict in hash_table.items():
    # Calculate the total number of words in the document
    total_words = sum(doc_dict.values())
    # Append the total number of words to the array
    total_words_array.append(total_words)

# Print the array
print("Total Words Array:")
print(total_words_array)

# Calculate the total number of words in the query text file
total_query_words = sum(query_dict.values())

# Print the total number of words in the query text file
print("Total Query Words:")
print(total_query_words)

# Calculate the probability for each word in the query dictionary
query_dict_prob = {word: ((freq + 1) / (total_query_words + 2)) for word, freq in query_dict.items()}

# Print the query dictionary with probabilities
print("Query Dictionary with Probabilities:")
for word, prob in query_dict_prob.items():
    print(f"{word}: {prob}")

#Here is the code to replace the frequency with the probability in each document dictionary in the hash table:

# Initialize an empty hash table to store the document dictionaries with probabilities
hash_table_prob = {}
# Keep track of the index for total_words_array
index = 0

# Iterate over each document dictionary in the hash table
for doc_id, doc_dict in hash_table.items():

    # Get the total number of words in the document from the total_words_array
    total_doc_words = total_words_array[index] # Use index variable here

    # Calculate the probability for each word in the document dictionary
    doc_dict_prob = {word: ((freq + 1) / (total_doc_words + 2)) for word, freq in doc_dict.items()}

    # Store the document dictionary with probabilities in the hash table
    hash_table_prob[doc_id] = doc_dict_prob
    index += 1 # Increment index for the next iteration

# Print the hash table with probabilities
print("Hash Table with Probabilities:")
for doc_id, doc_dict_prob in hash_table_prob.items():
    print(f"Document {doc_id}:")
    for word, prob in doc_dict_prob.items():
        print(f"{word}: {prob}")
    print()

# Here is the code to create a function to find the similarity between the query text file and all documents:

import math

def calculate_similarity(query_dict_prob, hash_table_prob):
    # Initialize an empty list to store the similarities
    similarities = []

    # Iterate over each document dictionary in the hash table
    for doc_id, doc_dict_prob in hash_table_prob.items():
        # Initialize the similarity for the current document to 0
        similarity = 0

        # Iterate over each word in the query dictionary
        for word, prob_query in query_dict_prob.items():
            # Check if the word is present in the document dictionary
            if word in doc_dict_prob:
                # Calculate the probability of the word in the document
                prob_doc = doc_dict_prob[word]

                # Calculate the similarity for the current word
                similarity += prob_query * math.log(prob_query / prob_doc)

        # Append the similarity for the current document to the list
        similarities.append((doc_id, similarity))

    # Return the list of similarities
    return similarities

# Calculate the similarities
similarities = calculate_similarity(query_dict_prob, hash_table_prob)

# Print the similarities
print("Similarities:")
for doc_id, similarity in similarities:
    print(f"Document {doc_id}: {similarity}")

# Print the best similarity
best_similarity = max(similarities, key=lambda x: x[1])
print(f"\n\n Best Similarity: Document {best_similarity[0]} with similarity {best_similarity[1]}")

"""### **Output :**

---



---



Best Similarity: Document doc/document_19 with similarity 1.573983918976757
"""
