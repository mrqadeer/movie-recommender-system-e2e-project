import pathlib,yaml,os,pickle
curr_dir=pathlib.Path(__file__)
home_dir=curr_dir.parent.parent.parent
paths_yaml_file=home_dir.as_posix()+'/config.yaml'
paths=yaml.safe_load(open(paths_yaml_file))
# print(paths)
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np
from ast import literal_eval
class MakingDataSet:
    def __init__(self) -> None:
        self.df=None
    def loading_data(self,path):
        return pd.read_csv(path)
    def setting_data(self,df1,df2):
        df=df1.merge(df2,on='title')
        df=df[['movie_id','title','overview','genres','keywords','cast','crew']]
        self.df=df
        return df 
    def cleaning_data(self,df):
        df=df.dropna()
        df=df.drop_duplicates()
        df['genres']=df['genres'].apply(lambda obj: [i['name'] for i in literal_eval(obj)])
        

        df['keywords']=df['keywords'].apply(lambda obj: [i['name'] for i in literal_eval(obj)])
        df['cast']=df['cast'].apply(lambda obj: [i['name'] for i in literal_eval(obj)][:3])
        df['crew']=df['crew'].apply(lambda obj:[i['name'] for i in literal_eval(obj) if i['job']=='Director'])
        df['overview']=df['overview'].str.split()
        
        df['genres']=df['genres'].apply(lambda x:[word.replace(" ",'') for word in x])
        df['keywords']=df['keywords'].apply(lambda x:[word.replace(" ",'') for word in x])
        df['cast']=df['cast'].apply(lambda x:[word.replace(" ",'') for word in x])
        df['crew']=df['crew'].apply(lambda x:[word.replace(" ",'') for word in x])
        df['tags']=df['overview']+df['genres']+df['keywords']+df['cast']+df['crew']
        df['tags']=df['tags'].apply(lambda x:' '.join(x))
        # df['tags']
        return df
        
    
    def save_to_file(self,file,output_path,tag):
        if os.path.exists(output_path):
            print(f"File {output_path} is already saved.")
            # exit()
        if tag=='pd':
            file.to_csv(output_path,index=False)
            print(f"Saved as {output_path}")
        elif tag=='np':
            np.save(output_path,file)
            print(f"Saved as {output_path}")
        elif tag=='pkl':
            pickle.dump(file,open(output_path,'wb'))
            print(f"Saved as {output_path}")
        else:
            print("Invalid tag")
        
if __name__=="__main__":
    mds=MakingDataSet()
    output_path=paths['paths']['cleaned_df_path']
    if os.path.exists(output_path):
        print("No need to clean! Already cleaned.")
    else:
        movies=mds.loading_data(paths['paths']['raw_data_movies'])
        credits=mds.loading_data(paths['paths']['raw_data_credits'])
        df=mds.setting_data(movies,credits)
        cleaned_df=mds.cleaning_data(df)
        mds.save_to_file(cleaned_df,output_path,'pd')
