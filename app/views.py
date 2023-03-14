from flask import render_template, flash, redirect
from app import app
import flask
import requests
from bd import urlth1, urlth2, urlth3, urlth4, urlhum1, urlhum2, urlhum3, urlhum4, urlhum5, urlhum6
import sqlite3
import json
import bd

#from templates.getpost import getpost
# print('view!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')


@app.route('/start_bd',  methods=['POST'])
def start_end():
    bd.data_base()
    return '{"status":"sucses"}'

@app.route('/')
@app.route('/index/index')
def index():
    return render_template("index.html",
        title = 'Home')

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


    
    f = []
    h = []
    s1 = []
    for k in a1.values():
        s1.append(float(k))
    f.append(int(s1[1]))
    h.append(int(s1[2]))

    s2 = []
    for k in a2.values():
        s2.append(float(k))
    f.append(int(s2[1]))
    h.append(int(s2[2]))

    s3 = []
    for k in a3.values():
        s3.append(float(k))
    f.append(int(s3[1]))
    h.append(int(s3[2]))
    
    s4 = []
    for k in a4.values():
        s4.append(float(k))
    f.append(int(s4[1]))
    h.append(int(s4[2]))
    
    s5 = []
    for k in b1.values():
        s5.append(float(k))

    s6 = []
    for k in b2.values():
        s6.append(float(k))

    s7 = []
    for k in b3.values():
        s7.append(float(k))

    s8 = []
    for k in b4.values():
        s8.append(float(k))

    s9 = []
    for k in b5.values():
        s9.append(float(k))

    s10 = []
    for k in b6.values():
        s10.append(float(k))
    
        
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
        mid_temp = sum(f)/len(f), 
        mid_hum = sum(h)/len(h))




@app.route('/index/about_us')
def about_us():
    return render_template('about_us.html',
        title = 'about_us')

@app.route('/index/input', methods = ['GET', 'POST'])
def input():
    return render_template('input.html',
            title = 'Ввод значений')

@app.route('/button_1', methods=['POST'])
def buton_1():
    data = flask.request.get_json()
    list_of_temp = data['temp']
    list_of_hum = data['hum']
    list_of_hum_of_earth = data['humearth']

    # conn = sqlite3.connect("greenhouse.db")
    # global count
    # log = open('log.txt')
    # count = int(log.readline())
    # log.close() 
    # maxID = count + 1
    # rs = []
    # for pr in zip(list_of_temp, list_of_hum):
    #     rs.extend(pr)
    # rs = [maxID] + rs
    # for i in range(len(rs)):
    #     rs[i] = float(rs[i])
    # print(rs)
    # # rs = "'" + ', '.join(lh) + "'"
    # # используем параметры запроса вместо форматирования строк
    # sqlTH = """INSERT INTO sens_hum_temp_value VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"""
    # conn.execute(sqlTH, rs)
    # lh = list_of_hum_of_earth
    # lh = [maxID] + lh
    # for i in range(len(lh)):
    #     lh[i] = float(lh[i])
    # print(lh)
    # # lh = "'" + ', '.join(lh) + "'"
    # sqlHE = """INSERT INTO hum_earth VALUES (?, ?, ?, ?, ?, ?, ?)"""
    # conn.execute(sqlHE, lh)
    # sqlDT = f"""\
    # INSERT INTO data
    #     VALUES ({maxID}, datetime('now'));
    # """
    # conn.execute(sqlDT)
    # maxID += 1 
    # count += 1
    # log = open('log.txt', 'w')
    # log.write(str(count))
    # log.close()

    # print(list_of_temp, list_of_hum, list_of_hum_of_earth )
    return 'sucsess'



@app.route('/button_2', methods = ['POST'])
def buton_2():
    data = flask.request.get_json()
    global list_of_average_temp
    list_of_average_temp = data['averagetemp']
    # global input_temp
    # if len(list_of_average_temp) == 0:
    #     input_temp = 25
    # else:
    #     input_temp = list_of_average_temp[0]
    # print(list_of_average_temp)
    return 'sucsess'

