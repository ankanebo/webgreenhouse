from flask import render_template, flash, redirect
from app import app
from bd import bd
#from templates.getpost import getpost


@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Miguel' } # выдуманный пользователь
    return render_template("index.html",
        title = 'Home',
        user = user)

#def get_db_connection():
 #   conn = sqlite3.connect('greenhouse.db')
  #  conn.row_factory = sqlite3.Row
   # return conn

@app.route('/table')
def table():
    #conn = get_db_connection()
    #posts = conn.execute('SELECT * FROM posts').fetchall()
    #conn.close()
    return render_template('table.html',
        title = 'table')


@app.route('/about_us')
def about_us():
    return render_template('about_us.html',
        title = 'about_us')

@app.route('/getDataTempGraph')
def gettemp():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9]

@app.route('/getDataHumGraph')
def gethum():
    return [9, 8, 7, 8, 5, 4, 3, 7, 4]

@app.route('/bd')
def getbd():
    bd()

