from flask import render_template, flash, redirect
from app import app
# from bd import bd
import requests
from bd import urlth1, urlth2, urlth3, urlth4, urlhum1, urlhum2, urlhum3, urlhum4, urlhum5, urlhum6
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
    a1 = requests.get(urlth1).json()
    a2 = requests.get(urlth2).json()
    a3 = requests.get(urlth3).json()
    a4 = requests.get(urlth4).json()
    b1 = requests.get(urlhum1).json()
    b2= requests.get(urlhum2).json()
    b3= requests.get(urlhum3).json()
    b4 = requests.get(urlhum4).json()
    b5 = requests.get(urlhum5).json()
    b6 = requests.get(urlhum6).json()
    
    global temp_1 
    global hum_1
    s1 = ''
    for k in a1.values():
        s1 += str(k)
    temp_1 = s1[1:2:]
    hum_1 = s1[2::]
    
    global temp_2
    global hum_2
    s1 = ''
    for k in a2.values():
        s1 += str(k)
    temp_2 = s1[1:2:]
    hum_2 = s1[2::]
    
    global temp_3
    global hum_3
    s1 = ''
    for k in a3.values():
        s1 += str(k)
    temp_3 = s1[1:2:]
    hum_3 = s1[2::]
    
    global temp_4
    global hum_4
    s1 = ''
    for k in a4.values():
        s1 += str(k)
    temp_4 = s1[1:2:]
    hum_4 = s1[2::]
    
    global hum_earth_1
    s1 = ''
    for k in b1.values():
        s1 += str(k)
    hum_earth_1 = s1[2::]

    global hum_earth_2
    s1 = ''
    for k in b2.values():
        s1 += str(k)
    hum_earth_2 = s1[2::] 

    global hum_earth_3
    s1 = ''
    for k in b3.values():
        s1 += str(k)
    hum_earth_3 = s1[2::]

    global hum_earth_4
    s1 = ''
    for k in b4.values():
        s1 += str(k)
    hum_earth_4 = s1[2::]

    global hum_earth_5
    s1 = ''
    for k in b5.values():
        s1 += str(k)
    hum_earth_5 = s1[2::]

    global hum_earth_6
    s1 = ''
    for k in b6.values():
        s1 += str(k)
    hum_earth_6 = s1[2::]
    return render_template('table.html',
        title = 'table')


@app.route('/about_us')
def about_us():
    return render_template('about_us.html',
        title = 'about_us')

@app.route('/getDataTempGraph')
def gettemp():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9]

# @app.route('/getDataHumGraph')
# def gethum():
#     return [9, 8, 7, 8, 5, 4, 3, 7, 4]

# @app.route('/bd')
# def getbd():
#     bd()

