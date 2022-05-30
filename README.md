# Face-rec-project

About this project:

This project uses face recognition to login a user and enable access to the data that he has stored in the website. 
Basically it stores a user's id and password for a particular website and that user will only be granted access to the database if the user is 
verified through face recognition
Anybody who has access to your computer has access to the saved passwords in your google account. This website therfore verifies the user using seamless 
face recognition before getting access to passwords. Therefore there is no need of remembering, this website will remember both the password and you face

NOTE:
All the html files are in the templates folder.
The basic html structure is in 'base.html' which is inherited by all the html files.
The main page is in 'index.html'.
The entire app runs on running the main.py and the views.py in the app folder has all the necessary functions for running the file.

Folder Description:

app - contains important data folder and views.py file

static- contains css files

templates- contains all the html files

  templates file descriptions:
  
      base- contains the basic structure of the website
      
      index- contains the home page
      
      faceapp- contains the face app page
      
      addSites- contains the site addition page
      
      compare- displays the result after face comparison 
      
      fetchSite- requests the server for the required data 
      
      display_data- displays the required data
      
      login- displays the appropriate message after successful storage of data
      
      registration- displays the data after successful registration
      
  
  
Root File descriptions:

Python files:

  main.py- contains the url rules and the main code for running the app

  views.py- connects the html files and python files
  
  append_data.py- helps to add new data
  
  read_data.py- helps to read previously inserted data
  
  utils.py- contains the face detection code
  
  utils2.py- compare the saved image with the captured image in utils.py and provides the data to the htmml pages 
  
  utils3.py- does the initial registration using face recognition

txt files:

  requirements - contains the dependency requirements
  
  faceuserids- contains the unique user for each person entering the website
  
  passwords- contains the saved passowrds of an user
  
  userids- contains the saved userids of an user
  
  websites- contains the saved website of the user
  

