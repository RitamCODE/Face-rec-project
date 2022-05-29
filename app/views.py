from flask import render_template,request
from flask import redirect,url_for
import os
from PIL import Image
from utils import pipeline_model
from utils2 import pipeline_model2
from utils3 import pipeline_model3
from append_data import appending
from read_data import reading1
from read_data import reading2

UPLOAD_FOLDER = 'static/uploads'

# to render the base tenmplate for the basic structuring of the website
def base():
    return render_template("base.html")

# to render the home page
def index():
    return render_template("index.html")

# to render the registration page
def register():
    val = pipeline_model3()
    return render_template("register.html",value=val)

# to render the faceapp page which authicates us using face recognition
def faceapp():
    return render_template("faceapp.html")

# to render the page which helps us to add data to the database
def addSites():
    if request.method == 'POST':
        faceuserid=request.form["faceuserid"]
        name = request.form["username"]
        password = request.form["password"]
        website=request.form["website"]
        appending(website,name,password,faceuserid)
        print('name={} \n password={} \n website={}'.format(name, password, website))
        return render_template("login.html",n=name,p=password,w=website)
    return render_template("addSites.html")

# to render the face comparison page
def compare():
    img=pipeline_model()
    ret=pipeline_model2()
    return render_template("compare.html",image=img,value=ret)

# to render the page which fetches the stored data for a particular user
def fetchSite():
    if request.method == 'POST':
        faceuserid = request.form["faceuserid"]
        website = request.form["website"]
        userid=reading1(website,faceuserid)
        password= reading2(website, faceuserid)
        return render_template("display_data.html",w=website,fe=faceuserid,u=userid,p=password)
    return render_template("fetchSite.html")
