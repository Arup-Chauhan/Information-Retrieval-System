import pandas as pd
import nltk
from collections import defaultdict
from itertools import groupby
import pickle
import math
nltk.download('words')
from nltk.corpus import words
correct_words = words.words()

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_index(tfidf_index_file):
    with open(tfidf_index_file, 'rb') as f:
        tfidf_vectorizer, tfidf_matrix = pickle.load(f)

    return tfidf_vectorizer, tfidf_matrix


def searchQuery(query, K, output_file):
    
    tfidf_vectorizer, tfidf_matrix = load_index(r'C:\Users\arupd\Documents\Academics\CS 429\Project\Final Iteration V2\CS429-IR-Project-Deployment\Sneaker Space Indexer\IndexFile\TF-IDF-index.pkl')


    df_documents = pd.read_json(output_file)

    query_vector = tfidf_vectorizer.transform([query])
    query_cosine_similarities = cosine_similarity(query_vector, tfidf_matrix)
    most_similar_indices = query_cosine_similarities.argsort()[0][::-1]


    results = []
    for idx in most_similar_indices[:K]:
        similarity_score = query_cosine_similarities[0][idx]
        document = df_documents.iloc[idx]['Sneaker Details']
        title = df_documents.iloc[idx]['Sneaker Title']
        docId = str(idx)
        results.append({ 'score': similarity_score, 'content': document, 'title' : title,  'Id': docId})

    return results


def get_vocab(index):
    return [term for term in index.keys()]

def spelling_correction(query):
    corrected_query = ''
    for word in query.split():
        temp = [(nltk.edit_distance(word, w),w) for w in correct_words if w[0]==word[0]]
        corrected_query += sorted(temp, key = lambda val:val[0])[0][1] + ' '
    return corrected_query


