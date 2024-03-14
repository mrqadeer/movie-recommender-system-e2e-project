import numpy as np
import sys,os
sys.path.insert(1,'.') # for proper importing modules
# vectorization using skearn
from sklearn.feature_extraction.text import CountVectorizer
# for similarity vectors
from sklearn.metrics.pairwise import cosine_similarity
# custom modules
from src.data.make_dataset import paths # use previous file paths variable
from src.features.build_features import BuildingFeatures
# fetching paths from yaml file 
df_path=paths['paths']['processed_df_path']
df_model_path=paths['paths']['model_df_path']
similarity_array_path=paths['paths']['similarity_array_path']

class TrainingModel(BuildingFeatures):
    def __init__(self) -> None:
        super().__init__() # for accessing parent class attributes and methods
    def vectorization(self,df):
        # max feature from config.yaml file
        max_features=paths['params']['max_features'] 
        # creating vector object with max features
        cv=CountVectorizer(max_features=max_features,stop_words='english')  
        # applying vectorization
        vectors=cv.fit_transform(df['tags']).toarray()
        # changing data types so that it take low space
        vectors=vectors.astype(np.int8)
        return vectors
    # method to do similarity of vector
    def similarity_matrix(self,vectors):
        similarity=cosine_similarity(vectors).astype(np.float32)
        return similarity
if __name__=="__main__":
    
    # it checks that if model.pkl or similarity.npy files are present or not 
    if os.path.exists(df_model_path) and os.path.exists(similarity_array_path):
        print(f"Models already Saved.")
    else:
        # class object
        training_model=TrainingModel()
        # loading data from grand parant class method
        df=training_model.loading_data(df_path)
        # converting to dictionary for pickling
        df_dict=df.to_dict()
        # vectorization of data
        vectors=training_model.vectorization(df)
        # similarity matrix of vectors
        similarity=training_model.similarity_matrix(vectors)
        # saving files
        training_model.save_to_file(file=similarity,output_path=similarity_array_path,tag='np')
        training_model.save_to_file(file=df_dict,output_path=df_model_path,tag='pkl')