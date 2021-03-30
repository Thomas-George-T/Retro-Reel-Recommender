import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def recommend_mov(movieId, df, tfidf_matrix):
    
    try:
        indices = pd.Series(df.ID)
        # getting the index of the movie that matches the title
        idx = indices[indices == movieId].index[0]

    except:
        return 'MovieID not found, Please try again'
   
    recommended_movies = []
    
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    
    # creating a Series with the similarity scores in descending order
    score_series = pd.Series(cosine_sim[idx]).sort_values(ascending = False)

    # getting the indexes of the 10 most similar movies
    top_10_indexes = list(score_series.iloc[1:11].index)
    
    # populating the list with the titles of the best 10 matching movies
    for i in top_10_indexes:
        recommended_movies.append(list(df.ID)[i])     
      
    return recommended_movies