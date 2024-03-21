import pathlib,yaml,os,pickle

curr_dir=pathlib.Path(__file__) # give current path of current file
home_dir=curr_dir.parent.parent.parent # 3 step back to project folder
paths_yaml_file=home_dir.as_posix()+'/config.yaml' # yaml file path
paths=yaml.safe_load(open(paths_yaml_file)) # opening yaml file

import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np

from ast import literal_eval # for fetching proper python object 

class MakingDataSet:
    def __init__(self) -> None:
        pass
        
    def loading_data(self,path):
        return pd.read_csv(path)
    
    def setting_data(self,df1,df2):
        # combining two datasets for working
        df=df1.merge(df2,on='title')
        df=df[['movie_id','title','overview','genres','keywords','cast','crew']]
        return df 
    
    def cleaning_data(self,df):
        # basic cleaning
        df=df.dropna()
        df=df.drop_duplicates()
        # fetching list of genres like Drama,Action etc
        df['genres']=df['genres'].apply(lambda obj: [i['name'] for i in literal_eval(obj)])
        
        # making list of keywords 
        df['keywords']=df['keywords'].apply(lambda obj: [i['name'] for i in literal_eval(obj)])
        # top 3 cast of movie
        df['cast']=df['cast'].apply(lambda obj: [i['name'] for i in literal_eval(obj)][:3])
        # only fetching director
        df['crew']=df['crew'].apply(lambda obj:[i['name'] for i in literal_eval(obj) if i['job']=='Director'])
        # making list of overview
        df['overview']=df['overview'].str.split()
        # removing space from words like hello world --> helloworld 
        df['genres']=df['genres'].apply(lambda x:[word.replace(" ",'') for word in x])
        df['keywords']=df['keywords'].apply(lambda x:[word.replace(" ",'') for word in x])
        df['cast']=df['cast'].apply(lambda x:[word.replace(" ",'') for word in x])
        df['crew']=df['crew'].apply(lambda x:[word.replace(" ",'') for word in x])
        
        
        # making new column 
        df['tags']=df['overview']+df['genres']+df['keywords']+df['cast']+df['crew']
        # making text from list
        df['tags']=df['tags'].apply(lambda x:' '.join(x))
        
        return df
        
    # General method to save 3 type of file
    def save_to_file(self,file,output_path,tag):
        # checking if file already in project folder or not (help if file runs twice)
        if os.path.exists(output_path):
            print(f"File {output_path} is already saved.")
        # saving csv file
        if tag=='pd':
            file.to_csv(output_path,index=False)
            print(f"Saved as {output_path}")
        # saving npy array
        elif tag=='np':
            np.save(output_path,file)
            print(f"Saved as {output_path}")
        # saving as pkl object
        elif tag=='pkl':
            pickle.dump(file,open(output_path,'wb'))
            print(f"Saved as {output_path}")
        else:
            print("Invalid tag")
        
if __name__=="__main__":
    make_dataset=MakingDataSet() # object of class
    # path from config.yaml file for saving file as csv
    output_path=paths['paths']['cleaned_df_path']
    if os.path.exists(output_path):
        print("No need to clean! Already cleaned.")
    else:
        movies_path=paths['paths']['raw_data_movies']
        credits_path=paths['paths']['raw_data_credits']
        # reading file paths
        try:
            movies=make_dataset.loading_data(movies_path)
            credits=make_dataset.loading_data(credits_path)
        except FileNotFoundError as e:
            print(f"Make sure you have files {movies_path} and {credits_path} in data/raw folder")
        else:
            # taking dataframe
            df=make_dataset.setting_data(movies,credits)
            # cleaning data
            cleaned_df=make_dataset.cleaning_data(df)
            # saving file
            make_dataset.save_to_file(cleaned_df,output_path,'pd')
