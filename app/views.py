from flask import render_template, flash, redirect
from app import app
# from bd import bd
import requests
from bd import urlth1, urlth2, urlth3, urlth4, urlhum1, urlhum2, urlhum3, urlhum4, urlhum5, urlhum6
import sqlite3
#from templates.getpost import getpost


@app.route('/')
@app.route('/index/index')
def index():
    return render_template("index.html",
        title = 'Home')

#def get_db_connection():
 #   conn = sqlite3.connect('greenhouse.db')
  #  conn.row_factory = sqlite3.Row
   # return conn

@app.route('/index/table')
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
    
    conn = sqlite3.connect("greenhouse.db")
    zpr0 = "temp_value_1, temp_value_2, temp_value_3, temp_value_4"
    sqlread1 = f"""\
    SELECT {zpr0} FROM data
    LEFT JOIN sens_hum_temp_value ON sens_hum_temp_value.ID = data.ID
    LEFT JOIN hum_earth ON hum_earth.ID = data.ID
    ORDER BY data.ID DESC LIMIT 1
    """
    
    lxlx = list(conn.execute(sqlread1))
    k = [list(f) for f in lxlx] 
    j = []
    for i in range(len(k)):
        for p in range(len(k[i])):
            j.append(int(k[i][p]))


    zpr1 = "hum_value_1, hum_value_2, hum_value_3, hum_value_4"
    sqlread1 = f"""\
    SELECT {zpr1} FROM data
    LEFT JOIN sens_hum_temp_value ON sens_hum_temp_value.ID = data.ID
    LEFT JOIN hum_earth ON hum_earth.ID = data.ID
    ORDER BY data.ID DESC LIMIT 1
    """
    lplp = list(conn.execute(sqlread1))
    n = [list(f) for f in lplp] 
    c = []
    for q in range(len(n)):
        for t in range(len(n[q])):
            c.append(int(n[q][t]))
        
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
        hum_earth_6 = s10[1], 
        mid_temp = sum(j)/len(j), 
        mid_hum = sum(c)/len(c))




@app.route('/index/about_us')
def about_us():
    return render_template('about_us.html',
        title = 'about_us')

@app.route('/index/input')
def input():
    return render_template('input.html',
        title = 'Ввод значений')

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
    conn = sqlite3.connect("greenhouse.db")
    zpr = "temp_value_1, hum_value_1"
    sqlread1 = f"""\
    SELECT {zpr} FROM data
    LEFT JOIN sens_hum_temp_value ON sens_hum_temp_value.ID = data.ID
    LEFT JOIN hum_earth ON hum_earth.ID = data.ID
    ORDER BY data.ID DESC LIMIT 10
    """
    lxlx = list(conn.execute(sqlread1))
    global smarr1
    smarr1 = [list(f) for f in lxlx] 
    return render_template('index.html')

@app.route('/index/temp_2')
def sensor_2():
    conn = sqlite3.connect("greenhouse.db")
    zpr = "temp_value_2, hum_value_2"
    sqlread1 = f"""\
    SELECT {zpr} FROM data
    LEFT JOIN sens_hum_temp_value ON sens_hum_temp_value.ID = data.ID
    LEFT JOIN hum_earth ON hum_earth.ID = data.ID
    ORDER BY data.ID DESC LIMIT 10
    """
    lxlx = list(conn.execute(sqlread1))
    global smarr2
    smarr2 = [list(f) for f in lxlx]    
    return render_template('index.html')

@app.route('/index/temp_3')
def sensor_3():    
    conn = sqlite3.connect("greenhouse.db")
    zpr = "temp_value_3, hum_value_3"
    sqlread1 = f"""\
    SELECT {zpr} FROM data
    LEFT JOIN sens_hum_temp_value ON sens_hum_temp_value.ID = data.ID
    LEFT JOIN hum_earth ON hum_earth.ID = data.ID
    ORDER BY data.ID DESC LIMIT 10
    """
    lxlx = list(conn.execute(sqlread1))
    global smarr3
    smarr3 = [list(f) for f in lxlx]    
    return render_template('index.html')

