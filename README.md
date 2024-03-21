### Project Structure
- ##### LICENSE
- ##### Makefile
  - Makefile with commands like `make data` or `make train`
- ##### README.md
  - The top-level README for developers using this project
- ##### Data
  - **external**: Data from third party sources.
  - **interim**: Intermediate data that has been transformed
  - **processed**: The final, canonical data sets for modeling
  - **raw**: The original, immutable data dump.
- ##### docs
   - A default Sphinx project; see sphinx-doc.org for details
- ##### models
  - Trained and serialized models, model predictions, or model summaries

- ##### notebooks
  - Jupyter notebooks. Naming convention is a number (for ordering),the creator's initials, and a short `-` delimited description, e.g.`1.0-jqp-initial-data-exploration`.

- ##### references
  - Data dictionaries, manuals, and all other explanatory materials.
- ##### reports
  - Generated analysis as HTML, PDF, LaTeX, etc.
    - figures  Generated graphics and figures to be used in reporting
- ##### requirements.txt 
  -  The requirements file for reproducing the analysis environment, e.g.generated with `pip freeze > requirements.txt`
- ##### setup.py
  - makes project pip installable (pip install -e .) so src can be imported
- ##### src
  - Source code for use in this project.
    - __init__.py   Makes src a Python module
    - **data**
      - Scripts to download or generate data
        └── make_dataset.py
    - **features**
      - Scripts to turn raw data into features for modeling
       └── build_features.py

    - **models**         
      - Scripts to train models and then use trained models to make predictions
        ├── predict_model.py
        └── train_model.py
    - **utils**
      - Scripts for helping streamlit app
        ├── home.py 
        └── prediction.py
      - **static**
        ├── home.css
        ├── prediction.css
        └── main.css
    - **visualization**  
      - Scripts to create exploratory and results oriented visualizations
       └── visualize.py
- ##### tox.ini 
  - tox file with settings for running tox; see tox.readthedocs.io
- ##### config.yaml
    - yaml file containing paths and parameters
- ##### run.yaml
    - yaml file containing files path for executing
- ##### run.py 
    - python file used run.yaml to execute files
### Usage
**Open Terminal or Command Prompt**
```bash
git clone https://github.com/mrqadeer/movie-recommender-system-e2e-project.git
```
Make sure you have ```git``` installed on your machine.
Otherwise download Zip file and extract it.
**Navigate to project directory**
```bash
cd movie-recommender-system-e2e-project
```
**Installation dependencies**
For executing standalone ```streamlit_app.py```
```bash
pip install -r requirements.txt
```
then
```bash
streamlit run streamlit_app.py
```
**OR**
Alternatively, you can run the following command to train and predict models with the Streamlit app:
```bash
python run.py 
```

 **Note**: This process may take some time depending on your machine's configuration. Additionally, it will download and install the necessary `nltk` packages.

This will also downlaod and install ```nltk``` packages

##### Thank you!