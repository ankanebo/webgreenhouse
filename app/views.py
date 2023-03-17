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

stop_start_data_base = False

@app.route('/start_bd',  methods=['POST'])
def start_end():
    global stop_start_data_base
    stop_start_data_base = not stop_start_data_base
    bd.data_base()
    return '{"status":"sucses"}'

avaragehum = 75
averagetemp = 25
averagehumearth = 80
averagetempinput = []
averagetempinput.append(averagetemp)
# averagetemp = averagetempinput[-1]

@app.route('/inputvalues', methods=['POST'])
def button_input():
    global averagetemp
    global avaragehum
    global averagehumearth
    global mid_hum_earh_1_value
    averagehuminput = []
    global averagetempinput
    data = flask.request.get_json()
    averagetempinput.append(averagetemp)
    if data["averagetemp"] != None:
        averagetemp = data["averagetemp"]
        # averagetempinput.append(averagetemp)
    # else:
    #     averagetemp = averagetempinput[-2]
    # print(averagetempinput)
    if data["averagehum"] != None:
        avaragehum = data["averagehum"]
    if data["averagehumearth"] != None:
        averagehumearth = data["averagehumearth"]
    return 'sucsees'

mid_hum_earth_post_1_value = 0
mid_hum_earth_post_2_value = 0
mid_hum_earth_post_3_value = 0
mid_hum_earth_post_4_value = 0
mid_hum_earth_post_5_value = 0
mid_hum_earth_post_6_value = 0
mid_temp_post = 27

@app.route('/average_temp_post', methods=['POST'])
def average_temp_post():
    global mid_temp_post 
    a1 = requests.get(urlth1).json()
    a2 = requests.get(urlth2).json()
    a3 = requests.get(urlth3).json()
    a4 = requests.get(urlth4).json()
    
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

    mid_temp_post = sum(f)/len(f)
    


@app.route('/average_hum_earth_post_1', methods=['POST'])
def average_hum_earth_post_1():
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    global mid_hum_earth_post_1_value
    global mid_hum_earth_post_2_value
    global mid_hum_earth_post_3_value
    global mid_hum_earth_post_4_value
    global mid_hum_earth_post_5_value
    global mid_hum_earth_post_6_value
    conn = sqlite3.connect("greenhouse.db")
    zpr = "hum_earth_1, hum_earth_2, hum_earth_3, hum_earth_4, hum_earth_5, hum_earth_6"
    sqlread1 = f"""\
    SELECT {zpr} FROM data
    LEFT JOIN sens_hum_temp_value ON sens_hum_temp_value.ID = data.ID
    LEFT JOIN hum_earth ON hum_earth.ID = data.ID
    ORDER BY data.ID DESC LIMIT 10
    """
    lsls = list(conn.execute(sqlread1))
    midhumearth1 = []
    midhumearth2 = []
    midhumearth3 = []
    midhumearth4 = []
    midhumearth5 = []
    midhumearth6 = []
    for i in range(len(lsls)):
        midhumearth1.append(lsls[i][0])
        midhumearth2.append(lsls[i][1])
        midhumearth3.append(lsls[i][2])
        midhumearth4.append(lsls[i][3])
        midhumearth5.append(lsls[i][4])
        midhumearth6.append(lsls[i][5])
    mid_hum_earth_post_1_value = round((sum(midhumearth1) / len(midhumearth1)), 2)
    mid_hum_earth_post_2_value = round((sum(midhumearth2) / len(midhumearth2)), 2)
    mid_hum_earth_post_3_value = round((sum(midhumearth3) / len(midhumearth3)), 2)
    mid_hum_earth_post_4_value = round((sum(midhumearth4) / len(midhumearth4)), 2)
    mid_hum_earth_post_5_value = round((sum(midhumearth5) / len(midhumearth5)), 2)
    mid_hum_earth_post_6_value = round((sum(midhumearth6) / len(midhumearth6)), 2)
    print(mid_hum_earth_post_1_value)
    conn.close()
    return 'sucsees'

