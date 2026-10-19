# My Video Saver & Sharer

A simple, family-friendly website to upload, save, and share your videos!

## Features
- Upload videos (MP4, WebM, OGG, MOV, AVI up to 200MB)
- View all your saved videos in a gallery
- Play videos directly in the browser
- Share individual videos via unique links
- Delete videos you no longer need
- Beautiful, colorful, kid-friendly design

## How to Run Locally

1. Make sure you have Python 3 installed.
2. Clone the repo:
   ```bash
   git clone https://github.com/Glitchplays1/video-saver-sharer.git
   cd video-saver-sharer
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the app:
   ```bash
   python app.py
   ```
5. Open your browser to: http://localhost:5000

## GitHub Pages

GitHub Pages only hosts **static** files. This is a dynamic Flask app that needs a Python server, so visiting the GitHub Pages URL will only show a landing page with instructions (once Pages is enabled).

To enable the landing page:
1. Go to the repo **Settings** → **Pages**
2. Under **Source**, select **Deploy from a branch**
3. Choose **main** branch and **/ (root)** folder
4. Save — it will be available at `https://glitchplays1.github.io/video-saver-sharer/` after a minute or two

## Free Hosting Options (for the real app)

To run the full app online you need a service that supports Python:
- [Render](https://render.com) (free tier available)
- [Railway](https://railway.app)
- [PythonAnywhere](https://www.pythonanywhere.com)
- [Replit](https://replit.com)

## Notes
- Videos are stored in the `uploads/` folder (local only).
- Titles are saved in small `.title` files next to each video.
- Keep content family-friendly! 🌟

## Files
- `app.py` — The Flask web server
- `templates/` — HTML pages
- `static/css/style.css` — Styles
- `index.html` — GitHub Pages landing page
- `requirements.txt` — Python packages needed
