import sys
import math
from collections import defaultdict

def process_document(filename):
    with open(filename, 'r') as f:
        words = f.read().lower().split()
        word_count = defaultdict(int)
        for word in words:
            word_count[word] += 1
    return word_count

def calculate_tfidf(doc_tf, idf):
    tfidf = {}
    for word, tf in doc_tf.items():
        if word in idf:
            tfidf[word] = tf * idf[word]
        else:
            tfidf[word] = 0
    return tfidf

def main():
    doc_filenames = sys.argv[1:-1]
    idf_filename = sys.argv[-1]

    # Process IDF file
    with open(idf_filename, 'r') as f:
        lines = f.readlines()
    idf = {}
    for line in lines:
        freq, word = line.strip().split()
        idf[word] = math.log(float(len(doc_filenames)) / float(freq))

    # Process documents and calculate TF-IDF scores
    for doc_filename in doc_filenames:
        doc_tf = process_document(doc_filename)
        tfidf = calculate_tfidf(doc_tf, idf)
        output_filename = "{}_tfidf.txt".format(doc_filename)
        with open(output_filename, 'w') as f:
            for word, score in tfidf.items():
                f.write("{} {}\n".format(word, score))

if __name__ == "__main__":
    main()