@app.route('/')
@app.route('/index/index')
def index():
    mid_hum_earth_1()
    global mid_hum_earth_post_1_value
    global mid_hum_earth_post_2_value
    global mid_hum_earth_post_3_value
    global mid_hum_earth_post_4_value
    global mid_hum_earth_post_5_value
    global mid_hum_earth_post_6_value
    global stop_start_data_base
    global averagetemp
    global avaragehum
    global averagehumearth
    global mid_hum_earth_1_value
    global mid_hum_earth_2_value
    global mid_hum_earth_3_value
    global mid_hum_earth_4_value
    global mid_hum_earth_5_value
    global mid_hum_earth_6_value

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
    return render_template("index.html",
        title = 'Home',
        mid_temp = sum(f)/len(f),
        mid_hum = sum(h)/len(h),
        input_temp = averagetemp,
        input_hum = avaragehum,
        input_hum_earth = averagehumearth,
        average_hum_earth_1 = mid_hum_earth_1_value,
        average_hum_earth_2 = mid_hum_earth_2_value,
        average_hum_earth_3 = mid_hum_earth_3_value,
        average_hum_earth_4 = mid_hum_earth_4_value,
        average_hum_earth_5 = mid_hum_earth_5_value,
        average_hum_earth_6 = mid_hum_earth_6_value,
        stop_start_data_base = ("true" if stop_start_data_base else "false"),
        text_bd_false = 'Включить запись информации с датчиков',
        text_bd_true = 'Выключить запись информации с датчиков',
        text_bd_core = ("Выключить запись информации с датчиков" if stop_start_data_base  else "Включить запись информации с датчиков"),
        average_hum_earth_post_1 = mid_hum_earth_post_1_value,
        average_hum_earth_post_2 = mid_hum_earth_post_2_value,
        average_hum_earth_post_3 = mid_hum_earth_post_3_value,
        average_hum_earth_post_4 = mid_hum_earth_post_4_value,
        average_hum_earth_post_5 = mid_hum_earth_post_5_value,
        average_hum_earth_post_6 = mid_hum_earth_post_6_value,
        average_temp_earth_input_alert = averagetemp,
        )


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

@app.route('/button_index', methods=['POST'])
def buton_1():
    data = flask.request.get_json()
    list_of_temp = data['temp']
    list_of_hum = data['hum']
    list_of_hum_of_earth = data['humearth']

    conn = sqlite3.connect("greenhouse.db")
    global count
    try:
        log = open('log.txt')
        count = int(log.readline())
        log.close()
    except FileNotFoundError:
        log = open('log.txt', 'w')
        count = 0
        log.write(str(count))
        log.close()
    maxID = count + 1
    rs = []
    for pr in zip(list_of_temp, list_of_hum):
        rs.extend(pr)
    for i in range(len(rs)):
        rs[i] = float(rs[i])
    rs = [maxID] + rs
    print(rs)
    # используем параметры запроса вместо форматирования строк
    sqlTH = """INSERT INTO sens_hum_temp_value VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"""
    conn.execute(sqlTH, rs)
    lh = list_of_hum_of_earth
    for i in range(len(lh)):
        lh[i] = float(lh[i])
    lh = [maxID] + lh
    print(lh)
    sqlHE = """INSERT INTO hum_earth VALUES (?, ?, ?, ?, ?, ?, ?)"""
    conn.execute(sqlHE, lh)
    sqlDT = f"""\
    INSERT INTO data
        VALUES ({maxID}, datetime('now'));
    """
    conn.execute(sqlDT)
    count += 1
    log = open('log.txt', 'w')
    log.write(str(count))
    log.close()
    conn.commit()
    conn.close()
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

date_1 = "2023-03-14 10:23:54"
date_2 = "2023-03-14 10:24:18"

