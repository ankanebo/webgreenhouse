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
    b2 = requests.get(urlhum2).json()
    b3 = requests.get(urlhum3).json()
    b4 = requests.get(urlhum4).json()
    b5 = requests.get(urlhum5).json()
    b6 = requests.get(urlhum6).json()
    
    s1 = []
    for k in a1.values():
        s1.append(str(k))
    

    s2 = []
    for k in a2.values():
        s2.append(str(k))
    
    s3 = []
    for k in a3.values():
        s3.append(str(k))
    
    s4 = []
    for k in a4.values():
        s4.append(str(k))
    
    s5 = []
    for k in b1.values():
        s5.append(str(k))

    s6 = []
    for k in b2.values():
        s6.append(str(k))

    s7 = []
    for k in b3.values():
        s7.append(str(k))

    s8 = []
    for k in b4.values():
        s8.append(str(k))

    s9 = []
    for k in b5.values():
        s9.append(str(k))

    s10 = []
    for k in b6.values():
        s10.append(str(k))
        
    return render_template('table.html',
        title = 'table',
        temp_1 = s1[1],
        hum_1 = s1[2],
        temp_2 = s2[1],
        hum_2 = s2[2],
        temp_3 = s3[1],
        hum_3 = s3[2],
        temp_4 = s4[1],
        hum_4 = s4[2],
        hum_earth_1 = s5[1],
        hum_earth_2 = s6[1],
        hum_earth_3 = s7[1],
        hum_earth_4 = s8[1],
        hum_earth_5 = s9[1],
        hum_earth_6 = s10[1])




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
@app.route('/index/temp_1')
def sensor_1():    
    return render_template('index.html')

@app.route('/index/temp_2')
def sensor_2():    
    return render_template('index.html')

@app.route('/index/temp_3')
def sensor_3():    
    return render_template('index.html')

@app.route('/index/temp_4')
def sensor_4():    
    return render_template('index.html')

@app.route('/index/humearth_1')
def sensor_5():    
    return render_template('index.html')

@app.route('/index/humearth_2')
def sensor_6():    
    return render_template('index.html')

@app.route('/index/humearth_3')
def sensor_7():    
    return render_template('index.html')

@app.route('/index/humearth_4')
def sensor_8():    
    return render_template('index.html')

@app.route('/index/humearth_5')
def sensor_9():    
    return render_template('index.html')

@app.route('/index/humearth_6')
def sensor_10():    
    return render_template('index.html')



