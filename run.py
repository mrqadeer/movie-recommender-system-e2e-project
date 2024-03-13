import yaml
import subprocess

def run_files_from_yaml(yaml_file):
    run=yaml.safe_load(open(yaml_file))

    for file_path in run['files_to_run']:
        subprocess.run(['python', file_path])
if __name__ == "__main__":
    run_files_from_yaml('run.yaml')