@app.route('/index/temp_4')
def sensor_4():    
    conn = sqlite3.connect("greenhouse.db")
    zpr = "temp_value_4, hum_value_4"
    sqlread1 = f"""\
    SELECT {zpr} FROM data
    LEFT JOIN sens_hum_temp_value ON sens_hum_temp_value.ID = data.ID
    LEFT JOIN hum_earth ON hum_earth.ID = data.ID
    ORDER BY data.ID DESC LIMIT 10
    """
    lxlx = list(conn.execute(sqlread1))
    global smarr4
    smarr4 = [list(f) for f in lxlx]    
    return render_template('index.html')

@app.route('/index/humearth_1')
def sensor_5():    
    conn = sqlite3.connect("greenhouse.db")
    zpr = "hum_earth_1"
    sqlread1 = f"""\
    SELECT {zpr} FROM data
    LEFT JOIN sens_hum_temp_value ON sens_hum_temp_value.ID = data.ID
    LEFT JOIN hum_earth ON hum_earth.ID = data.ID
    ORDER BY data.ID DESC LIMIT 10
    """
    lxlx = list(conn.execute(sqlread1))
    global smarr5
    smarr5 = [list(f) for f in lxlx]    
    return render_template('index.html')

@app.route('/index/humearth_2')
def sensor_6():   
    conn = sqlite3.connect("greenhouse.db")
    zpr = "hum_earth_2"
    sqlread1 = f"""\
    SELECT {zpr} FROM data
    LEFT JOIN sens_hum_temp_value ON sens_hum_temp_value.ID = data.ID
    LEFT JOIN hum_earth ON hum_earth.ID = data.ID
    ORDER BY data.ID DESC LIMIT 10
    """
    lxlx = list(conn.execute(sqlread1))
    global smarr6
    smarr6 = [list(f) for f in lxlx]     
    return render_template('index.html')

@app.route('/index/humearth_3')
def sensor_7():   
    conn = sqlite3.connect("greenhouse.db") 
    zpr = "hum_earth_3"
    sqlread1 = f"""\
    SELECT {zpr} FROM data
    LEFT JOIN sens_hum_temp_value ON sens_hum_temp_value.ID = data.ID
    LEFT JOIN hum_earth ON hum_earth.ID = data.ID
    ORDER BY data.ID DESC LIMIT 10
    """
    lxlx = list(conn.execute(sqlread1))
    global smarr7
    smarr7 = [list(f) for f in lxlx]    
    return render_template('index.html')

@app.route('/index/humearth_4')
def sensor_8():    
    conn = sqlite3.connect("greenhouse.db")
    zpr = "hum_earth_4"
    sqlread1 = f"""\
    SELECT {zpr} FROM data
    LEFT JOIN sens_hum_temp_value ON sens_hum_temp_value.ID = data.ID
    LEFT JOIN hum_earth ON hum_earth.ID = data.ID
    ORDER BY data.ID DESC LIMIT 10
    """
    lxlx = list(conn.execute(sqlread1))
    global smarr8
    smarr8 = [list(f) for f in lxlx]    
    return render_template('index.html')

@app.route('/index/humearth_5')
def sensor_9():  
    conn = sqlite3.connect("greenhouse.db")  
    zpr = "hum_earth_5"
    sqlread1 = f"""\
    SELECT {zpr} FROM data
    LEFT JOIN sens_hum_temp_value ON sens_hum_temp_value.ID = data.ID
    LEFT JOIN hum_earth ON hum_earth.ID = data.ID
    ORDER BY data.ID DESC LIMIT 10
    """
    lxlx = list(conn.execute(sqlread1))
    global smarr9
    smarr9 = [list(f) for f in lxlx]    
    return render_template('index.html')

@app.route('/index/humearth_6')
def sensor_10():    
    conn = sqlite3.connect("greenhouse.db")
    zpr = "hum_earth_6"
    sqlread1 = f"""\
    SELECT {zpr} FROM data
    LEFT JOIN sens_hum_temp_value ON sens_hum_temp_value.ID = data.ID
    LEFT JOIN hum_earth ON hum_earth.ID = data.ID
    ORDER BY data.ID DESC LIMIT 10
    """
    lxlx = list(conn.execute(sqlread1))
    global smarr10
    smarr10 = [list(f) for f in lxlx] 
    return render_template('index.html')



