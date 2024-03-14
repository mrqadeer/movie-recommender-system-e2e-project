import sys ,os
sys.path.insert(1,'.')
from src.data.make_dataset import MakingDataSet,paths
from nltk.stem.porter import PorterStemmer
import nltk
nltk.download('punkt')  # Download the punkt tokenizer
nltk.download('wordnet')  # Download the WordNet lemmatizer
nltk.download('stopwords')  # Download the stopwords corpus
class BuildingFeatures(MakingDataSet):
    def __init__(self) -> None:
        super().__init__()
    def __stem_words(self,text):
        stemmer=PorterStemmer()
        return " ".join([stemmer.stem(word) for word in text.split()])
    def preprocessing_data(self,df):
        new_df=df[['movie_id','title','tags']]
        
        new_df['tags']=new_df['tags'].str.lower()
        new_df['tags']=new_df['tags'].apply(self.__stem_words)
        return new_df
        
        
if __name__=="__main__":
    df_path=paths['paths']['cleaned_df_path']
    if os.path.exists(df_path):
        print(f"File {df_path} already processed.")
    else:
        bf=BuildingFeatures()
        df=bf.loading_data(df_path)

        # print(df.isnull().sum())
        df=bf.preprocessing_data(df)
        processed_file_path=paths['paths']['processed_df_path']
        bf.save_to_file(df,processed_file_path,'pd')
    
    