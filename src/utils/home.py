import streamlit as st 
# helper class for main streamlit app
class Home:
    def __init__(self) -> None:
        # reading home.css file
        with open('src/utils/static/home.css','r') as stlye:
            st.markdown(f"<style>{stlye.read()}</style>",unsafe_allow_html=True)
        st.markdown('<link rel="stylesheet" href="src/utils/static/styles.css">', unsafe_allow_html=True)
        # my soical media links
        self.SOCIAL_MEDIA = {
            "LinkedIn": "https://www.linkedin.com/in/mr-qadeer-3499a4205/",
            "GitHub": "https://github.com/mrqadeer",
            "Twitter": "https://twitter.com/mr_sin_of_me",
            "Whatsapp":"https://wa.me/923011231122",
            "Facebook": "https://web.facebook.com/mrqadeerofficial/",
        }
    # method for home page
    def home(self):
        st.markdown('<p class="styled-text">Movie Recommendation System</p>', unsafe_allow_html=True)
        with st.expander("About Project",expanded=True):
            st.markdown('''<p class="about-project"> <span class="movie-text">Movie Recommendation System </span>
                        will recommend best five 5 movies on the base of 1 Movie choosen by user.
                        Dataset I used <a href="https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata">TMDB Movies</a></p>''',unsafe_allow_html=True)
            st.subheader("Configration")
            st.markdown("""In this project we will use TMDB API Key to fetch Movie Poster""")
            st.markdown('Login to <a href="https://www.themoviedb.org/">TMDB</a>',unsafe_allow_html=True)
            st.markdown('Get API Key <a href="https://www.themoviedb.org/settings/api">API KEY</a>',unsafe_allow_html=True)
            
        st.markdown('<p class="name-text">Qadeer Ahmad</p>', unsafe_allow_html=True)
        # about me section
        with st.expander("About Me",expanded=True):
            st.markdown('''<p class="about-me"> I am <span class="my-text"> Data Science,Machine
                        Learning, Deep Learning and Natural Language Processing  </span>enthusiast
                        </p>''',unsafe_allow_html=True)
        # social media section
        st.markdown('<p class="social-text">Social Links</p>', unsafe_allow_html=True)
        
        with st.expander("Catch me on",expanded=True):
            cols = st.columns(len(self.SOCIAL_MEDIA))
            for index, (platform, link) in enumerate(self.SOCIAL_MEDIA.items()):
                cols[index].write(f"[{platform}]({link})")
        st.markdown('''<p class="message"> Keep Learning and Exploring.
                        </p>''',unsafe_allow_html=True)