@app.route('/button_3', methods = ['POST'])
def buton_3():
    data = flask.request.get_json()
    list_of_average_hum_of_oxygen = data['averagehumofoxygen']
    # print(list_of_average_hum_of_oxygen)
    return 'sucsess'

@app.route('/button_4', methods = ['POST'])
def buton_4():
    data = flask.request.get_json()
    list_of_average_hum_of_earth = data['averagehumofearth']
    # print(list_of_average_hum_of_earth)
    return 'sucsess'


@app.route('/index/temp_hum')
def temp_hum():
    number = flask.request.args.get("number")
    conn = sqlite3.connect("greenhouse.db")
    zpr = "temp_value_"+ number +", hum_value_"+ number + ", dates"
    sqlread1 = f"""\
    SELECT {zpr} FROM data
    LEFT JOIN sens_hum_temp_value ON sens_hum_temp_value.ID = data.ID
    LEFT JOIN hum_earth ON hum_earth.ID = data.ID
    ORDER BY data.ID DESC LIMIT 10
    """
    lxlx = list(conn.execute(sqlread1)) 
    ret = {"temp": [], "hum": [], "date": []}
    for i in lxlx:
        j = list(i)
        ret["temp"].append(j[0])
        ret["hum"].append(j[1])
        ret["date"].append(j[2])
    conn.close()
    return json.dumps(ret)



@app.route('/index/hum_earth')
def hum_earth():    
    number = flask.request.args.get("number")
    conn = sqlite3.connect("greenhouse.db")
    zpr = "hum_earth_"+ number + ", dates"
    sqlread1 = f"""\
    SELECT {zpr} FROM data
    LEFT JOIN sens_hum_temp_value ON sens_hum_temp_value.ID = data.ID
    LEFT JOIN hum_earth ON hum_earth.ID = data.ID
    ORDER BY data.ID DESC LIMIT 10
    """
    lxlx = list(conn.execute(sqlread1)) 
    ret_1 = {"hum_earth": [], "date": []}
    for i in lxlx:
        j = list(i)
        ret_1["hum_earth"].append(j[0])
        ret_1["date"].append(j[1])
    conn.close()
    return json.dumps(ret_1)


@app.route('/mid_temp_graph')
def mid_temp_graph():
    conn = sqlite3.connect("greenhouse.db")
    zpr = "temp_value_1, temp_value_2, temp_value_3, temp_value_4, dates"
    sqlread1 = f"""\
    SELECT {zpr} FROM data
    LEFT JOIN sens_hum_temp_value ON sens_hum_temp_value.ID = data.ID
    LEFT JOIN hum_earth ON hum_earth.ID = data.ID
    ORDER BY data.ID DESC LIMIT 10
    """
    lsls = list(conn.execute(sqlread1))
    mid_temp = {"mid_temp": [], "date": []}
    for i in range(len(lsls)):
        j = (lsls[i][0] + lsls[i][1] + lsls[i][2] + lsls[i][3]) / 4
        p = lsls[i][-1]
        mid_temp["mid_temp"].append(j)
        mid_temp["date"].append(p)
    conn.close()
    return json.dumps(mid_temp)

@app.route('/mid_hum_graph')
def mid_hum_graph():
    conn = sqlite3.connect("greenhouse.db")
    zpr = "hum_value_1, hum_value_2, hum_value_3, hum_value_4, dates"
    sqlread1 = f"""\
    SELECT {zpr} FROM data
    LEFT JOIN sens_hum_temp_value ON sens_hum_temp_value.ID = data.ID
    LEFT JOIN hum_earth ON hum_earth.ID = data.ID
    ORDER BY data.ID DESC LIMIT 10
    """
    lsls = list(conn.execute(sqlread1))
    mid_hum = {"mid_hum": [], "date": []}
    for i in range(len(lsls)):
        j = (lsls[i][0] + lsls[i][1] + lsls[i][2] + lsls[i][3]) / 4
        p = lsls[i][-1]
        mid_hum["mid_hum"].append(j)
        mid_hum["date"].append(p)
    conn.close()
    return json.dumps(mid_hum)