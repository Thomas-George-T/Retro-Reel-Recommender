# Retro Reel Recommender
Building a recommendation for movies mostly in the 19th century.

## Background

We build a content based recommendation engine. We use cosine similarity index to determine the similarity between the movies and recommend them.

## Methodology

The following approaches are used to build the recommendation system:

1. Keywords as the feature.
2. Movie Titles as the feature.
3. Generating our own keywords using NLP as the feature.
4. Combining 2 & 3 to get the best of both.

Processes involved:

1. Data Acquisition
	Parse the deeply nested JSON file

2. Data Preprocessing
	Normalize the JSON file, make the data usable.
	
3. Feature Engineering
	Use the mentioned approaches for feature selection mentioned above.
	
4. Model building
	For each of the approaches, we determine the cosine similarity index and train our model.

5. Model Comparison
	Compare the results with each of the models.

## Resources 
1. [How to build a content-based movie recommender system with Natural Language Processing](https://towardsdatascience.com/how-to-build-from-scratch-a-content-based-movie-recommender-with-natural-language-processing-25ad400eb243)