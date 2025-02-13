import os
import time
import requests
import streamlit as st
from dotenv import load_dotenv

# Load API Key from .env file
load_dotenv()
API_KEY = os.getenv("TMDB_API_KEY")

# Base URLs for TMDB API
SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
RECOMMEND_URL = "https://api.themoviedb.org/3/movie/{}/recommendations"
POSTER_URL = "https://image.tmdb.org/t/p/w500"

# Function to check API Key validity
def is_api_key_valid():
    if not API_KEY or API_KEY.strip() == "":
        st.error("❌ API Key is missing! Please set it in your `.env` file.")
        return False
    return True

# Function to fetch data with retries
def fetch_with_retries(url, params, retries=3, delay=5):
    for attempt in range(retries):
        try:
            response = requests.get(url, params=params, timeout=40)  # Increased timeout
            response.raise_for_status()
            return response.json()  # Return response if successful

        except requests.exceptions.Timeout:
            st.warning(f"⚠️ Attempt {attempt+1}: API request timed out. Retrying...")
        except requests.exceptions.ConnectionError:
            st.warning(f"⚠️ Attempt {attempt+1}: Network issue. Check your connection.")
        except requests.exceptions.HTTPError as e:
            st.error(f"❌ HTTP Error: {e}")
            return None
        except requests.exceptions.RequestException as e:
            st.error(f"❌ Unexpected Error: {e}")
            return None

        time.sleep(delay)  # Wait before retrying

    return None  # Return None if all retries fail

# Function to fetch movie ID
def get_movie_id(movie_name):
    params = {"api_key": API_KEY, "query": movie_name, "language": "en-US"}
    data = fetch_with_retries(SEARCH_URL, params)

    if data and "results" in data and data["results"]:
        return data["results"][0]["id"]
    else:
        st.error("❌ No movie found. Try another name.")
        return None

# Function to fetch recommended movies
def get_recommendations(movie_id):
    url = RECOMMEND_URL.format(movie_id)
    params = {"api_key": API_KEY, "language": "en-US"}
    data = fetch_with_retries(url, params)

    if data:
        return data.get("results", [])[:5]  # Return top 5 recommendations
    else:
        return []

# Function to fetch movie poster
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    params = {"api_key": API_KEY, "language": "en-US"}
    data = fetch_with_retries(url, params)

    if data and "poster_path" in data and data["poster_path"]:
        return POSTER_URL + data["poster_path"]
    return None  # No poster available

# Streamlit UI Layout
st.title("🎬 Movie Recommendation System")

# Validate API Key before proceeding
if not is_api_key_valid():
    st.stop()  # Stop execution if API key is missing

# Input box for movie search
movie_name = st.text_input("Enter a movie name:", "")

# Recommend Button
if st.button("Recommend"):
    if movie_name:
        movie_id = get_movie_id(movie_name)
        
        if movie_id:
            recommendations = get_recommendations(movie_id)
            
            if recommendations:
                st.subheader("✨ Recommended Movies:")
                
                # Display recommended movies with posters
                for movie in recommendations:
                    col1, col2 = st.columns([1, 3])
                    
                    with col1:
                        poster_url = fetch_poster(movie["id"])
                        if poster_url:
                            st.image(poster_url, use_container_width=True)  # ✅ Fixed parameter
                        else:
                            st.write("No poster available")
                    
                    with col2:
                        st.write(f"**{movie['title']}** ({movie['release_date'][:4]})")
                        st.write(f"⭐ Rating: {movie['vote_average']}")
                        st.write(movie["overview"][:200] + "...")  # Short description
                    
                    st.write("---")  # Separator between movies
            else:
                st.warning("❌ No recommendations found.")
