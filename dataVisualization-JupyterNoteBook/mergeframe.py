import pandas as pd
from pandas import DataFrame as df

movies_df = pd.read_csv("movies.csv")

# now lets move onto the movie ratings data
ratings_path = './ratings.csv'
ratings_df = pd.read_csv("ratings.csv")

merged_df = pd.merge(ratings_df, movies_df, on='movieId')
print(merged_df.head())
# lets check how many ratings have these movies received, lets take an example of movieId 163949
print("length : ",len(ratings_df[ratings_df['movieId'] == 2794].index))
print("length : ",len(ratings_df.index))
