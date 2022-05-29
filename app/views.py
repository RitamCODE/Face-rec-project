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

def base():
    return render_template("base.html")

def index():
    return render_template("index.html")

def register():
    val = pipeline_model3()
    return render_template("register.html",value=val)

def faceapp():
    return render_template("faceapp.html")

#def getwidth(path):
 #  size=img.size # returns the width and height of the image
  #  aspect = size[0]/size[1] # width/height is the aspect ratio
   # w=300*aspect
    #return int(w)

#def gender():
    #   if request.method == 'POST':
    #   f = request.files["image"]
    #   filename = f.filename
    #   path = os.path.join(UPLOAD_FOLDER,filename)
    #    f.save(path)
    #    w=getwidth(path)
    #       return render_template("gender.html",fileupload=True,img_name=filename,w=w)
#    return render_template("gender.html",fileupload=False,img_name="freeai.png",w=300)

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

def compare():
    img=pipeline_model()
    ret=pipeline_model2()
    return render_template("compare.html",image=img,value=ret)

def fetchSite():
    if request.method == 'POST':
        faceuserid = request.form["faceuserid"]
        website = request.form["website"]
        userid=reading1(website,faceuserid)
        password= reading2(website, faceuserid)
        return render_template("display_data.html",w=website,fe=faceuserid,u=userid,p=password)
    return render_template("fetchSite.html")
