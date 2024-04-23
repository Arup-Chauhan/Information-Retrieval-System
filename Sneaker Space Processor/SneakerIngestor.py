from flask import Flask, render_template, redirect, jsonify, request
import pickle
from sklearn.metrics.pairwise import cosine_similarity
from flask_cors import CORS
import SneakerQueryProcessor


app = Flask(__name__)
CORS(app)

# @app.route('/', methods=['GET'])
# def index():
#     return jsonify({'top_k_urls': 2})


@app.route("/search", methods = ['POST'])
def handle_query():
    
    query = request.get_json()['query']
    K = request.get_json()['top_k']
    output_file = r'C:\Users\arupd\Documents\Academics\CS 429\Project\Final Iteration V2\CS429-IR-Project-Deployment\Sneaker Space Indexer\FinalOutputJSON\FilteredJSON.json'

    results = SneakerQueryProcessor.searchQuery(query, K, output_file)
    return jsonify(results)
    




if __name__ == '__main__':
    app.run(debug=True, port=3000)