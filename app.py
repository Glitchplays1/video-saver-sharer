from flask import Flask, request, render_template, send_from_directory, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename
import uuid

app = Flask(__name__)
app.secret_key = 'safe-video-key-2026'
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'mp4', 'webm', 'ogg', 'mov', 'avi'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 200 * 1024 * 1024  # 200 MB max

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    videos = []
    for f in os.listdir(UPLOAD_FOLDER):
        if allowed_file(f):
            title = f.split('_', 1)[1] if '_' in f else f
            title_path = os.path.join(UPLOAD_FOLDER, f + '.title')
            if os.path.exists(title_path):
                with open(title_path) as tf:
                    title = tf.read().strip() or title
            videos.append({'filename': f, 'title': title})
    videos.sort(key=lambda x: x['filename'], reverse=True)
    return render_template('index.html', videos=videos)

@app.route('/upload', methods=['POST'])
def upload():
    if 'video' not in request.files:
        flash('No video file selected!')
        return redirect(url_for('index'))
    file = request.files['video']
    title = request.form.get('title', '').strip() or 'Untitled Video'
    if file.filename == '':
        flash('No file selected!')
        return redirect(url_for('index'))
    if file and allowed_file(file.filename):
        original = secure_filename(file.filename)
        unique_id = str(uuid.uuid4())[:8]
        filename = f"{unique_id}_{original}"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        # Save title in a simple sidecar or just use filename for now
        with open(filepath + '.title', 'w') as tf:
            tf.write(title)
        flash(f'Video "{title}" uploaded successfully!')
    else:
        flash('Invalid file type. Please upload MP4, WebM, OGG, MOV, or AVI.')
    return redirect(url_for('index'))

@app.route('/video/<filename>')
def serve_video(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/share/<filename>')
def share_page(filename):
    title = 'Shared Video'
    title_path = os.path.join(app.config['UPLOAD_FOLDER'], filename + '.title')
    if os.path.exists(title_path):
        with open(title_path) as tf:
            title = tf.read().strip()
    return render_template('share.html', filename=filename, title=title)

@app.route('/delete/<filename>', methods=['POST'])
def delete_video(filename):
    path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(path):
        os.remove(path)
        title_path = path + '.title'
        if os.path.exists(title_path):
            os.remove(title_path)
        flash('Video deleted.')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
