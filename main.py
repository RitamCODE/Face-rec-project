
from flask import Flask
from app import views

app= Flask(__name__)



#url
app.add_url_rule('/base','base',views.base)
app.add_url_rule('/','index',views.index)
app.add_url_rule('/home/register','register',views.register)
app.add_url_rule('/faceapp','faceapp',views.faceapp)
app.add_url_rule('/addSites','addSites',views.addSites,methods=['GET','POST'])
app.add_url_rule('/faceapp/compare','compare',views.compare)
app.add_url_rule('/faceapp/compare/fetchSite','fetchSite',views.fetchSite,methods=['GET','POST'])




#run


if __name__ == "__main__":
    app.run(debug=True)