@app.route('/input_dates', methods=["POST"])
def input_dates():
    print('input!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    global date_1
    global date_2
    data = flask.request.get_json()
    date_1 = data['date_from']
    date_2 = data['date_to']
    print(date_1)
    print(date_2)
    return 'sucsees'

@app.route('/input_dates_temp_hum')
def input_dates_temp_hum():
    global date_1
    global date_2
    number = flask.request.args.get("number")
    zprd = "temp_value_"+ number +", hum_value_"+ number + ", dates"
    conn = sqlite3.connect("greenhouse.db")
    sqlread= f"""\
    SELECT {zprd} FROM data
    LEFT JOIN sens_hum_temp_value ON sens_hum_temp_value.ID = data.ID
    LEFT JOIN hum_earth ON hum_earth.ID = data.ID
    WHERE data.dates > '{date_1}' AND data.dates < '{date_2}'
    """
    xxxx = list(conn.execute(sqlread))
    ret2 = {"temp": [], "hum": [], "date": []}
    for i in range(len(xxxx)):
        ret2["temp"].append(xxxx[i][0])
        ret2["hum"].append(xxxx[i][1])
        ret2["date"].append(xxxx[i][2])
    conn.close()
    return json.dumps(ret2)

@app.route('/input_dates_hum_earth')
def input_dates_hum_earth(): 
    global date_1
    global date_2
    number = flask.request.args.get("number")
    conn = sqlite3.connect("greenhouse.db")
    zprd = "hum_earth_"+ number + ", dates"
    sqlread1 = f"""\
    SELECT {zprd} FROM data
    LEFT JOIN sens_hum_temp_value ON sens_hum_temp_value.ID = data.ID
    LEFT JOIN hum_earth ON hum_earth.ID = data.ID
    WHERE data.dates > '{date_1}' AND data.dates < '{date_2}'
    """
    lxlx = list(conn.execute(sqlread1)) 
    ret3 = {"hum_earth": [], "date": []}
    for i in range(len(lxlx)):
        ret3["hum_earth"].append(lxlx[i][0])
        ret3["date"].append(lxlx[i][1])
    conn.close()
    return json.dumps(ret3)


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
        j = round(((lsls[i][0] + lsls[i][1] + lsls[i][2] + lsls[i][3]) / 4), 2)
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
        j = round(((lsls[i][0] + lsls[i][1] + lsls[i][2] + lsls[i][3]) / 4), 2)
        p = lsls[i][-1]
        mid_hum["mid_hum"].append(j)
        mid_hum["date"].append(p)
    conn.close()
    return json.dumps(mid_hum)

mid_hum_earth_1_value = 0
mid_hum_earth_2_value = 0
mid_hum_earth_3_value = 0
mid_hum_earth_4_value = 0
mid_hum_earth_5_value = 0
mid_hum_earth_6_value = 0

@app.route('/mid_hum_earth')
def mid_hum_earth_1():
    global mid_hum_earth_1_value
    global mid_hum_earth_2_value
    global mid_hum_earth_3_value
    global mid_hum_earth_4_value
    global mid_hum_earth_5_value
    global mid_hum_earth_6_value
    conn = sqlite3.connect("greenhouse.db")
    zpr = "hum_earth_1, hum_earth_2, hum_earth_3, hum_earth_4, hum_earth_5, hum_earth_6"
    sqlread1 = f"""\
    SELECT {zpr} FROM data
    LEFT JOIN sens_hum_temp_value ON sens_hum_temp_value.ID = data.ID
    LEFT JOIN hum_earth ON hum_earth.ID = data.ID
    ORDER BY data.ID DESC LIMIT 10
    """
    lsls = list(conn.execute(sqlread1))
    midhumearth1 = []
    midhumearth2 = []
    midhumearth3 = []
    midhumearth4 = []
    midhumearth5 = []
    midhumearth6 = []
    for i in range(len(lsls)):
        midhumearth1.append(lsls[i][0])
        midhumearth2.append(lsls[i][1])
        midhumearth3.append(lsls[i][2])
        midhumearth4.append(lsls[i][3])
        midhumearth5.append(lsls[i][4])
        midhumearth6.append(lsls[i][5])
    mid_hum_earth_1_value = round((sum(midhumearth1) / len(midhumearth1)), 2)
    mid_hum_earth_2_value = round((sum(midhumearth2) / len(midhumearth2)), 2)
    mid_hum_earth_3_value = round((sum(midhumearth3) / len(midhumearth3)), 2)
    mid_hum_earth_4_value = round((sum(midhumearth4) / len(midhumearth4)), 2)
    mid_hum_earth_5_value = round((sum(midhumearth5) / len(midhumearth5)), 2)
    mid_hum_earth_6_value = round((sum(midhumearth6) / len(midhumearth6)), 2)
    print(mid_hum_earth_1_value)
    conn.close()
    return 'sucsees'