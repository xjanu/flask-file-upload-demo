#!/usr/bin/env python3

from flask import Flask, request, render_template
import os

UPLOAD_FOLDER = 'static'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.get('/')
def endpoint_get():
    return render_template('index.html', title="Flask file upload demo")

# file upload endpoint
@app.post('/')
def endpoint_post():

    file = request.files['upload']

    path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(path)

    return render_template('index.html', title="Flask file upload demo", content=f"<a href='{path}'>{file.filename}</a>")
