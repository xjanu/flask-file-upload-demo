#!/usr/bin/env python3

from flask import Flask, request, render_template
import os

UPLOAD_FOLDER = 'static/upload/'
APP_TITLE = "Flask file upload demo"

if not os.path.exists(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def endpoint_post():

    # Save the uploaded file (POST)
    uploaded = None
    if request.files:
        file = request.files['upload']
        path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(path)
        uploaded = {
            'name': file.filename,
            'href': path}

    # List all uploaded files
    all_files = []
    for file in sorted(os.listdir(UPLOAD_FOLDER)):
        all_files.append({
            "name": file,
            "href": os.path.join(UPLOAD_FOLDER, file)
        })

    return render_template(
        'index.html',
        title=APP_TITLE,
        uploaded=uploaded,
        all_files=all_files
    )
