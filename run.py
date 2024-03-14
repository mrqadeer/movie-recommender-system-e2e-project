import yaml
import subprocess
import logging
# Configure logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
def run_files_from_yaml(yaml_file):
    run=yaml.safe_load(open(yaml_file))
    for file_path in run['requirements']:
        subprocess.run(['pip','install','-r',file_path])
    # Log a message indicating the start of the installation process
    logging.info("Installing dependencies from requirements.txt...")
    
    for file_path in run['files_to_run']:
        subprocess.run(['python', file_path])
        logging.info(f"Running {file_path}")
    
    for file_path in run['streamlit_app']:
        subprocess.run(['python','-m','streamlit','run',file_path])
        logging.info(f"Running {file_path}")

if __name__ == "__main__":
    run_files_from_yaml('run.yaml')

