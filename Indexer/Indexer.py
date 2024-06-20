import json
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from pathlib import Path
import pickle

def load_corpus(file_path):
    corpus = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            obj = json.loads(line)
            doc = f"title: {obj['Sneaker Title']} content: {obj['Sneaker Details']}"
            corpus.append(doc)
    return corpus

def create_tf_idf_index(corpus):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(corpus)
    features = vectorizer.get_feature_names_out()
    tfidf_index = {feature: [] for feature in features}
    for i, feature in enumerate(features):
        for j in range(len(corpus)):
            if X[j, i] > 0:
                tfidf_index[feature].append((j, X[j, i]))
    return vectorizer, X

def save_to_file(data, filename, mode='w', encoding='utf-8'):
    with open(filename, mode, encoding=encoding) as f:
        for item in data:
            f.write(f"{item}\n")
    print(f"Text corpus data saved to {filename}")

def save_object_to_pickle(obj, filename):
    with open(filename, 'wb') as file:
        pickle.dump(obj, file)
    print(f"TF-IDF Index saved to {filename}")

def save_json_data(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    print(f"JSON data saved to {filename}")

def main():
    print("Script started")
    json_path = Path('C:/Users/arupd/Documents/Academics/CS 429/Project/Final Iteration V2/CS429-IR-Project-Deployment/Sneaker Space Indexer/ParsedDocument/ParsedDocument.json')
    corpus = load_corpus(json_path)
    print(f"Documents loaded successfully: {len(corpus)}")

    tfidf_index = create_tf_idf_index(corpus)
    save_object_to_pickle(tfidf_index, 'C:/Users/arupd/Documents/Academics/CS 429/Project/Final Iteration V2/CS429-IR-Project-Deployment/Sneaker Space Indexer/IndexFile/TF-IDF-index.pkl')
    save_to_file(corpus, 'C:/Users/arupd/Documents/Academics/CS 429/Project/Final Iteration V2/CS429-IR-Project-Deployment/Sneaker Space Indexer/TextCorpus/DocumentCorpus.txt')
    
    json_output_path = 'C:/Users/arupd/Documents/Academics/CS 429/Project/Final Iteration V2/CS429-IR-Project-Deployment/Sneaker Space Indexer/OutputParsedJSON/CorpusData.json'
    
    json_data = []
    for doc in corpus:
        parts = doc.split(" title: ", 1)
        if len(parts) > 1:
            content_part = parts[1].split(" content: ", 1)
            if len(content_part) > 1:
                title, content = content_part
                json_data.append({"title": title, "content": content})
            else:
                print("Error: Document format not recognized", doc)
        else:
            print("Error: Document format not recognized", doc)

    save_json_data(json_data, json_output_path)

if __name__ == '__main__':
    main()
