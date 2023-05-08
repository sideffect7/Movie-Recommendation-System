import streamlit as st
import pickle
import pandas as pd
import requests

def poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=7fff567609c9f52a68f9f44e655b8606&language=en-US'.format(movie_id))
    data = response.json()
    return  "https://image.tmdb.org/t/p/w500" + data['poster_path']

def recommend_movies(movie):
    index=recommended_movies[recommended_movies['title']==movie].index[0]
    distances=dist[index]
    recommended_movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    
    recommended=[]
    recommended_poster=[]
    for i in recommended_movies_list:
        movie_id=recommended_movies.iloc[i[0]].movie_id
        recommended.append(recommended_movies.iloc[i[0]].title)
        recommended_poster.append(poster(movie_id))
    return recommended,recommended_poster

recommended_movies_dict=pickle.load(open('movies_dict.pkl','rb'))
recommended_movies=pd.DataFrame(recommended_movies_dict)

dist=pickle.load(open('dist.pkl','rb'))

st.title("Movie Reccomneder")

movie_selected=st.selectbox(
    ' ',
    recommended_movies['title'].values
)

if st.button("Movies Recommended for you"):
    recommended_movie_names,recommended_movie_posters = recommend_movies(movie_selected);
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])