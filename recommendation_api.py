from flask import Flask, request, jsonify
#from flask_cors import CORS
from recommender import recommend_mov #Importing engine function
import pandas as pd
import pickle

app = Flask(__name__)

#Load the datasets
df = pickle.load(open('movies.pickle', 'rb'))

tfidf_matrix = pickle.load(open('engine.pickle', 'rb'))

#API endpoint
@app.route('/api', methods=['GET'])
def process_request():
    mov_id = request.args.get('movieID')
    #return mov_id
    #Call recommendation engine
    recommended_retro = recommend_mov(mov_id , df, tfidf_matrix)
    return jsonify(recommended_retro)


if __name__ == '__main__':
    app.run()