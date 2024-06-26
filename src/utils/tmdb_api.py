import streamlit as st
import requests # for api hitting


def get_movie_detail(movie_id,key):
    # fething api for poster image path
    try:
        url=f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={key}"
        
        response=requests.get(url)
        response.raise_for_status()
        result=response.json()
        # final path
        path='https://image.tmdb.org/t/p/w185'+result['poster_path']
    except KeyError as e:
        st.error("Could not fetch image.")
        st.stop()
    except requests.ConnectionError as e:
        st.write(f"Connection Error {e}")
        st.stop()
    except requests.HTTPError as e:
        st.error(f"HTTP Error {e}")
        st.stop()
    except requests.TooManyRedirects as e:
        st.error(f"Too Many API hits {e}")
        st.stop()
    except requests.RequestException as e:
        st.error(f"Request Error {e}")
        st.stop()
    except Exception as e:
        st.error(f"Error {e}")
        st.stop()
    else:
        return path

