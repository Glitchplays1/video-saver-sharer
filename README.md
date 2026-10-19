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
2. Open a terminal in this folder.
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the app:
   ```
   python app.py
   ```
5. Open your browser to: http://localhost:5000

## Notes
- Videos are stored in the `uploads/` folder.
- Titles are saved in small `.title` files next to each video.
- This is a local app — perfect for personal use or sharing on a home network.
- Keep content family-friendly! 🌟

## Files
- `app.py` — The Flask web server
- `templates/` — HTML pages
- `static/css/style.css` — Styles
- `requirements.txt` — Python packages needed
