import sys,os
sys.path.insert(1,'.')
from sklearn.feature_extraction.text import CountVectorizer
from src.data.make_dataset import paths 
from src.features.build_features import BuildingFeatures
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

df_path=paths['paths']['processed_df_path']
df_model_path=paths['paths']['model_df_path']
similarity_array_path=paths['paths']['similarity_array_path']

class TrainingModel(BuildingFeatures):
    def __init__(self) -> None:
        super().__init__()
    def vectorization(self,df):
        max_features=paths['params']['max_features']
        cv=CountVectorizer(max_features=max_features,stop_words='english')  
        vectors=cv.fit_transform(df['tags']).toarray()
        vectors=vectors.astype(np.int8)
        return vectors
    def similarity_matrix(self,vectors):
        similarity=cosine_similarity(vectors).astype(np.float32)
        return similarity
if __name__=="__main__":
    
    
    if os.path.exists(df_model_path) and os.path.exists(similarity_array_path):
        print(f"Models already Saved.")
    else:
        tm=TrainingModel()
        df=tm.loading_data(df_path)
        df_dict=df.to_dict()
        vectors=tm.vectorization(df)
        similarity=tm.similarity_matrix(vectors)
        print(similarity.shape)
        
        tm.save_to_file(file=similarity,output_path=similarity_array_path,tag='np')
        tm.save_to_file(file=df_dict,output_path=df_model_path,tag='pkl')