# My Video Saver & Sharer

A simple, family-friendly website to upload, save, and share your videos!

## Features
- Upload videos (MP4, WebM, OGG, MOV, AVI up to 200MB)
- View all your saved videos in a gallery
- Play videos directly in the browser
- Share individual videos via unique links
- Delete videos you no longer need
- Beautiful, colorful, kid-friendly design

## Deploy on Railway (Recommended)

1. Go to [Railway](https://railway.app) and sign in (GitHub login is easiest).
2. Click **New Project** → **Deploy from GitHub repo**.
3. Select this repository: `Glitchplays1/video-saver-sharer`.
4. Railway will automatically detect the Python app and the `Procfile`.
5. Click **Deploy**. After a minute or two it will give you a public URL (like `something.up.railway.app`).
6. Open that URL — your video saver is live!

### Important note about storage
On Railway’s free/hobby plan the filesystem is **temporary**. Uploaded videos will disappear when the app restarts or redeploys. For permanent storage you would need to connect a volume or use cloud storage (S3, etc.). For personal/testing use it works fine.

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

GitHub Pages only hosts static files. The real app needs Railway (or similar). A landing page is available if you enable Pages.

## Notes
- Videos are stored in the `uploads/` folder.
- Keep content family-friendly! 🌟

## Files
- `app.py` — The Flask web server
- `Procfile` — Tells Railway how to start the app
- `templates/` — HTML pages
- `static/css/style.css` — Styles
- `requirements.txt` — Python packages needed
