import streamlit as st 
import pandas as pd 
import numpy as np

import sys,pickle
sys.path.insert(1,'.')

from src.models.predict_model import  df_model_path,similarity_array_path
from src.utils.tmdb_api import get_movie_detail

class ModelPredictions:
    def __init__(self) -> None:
        with open('src/utils/static/styles.css','r') as stlye:
            st.markdown(f"<style>{stlye.read()}</style>",unsafe_allow_html=True)
        st.markdown('<link rel="stylesheet" href="src/utils/static/styles.css">', unsafe_allow_html=True)
        model_pkl=pickle.load(open(df_model_path,'rb'))
        self.df=pd.DataFrame(model_pkl)
        self.similarity=np.load(similarity_array_path)
    def recommend(self,movie):
        movie_index=self.df[self.df['title']==movie].index[0]
        distances=self.similarity[movie_index]
        movies=sorted(list(enumerate(distances)),key=lambda x:x[1],reverse=True)[1:6]
        movies_list=[]
        movies_posters=[]
        for i in movies:
            movie_id=self.df.iloc[i[0]].movie_id
            movies_list.append(self.df.iloc[i[0]].title)
            movies_posters.append(get_movie_detail(movie_id))
        return movies_list,movies_posters
    def get_movies_list(self):
        movies=self.df['title'].values
        return movies
    def prediction(self):
        movies=self.get_movies_list()
        m=st.selectbox("Select a Movie",movies)
        recomend_btn=st.button("Recommend")
        if recomend_btn:
            
            movies_rec,movies_posters=self.recommend(movie=m)
            cols=st.columns(len(movies_rec))
            for count,(name,poster_path) in enumerate(zip(movies_rec,movies_posters)):
                
                cols[count].image(poster_path)
                cols[count].markdown(name)

