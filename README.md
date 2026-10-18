# PyQfy - Smart PYQ & Academic Intelligence Hub 🎓

An advanced academic AI assistant tool built with Streamlit and Gemini AI.

## Features
- Deep, structured model answers for uploaded PDF or TXT question papers.
- Glassmorphic dark theme UI.
- Interactive AI study assistant chat.
- Downloadable PDF report generation.

## Deployment Instructions

### 1. Push to GitHub
1. Create a new GitHub repository named `PyQfy`.
2. Upload all files from this folder (`app.py`, `requirements.txt`, `.streamlit/`, `README.md`) to your repository.

### 2. Deploy on Streamlit Community Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io/) and log in with your GitHub account.
2. Click **New app**.
3. Select your repository `PyQfy`, branch `main`, and main file path `app.py`.
4. Open **Advanced settings...** and add your Gemini API key in **Secrets**:
   ```toml
   GEMINI_API_KEY = "your-actual-gemini-api-key"
   ```
5. Click **Deploy!**
