import sys,pickle
sys.path.insert(1,'.')
import numpy as np 
import pandas as pd 

from src.models.train_model import df_model_path,similarity_array_path

class Predictions:
    def __init__(self) -> None:
        pass
    def recommend(self,movie,df,similarity_array):
        movie_index=df[df['title']==movie].index[0]
        distances=similarity_array[movie_index]
        movies=sorted(list(enumerate(distances)),key=lambda x:x[1],reverse=True)[1:6]
        for i in movies:
            print(df.iloc[i[0]].title)
if __name__=="__main__":
    df_dict=pickle.load(open(df_model_path,'rb'))
    df=pd.DataFrame(df_dict)
    similarity_array=np.load(similarity_array_path)
    predictions=Predictions()
    predictions.recommend('Avatar',df,similarity_array)
    