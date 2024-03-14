import streamlit as st
from streamlit_option_menu import option_menu
# for proper importing
import sys 
sys.path.insert(1,'.')
# custom modules
from src.utils.home import Home
from src.utils.prediction import ModelPredictions

st.set_page_config("Movie Recommendation System",page_icon='🎥')

#main class
class App:
    def __init__(self) -> None:
        
        with open('src/utils/static/main.css','r') as stlye:
            st.markdown(f"<style>{stlye.read()}</style>",unsafe_allow_html=True)
        st.markdown('<link rel="stylesheet" href="src/utils/static/styles.css">', unsafe_allow_html=True)
    
    def run(self):
        with st.sidebar:
            app=option_menu(
                menu_title='Introduction',
                options=['Home','Prediction'],
                icons=['house-heart','command'],
                menu_icon='info',
                default_index=0,
                styles={
                    "container": {"padding": "15!important", "background-color": '#06040a'},
                    "icon": {"color": "white ", "font-size": "20px"},
                    "nav-link": {"color": "white", "font-size": "20px",'font-weight':'bold', 
                                 "text-align": "left", "margin": "0px",
                                 "--hover-color": "magenta"},
                    "nav-link-selected": {"background-color": "#02ab21"}
                }
            )
        if app=='Home':
            home=Home()
            home.home()
        if app=='Prediction':
            prediction=ModelPredictions()
            prediction.prediction()
            

            
if __name__=='__main__':
    app=App()
    app.run()