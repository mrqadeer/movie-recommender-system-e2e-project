import yaml
import subprocess # for running file
import logging # for printing
# Configure logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
def run_files_from_yaml(yaml_file):
    run=yaml.safe_load(open(yaml_file)) # reading run.yaml file in files paths are present
    for file_path in run['requirements']:
        subprocess.run(['pip','install','-r',file_path])
    # this is for running training files 
    
    # Log a message indicating the start of the installation process
    logging.info("Installing dependencies from requirements.txt...")
    import nltk
    nltk.download('punkt')  # Download the punkt tokenizer
    nltk.download('wordnet')  # Download the WordNet lemmatizer
    nltk.download('stopwords')  # Download the stopwords corpus
    # for training and cleaing files
    for file_path in run['files_to_run']:
        subprocess.run(['python', file_path])
        logging.info(f"Running {file_path}")
    # for running main streamlit app
    for file_path in run['streamlit_app']:
        subprocess.run(['python','-m','streamlit','run',file_path])
        logging.info(f"Running {file_path}")

if __name__ == "__main__":
    run_files_from_yaml('run.yaml')
    
