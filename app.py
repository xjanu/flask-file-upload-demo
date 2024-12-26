#!/usr/bin/env python3

from flask import Flask, request, render_template
import os

UPLOAD_FOLDER = 'static'
APP_TITLE = "Flask file upload demo"

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=["GET", "POST"])
def endpoint_post():

    # Save the uploaded file (POST)
    uploaded = None
    if request.files:
        file = request.files['upload']
        path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(path)
        uploaded = file.filename

    # List all uploaded files
    all_files = os.listdir(UPLOAD_FOLDER)
    all_files.sort()
    print(all_files)

    return render_template(
        'index.html',
        title=APP_TITLE,
        uploaded=uploaded,
        all_files=all_files
    )
