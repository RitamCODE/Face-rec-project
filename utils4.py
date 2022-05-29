# creating the database

import sqlite3
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
db = sqlite3.connect("user_password.db")
cursor=db.cursor()
cursor.execute("CREATE TABLE UID(WEBSITE VARCHAR(250) PRIMARY KEY,USERID VARCHAR(250),PASSWORD VARCHAR(250))")
cursor.execute("INSERT INTO UID VALUES('abc.com', 'Ritam Mukherjee', 'ritam122388930' )")
db.commit()