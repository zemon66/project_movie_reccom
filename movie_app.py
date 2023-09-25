import streamlit as st
import pandas as pd
import pickle

movies_df = pd.read_pickle('movies.pkl')
similarity = pd.read_pickle('similarity.pkl')


def recommend(movie):
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_indices = sorted(range(len(distance)), key=lambda i: distance[i], reverse=True)[1:6]

    recommended_movies = []

    for i in movie_indices:
        recommended_movies.append(movies_df.iloc[i].title)

    return recommended_movies


st.title('MOVIE RECOMMENDER')

selected_movie = st.selectbox(
    'SEARCH A MOVIE',
    movies_df['title']
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie)
    st.write("Recommended Movies:")
    for movie in recommendations:
        st.write(movie)
