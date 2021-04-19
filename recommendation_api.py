from flask import Flask, request, jsonify
#from flask_cors import CORS
from recommender import recommend_mov #Importing engine function
import pandas as pd
import pickle
import re

app = Flask(__name__)

#Load the datasets
df = pickle.load(open('movies.pickle', 'rb'))

tfidf_matrix = pickle.load(open('engine.pickle', 'rb'))

remove_punct = re.compile("(\.)|(\')|(\:)|(\,)|(\-)|(\$)|(\")")

#API endpoint
@app.route('/api', methods=['GET'])
def process_request():
    mov_title = request.args.get('title')
    
    #Convert the title into lowercase and remove special characters
    movTitle = re.sub(r'[^\w\s]', '', mov_title.lower())
    
    #Remove unwanted whitespaces & Call recommendation engine
    recommended_retro = recommend_mov(movTitle.strip() , df, tfidf_matrix)
    return jsonify(recommended_retro)


if __name__ == '__main__':
    app.run()