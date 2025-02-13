# 🎬 Movie Recommendation System

## 📌 Overview
The **Movie Recommendation System** is a **content-based** recommendation engine that suggests similar movies based on user input. It utilizes **The Movie Database (TMDb) API** to fetch movie details and posters. The system is built with **Python** and **Streamlit**, providing an interactive UI for users.

## 🚀 Features
- 🔍 **Search for a Movie**: Enter a movie name to get recommendations.
- 🎥 **Top 5 Movie Recommendations**: Get a list of similar movies with posters.
- 🖼️ **Movie Posters & Details**: View posters, ratings, and brief descriptions.
- 🔄 **Error Handling & Retry Mechanism**: Handles API failures with retries.
- 📦 **.env File Support**: Stores API keys securely.

## 🛠️ Technologies Used
- **Python** 🐍
- **Streamlit** 🎛️ (for UI)
- **Requests** 📡 (to fetch data from TMDb API)
- **dotenv** 🔑 (for API key security)
- **Git & GitHub** 🖥️ (for version control)

## 📥 Installation & Setup
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-username/Movie-Recommendation-System.git
cd Movie-Recommendation-System
```
### 2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```
### 3️⃣ Set Up the API Key
1. **Create a `.env` file** in the project directory.
2. **Add your TMDb API Key** inside the `.env` file:
```sh
TMDB_API_KEY=your_api_key_here
```
3. **Save the file**.

### 4️⃣ Run the Application
```sh
streamlit run app.py
```

## 🎯 Usage
1. Enter a movie name in the search bar.
2. Click the **"Recommend"** button.
3. View the top 5 recommended movies with posters & ratings.

## 🛑 Error Handling & Troubleshooting
- **API Timeout?** 🕒 → Retry mechanism is implemented (wait a few seconds).
- **Incorrect Movie Name?** 🔍 → Try different spellings or a more popular title.
- **No Recommendations Found?** ❌ → Some movies may not have recommendations in TMDb.

## 📜 License
This project is open-source under the **MIT License**.

## 🙌 Acknowledgments
- **TMDb API** for movie data.
- **Streamlit** for a simple UI.
- **Python Community** for libraries & support.

---

⭐ **If you like this project, don't forget to star the repository!** ⭐

