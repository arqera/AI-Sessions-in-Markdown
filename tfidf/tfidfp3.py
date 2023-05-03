import sys
import os
import math
from collections import defaultdict
from nltk.tokenize import word_tokenize

def calculate_tf(doc):
    tf = defaultdict(int)
    total_words = 0
    with open(doc, 'r') as f:
        for line in f:
            words = word_tokenize(line)
            for word in words:
                tf[word.lower()] += 1
                total_words += 1

    for word in tf:
        tf[word] /= total_words

    return tf

def calculate_idf(docs):
    idf = defaultdict(int)
    total_docs = len(docs)

    for doc in docs:
        unique_words = set()
        with open(doc, 'r') as f:
            for line in f:
                words = word_tokenize(line)
                for word in words:
                    unique_words.add(word.lower())

        for word in unique_words:
            idf[word] += 1

    for word in idf:
        idf[word] = math.log(total_docs / idf[word])

    return idf

def calculate_tfidf(doc_tf, idf):
    tfidf = {}
    for word, tf in doc_tf.items():
        tfidf[word] = tf * idf[word]

    return tfidf

def main():
    docs = sys.argv[1:]

    idf = calculate_idf(docs)

    for doc in docs:
        tf = calculate_tf(doc)
        tfidf = calculate_tfidf(tf, idf)

        output_filename = f"{doc}_tfidf.txt"
        with open(output_filename, 'w') as f:
            for word, score in tfidf.items():
                f.write(f"{word} {score}\n")

if __name__ == "__main__":
    main()
