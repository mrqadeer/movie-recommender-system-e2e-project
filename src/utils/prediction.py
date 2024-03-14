import streamlit as st 
import pandas as pd 
import numpy as np
# for proper importing custom modules
import sys,pickle
sys.path.insert(1,'.')
# importing custom modules
from src.models.predict_model import  df_model_path,similarity_array_path
from src.utils.tmdb_api import get_movie_detail
# helper class for main streamlit app
class ModelPredictions:
    def __init__(self) -> None:
        # reading css file for styling
        with open('src/utils/static/prediction.css','r') as stlye:
            st.markdown(f"<style>{stlye.read()}</style>",unsafe_allow_html=True)
        st.markdown('<link rel="stylesheet" href="src/utils/static/styles.css">', unsafe_allow_html=True)
        # loding models pkl and npy for further working
        model_pkl=pickle.load(open(df_model_path,'rb'))
        self.df=pd.DataFrame(model_pkl)
        self.similarity=np.load(similarity_array_path)
        
    # method to return recommended movies and their poster
    def recommend(self,movie,key):
        # getting indexes of movies
        movie_index=self.df[self.df['title']==movie].index[0]
        # calculating distances vectors of movies
        distances=self.similarity[movie_index]
        # sorting movies on similarity vector values
        movies=sorted(list(enumerate(distances)),key=lambda x:x[1],reverse=True)[1:6]
        # empty lists
        movies_list=[]
        movies_posters=[]
        # iterating over 5 movies
        for i in movies:
            movie_id=self.df.iloc[i[0]].movie_id
            # name of movies
            movies_list.append(self.df.iloc[i[0]].title)
            # images links of desired movies
            movies_posters.append(get_movie_detail(movie_id,key))
        return movies_list,movies_posters

    def prediction(self):
        
        if 'key' not in st.session_state:
                st.session_state.key=""

        # header
        st.markdown('<p class="movie-text">Movie Recommendation System</p>', unsafe_allow_html=True)
        with st.expander("Configuration",expanded=True):
            
            st.subheader("TMDB API Key")
            st.markdown("""In this project we will use TMDB API Key to fetch Movie Poster""")
            # taking name and key from user
            name=st.text_input("Enter your Name",placeholder='Qadeer').title()
            key=st.text_input("Enter Key: ",type='password',placeholder='API Key')
            # checking if key is empty or not
            if len(key)==0:
                st.warning(f"Dear {name} please Enter TMDB API Key")
                st.stop()
            st.session_state.key=key
            st.info(f"Welcome dear {name}")
        # getting all the movies in list
        movies=self.df['title'].values
        # drop down menu for chosing a movie
        selected_movie=st.selectbox("Select a Movie",movies)
        recomend_btn=st.button("Recommend")
        if recomend_btn:
            # taking movies list and poster list
            movies_rec,movies_posters=self.recommend(selected_movie,st.session_state.key)
            # making columns as length of movies i.e 5
            cols=st.columns(len(movies_rec))
            # displaying movies name and poster
            for count,(name,poster_path) in enumerate(zip(movies_rec,movies_posters)):
                cols[count].image(poster_path)
                cols[count].markdown(name)
        
