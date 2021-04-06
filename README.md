![GitHub](https://img.shields.io/github/license/Thomas-George-T/Retro-Reel-Recommender?style=flat)
![GitHub top language](https://img.shields.io/github/languages/top/Thomas-George-T/Retro-Reel-Recommender?style=flat)
![GitHub language count](https://img.shields.io/github/languages/count/Thomas-George-T/Retro-Reel-Recommender?style=flat)
![GitHub last commit](https://img.shields.io/github/last-commit/Thomas-George-T/Retro-Reel-Recommender?style=flat)
![ViewCount](https://views.whatilearened.today/views/github/Thomas-George-T/Retro-Reel-Recommender.svg?cache=remove)

# Retro Reel Recommender

<p align="center">
	<a href="#">
		<img src="https://raw.githubusercontent.com/Thomas-George-T/Thomas-George-T/master/assets/flask.svg" alt="Flask" title="Flask" width ="100" />
	</a>
	<a href="#">
		<img src="https://raw.githubusercontent.com/Thomas-George-T/Thomas-George-T/master/assets/heroku.svg" alt="Heroku" title="Heroku" width ="400" hspace=80 />
	</a>
	<a href="#">
		<img src="https://raw.githubusercontent.com/Thomas-George-T/Thomas-George-T/master/assets/python.svg" alt="Python" title="Python" width ="120" />
	</a>
</p>

## Description

Building a Content-based recommendation engine API to recommend similar movies using NLP, Flask and Heroku. We generate keywords using NLTK, use it to build the model. Generate an API request using Flask and deploy it to Heroku.

## Demo

Query String: /api?movieID=Insert-Movie-ID-Here

Sample API : https://retro-reel-recommendation-api.herokuapp.com/api?movieID=b70eec12b79148dfbc97ac3b69ca49bf

## Background

I love movies and was interested in working on a recommendation engine. So, I reached out to a Popular Android developer to create a recommendation engine for their retro reel app which serves retro movies from the 1900's onwards. Their requirement was to recommend similar movies as an API by passing only the movieID.

## Environment
- Python
- Numpy
- Pandas
- NLTK
- Rake
- Scikit learn
- Pickle
- Flask
- Heroku

## Methodology

After the initial EDA, I extracted keywords using Natural Language Processing from the Dataset. After feature engineering, I decided to build a recommender enginer using TF-ID vectorizer. 

I had previously used the following approaches to build the recommendation system using a countvectorizer:

1. Keywords as the feature.
2. Movie Titles as the feature.
3. Generating my own keywords using NLP as the feature.
4. Combining 2 & 3 to get the best of both.

I found that TF-ID vectorizer gave out a better quality of recommendations and chose that model.

### Processes involved:

1. Data Acquisition
	Parse the deeply nested JSON file

2. Data Preprocessing
	Normalize the JSON file, make the data usable.
	
3. Feature Engineering
	Use the mentioned approaches for feature selection mentioned above.
	
4. Model building
	For each of the approaches, we determine the cosine similarity index and post training, the model is pickled.

5. Model Evaluation
	Compare the results with each of the models and determine the best model to productionize.
	
## Components	

- [Retro_Reel_Recommender](Retro_Reel_Recommender.ipynb) : To demonstrate the entire data science lifecycle.
- [recommender](recommender.py) : Has functions to return the recommendations for the API calls.
- [recommendation_api](recommendation_api.py) : Flask app to run the recommender engine as an API.

## Feedback

Please leave me a feedback of how my engine performed in the Issues tab or email me. Feel free to try out the API calls with different movieID's from the list below.

|  Sr.no |                ID                |                   Title                  |
|-------:|:--------------------------------:|:----------------------------------------:|
|    0   | b70eec12b79148dfbc97ac3b69ca49bf |           angel on my shoulder           |
|    1   | 1950e4a11304438dbfd4792a908fc76f |            flirting with fate            |
|    2   | 37d8cae8d87f4dbc9cf8967454537afb |                  detour                  |
|    3   | b99dd03c00cc4fb9b2d4ad26082de498 |               the big trees              |
|    4   | 5566ce75b5954f3dad323c2f154856a3 |              the jungle book             |
|    5   | 62e08996bb034303a417d10e136bedda |              the lost world              |
|    6   | 74ac96777a4d404b8eba028e44f8f06b |                 suddenly                 |
|    7   | 4014bc52406d47d88f077ab9ca6e988c |           bloody pit of horror           |
|    8   | 97063c49fbe94966a7f883594896855b |         charlie chaplins the rink        |
|    9   | 3cb4bd7eed36485c8faf54c41c243f20 |               texas terror               |
|   10   | 5807bf3c700d4a659a74fc15de8b923c |               the iron mask              |
|   11   | 734953cfa879481ca4fd1a264b41c4ad |               barefoot boy               |
|   12   | 47390e712fbe452a9ab62132db7836fe |                borderline                |
|   13   | 19eff70e96924a6496635736387e6fc5 |       charlie chaplins the vagabond      |
|   14   | 7150410637e24c4ca5e67bdcc41085ac |              galloping romeo             |
|   15   | d8594f27c94b481b99985c5855c17c9e |              his girl friday             |
|   16   | 5d55325b03ce4b2c8f3396638f068a1c |              the star packer             |
|   17   | 03e766ae999c4d05b2d3cc490b38e06c |              scarlet street              |
|   18   | 14d208c6f0264d5eb1ce83a60b19ef43 | charlie chaplins a burlesque on   carmen |
|   19   | 92b566058c1443dd90f01342ecd763b5 |       charlie chaplins the pawnshop      |
|   20   | db728e8c6c134a43b789d72953d360e4 |                  manfish                 |
|   21   | 9dc976bf36904926928abcdcf7c924a5 |             carnival of souls            |
|   22   | fe5901c51ca44c8cb40507949b2f2da0 |         the snows of kilimanjaro         |
|   23   | d3ae2ba361ca496b82c5622c8b626277 |                  millie                  |
|   24   | 9db604ab028c4d2ca7f299d5ed610dfc |              my man godfrey              |
|   25   | 315033f27af947ab8bcd404e1ee9a101 |            million dollar kid            |
|   26   | 02d4f14c804947ca927b7455141bcea9 |                the outlaw                |
|   27   | ea77b983d3644fdd9bc6282cd60e40bc |          she gods of shark reef          |
|   28   | 41a069f0d71042be908429adf7e1324e |          plan 9 from outer space         |
|   29   | 78baeb60405941728509272c0991e293 |              a star is born              |
|   30   | 38b77b1141af4b468413c62cadd916a6 |         night of the living dead         |
|   31   | 16c4b6cf6d1e411db4953b205ecbc102 |              penny serenade              |
|   32   | 1e06d628af564e20a1beb9837d100fe1 |        the brain that wouldnt die        |
|   33   | 33542b5771474f0c9493e5dc747d5806 |             call of the yukon            |
|   34   | 62b36e28f1d6443c8bef36f7cd216a7d |             a christmas carol            |
|   35   | 721d6c4a6c0746f3893a7721372da07a |               ambush valley              |
|   36   | 0570da091e71401295cb5f8cd33ea336 |            a stranger in town            |
|   37   | 09bd0daa54ac4c349bfa1e45687a37f4 |               the big combo              |
|   38   | 37e2c6e074394731bf686c2a4ebbf3c1 |     charlie chaplins a fair exchange     |
|   39   | 93408d720a73433381f3e35c90467eaa |               danger flight              |
|   40   | 1ed15145f6e24781a2d7841caaad56c2 |               the big show               |
|   41   | 7d40352cdcfb4199acf7324a4a7c60e8 |             a bucket of blood            |
|   42   | c03c4921cf1d4fba851197ec99c51da6 |           house on haunted hill          |
|   43   | 0254461677cf4d0aa48319e226a68ca5 |        teenagers from outer space        |
|   44   | 2822e173b50243348e49c8813510f563 |                 the ghoul                |
|   45   | cc346358768c41fe9dac75f475a1281e |           the light in the dark          |
|   46   | 53461fabeaef483e942c9aaad235ca4d |             life with father             |
|   47   | 4bf0b9efdca047028436d851a7143b05 |       charlie chaplins the knockout      |
|   48   | 435422be103842c982e300a633ac9591 |            made for each other           |

## Resources 
1. [How to build a content-based movie recommender system with Natural Language Processing](https://towardsdatascience.com/how-to-build-from-scratch-a-content-based-movie-recommender-with-natural-language-processing-25ad400eb243)
2. [Build a Movie Recommendation API using Scikit-Learn, Flask and Heroku](https://towardsdatascience.com/build-a-movie-recommendation-api-using-scikit-learn-flask-and-heroku-bee239dc96e3)
3. [Simple Content-based Recommendation Engine API With Flask Heroku Deployed](https://medium.com/@MAbdElRaouf/simple-content-based-recommendation-engine-flask-api-heroku-dd27760dfe8e)
