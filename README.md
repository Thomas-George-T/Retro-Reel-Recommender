# Retro Reel Recommender

Building a NLP & content-based recommendation engine API to recommend similar movies using Flask.

## Background

I love movies and was interested in working on a recommendation engine. So, I reached out to a Popular Android developer to create a recommendation engine for their retro reel app which serves retro movies from the 1900's onwards. Their requirement was to recommend similar movies as an API by passing only the movieID.

## Environment
- Numpy
- Pandas
- NLTK
- Rake
- Scikit learn
- Pickle
- Flask

## Methodology

After the initial EDA, I extracted keywords using Natural Language Processing from the Dataset. After feature engineering, I decided to build a recommender enginer using TF-ID vectorizer. 

I had previously used the following approaches to build the recommendation system using a countvectorizer:

1. Keywords as the feature.
2. Movie Titles as the feature.
3. Generating my own keywords using NLP as the feature.
4. Combining 2 & 3 to get the best of both.

I found that TF-ID vectorizer gave out a better quality of recommendations and chose that model.

Processes involved:

1. Data Acquisition
	Parse the deeply nested JSON file

2. Data Preprocessing
	Normalize the JSON file, make the data usable.
	
3. Feature Engineering
	Use the mentioned approaches for feature selection mentioned above.
	
4. Model building
	For each of the approaches, we determine the cosine similarity index and train our model.

5. Model Evaluation
	Compare the results with each of the models and determine the best model to productionize.
	
## Components	

## Resources 
1. [How to build a content-based movie recommender system with Natural Language Processing](https://towardsdatascience.com/how-to-build-from-scratch-a-content-based-movie-recommender-with-natural-language-processing-25ad400eb243)
