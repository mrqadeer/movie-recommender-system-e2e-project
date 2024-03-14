import sys ,os
sys.path.insert(1,'.') # proper importing modlules
# nltk package for stemming like loving to love 
from nltk.stem.porter import PorterStemmer
# custom module
from src.data.make_dataset import MakingDataSet,paths

# class inheritance so that some functionaly can be used
class BuildingFeatures(MakingDataSet):
    def __init__(self) -> None:
        super().__init__()
    def __stem_words(self,text):
        stemmer=PorterStemmer() # stemmer object 
        # returning the text after stemming
        return " ".join([stemmer.stem(word) for word in text.split()])
    # preprocessing data
    def preprocessing_data(self,df):
        # useful features
        new_df=df[['movie_id','title','tags']]
        # basic cleaning
        new_df['tags']=new_df['tags'].str.lower()
        # applying above method
        new_df['tags']=new_df['tags'].apply(self.__stem_words)
        return new_df
        
        
if __name__=="__main__":
    # path for fetching reading cleaned file
    df_path=paths['paths']['cleaned_df_path']
    if os.path.exists(df_path):
        print(f"File {df_path} already processed.")
    else:
        # creating object of class
        building_feature=BuildingFeatures()
        # loading data from inheritance functionality
        df=building_feature.loading_data(df_path)
        # preprocessing data
        df=building_feature.preprocessing_data(df)
        # fetching file path from yaml file for saving processed data as csv
        processed_file_path=paths['paths']['processed_df_path']
        # saving file
        building_feature.save_to_file(df,processed_file_path,'pd')
    
    