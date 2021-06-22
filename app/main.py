from flask import Flask,render_template,request,redirect, url_for,flash
from app.utils.db import create_project,get_projects
from app.utils.file import allowed_file,UPLOAD_FOLDER
from werkzeug.utils import secure_filename



import cloudinary.uploader

cloudinary.config(
    cloud_name = 'do3lstjln',  
    api_key = '824753697255582',  
    api_secret = 'HgPg6sFKi9-hLGLevHmw_Y3JN_o'  
    )


app = Flask(__name__)

db=None



@app.route('/')
def index():
        return render_template('/pages/index.html',page='home')

@app.route('/about')
def about():
        return render_template('/pages/about.html',page='about')

@app.route('/projects')
def projects():
        projects = get_projects()
        return render_template('/pages/projects.html',projects=projects)

@app.route('/backoffice')
def back_office():
        return render_template('/pages/backoffice.html',page='backoffice')

@app.post('/projects')
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']   
        if file.filename == '':
            return redirect(url_for('back_office'))
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            cloudinary_response=cloudinary.uploader.upload(file, public_id = filename)
            title=request.form.get('title')
            description=request.form.get('description')
            url=request.form.get('url')
            cover=cloudinary_response.get('url')
            db_response = create_project(title, description, url,cover)
            return  redirect("/projects")




