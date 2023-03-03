import sqlite3
def bd():

    conn = sqlite3.connect("greenhouse.db")

    try:
        sql = """\
        CREATE TABLE sens_hum_temp_value(
            ID INTEGER PRIMARY KEY,
            temp_value_1 FLOAT,
            hum_value_1 FLOAT,
            temp_value_2 FLOAT,
            hum_value_2 FLOAT,
            temp_value_3 FLOAT,
            hum_value_3 FLOAT,
            temp_value_4 FLOAT,
            hum_value_4 FLOAT
        );
        CREATE TABLE hum_earth(
            ID INTEGER PRIMARY KEY,
            hum_earth_1 FLOAT,
            hum_earth_2 FLOAT,
            hum_earth_3 FLOAT,
            hum_earth_4 FLOAT,
            hum_earth_5 FLOAT,
            hum_earth_6 FLOAT
        );
        CREATE TABLE data(
            ID INTEGER PRIMARY KEY,
            dates INTEGER
        )
        """

        conn.executescript(sql)
            
        sql = """\
        INSERT INTO sens_hum_temp_value
            VALUES (0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0);
        INSERT INTO hum_earth
            VALUES (0,0.0,0.0,0.0,0.0,0.0,0.0);
        INSERT INTO data
            VALUES (0, datetime('now'));

        """
        conn.executescript(sql)


        sql = """\
        SELECT MAX(ID) FROM data;
        """

    except sqlite3.OperationalError:
        sql = """\
            SELECT MAX(ID) FROM data;
            """

    maxID = list(conn.execute(sql))[0][0]

    import requests

    urlth1 = 'https://dt.miet.ru/ppo_it/api/temp_hum/1'
    urlth2 = 'https://dt.miet.ru/ppo_it/api/temp_hum/2'
    urlth3 = 'https://dt.miet.ru/ppo_it/api/temp_hum/3'
    urlth4 = 'https://dt.miet.ru/ppo_it/api/temp_hum/4'
    urlhum1 = 'https://dt.miet.ru/ppo_it/api/hum/1'
    urlhum2 = 'https://dt.miet.ru/ppo_it/api/hum/2'
    urlhum3 = 'https://dt.miet.ru/ppo_it/api/hum/3'
    urlhum4 = 'https://dt.miet.ru/ppo_it/api/hum/4'
    urlhum5 = 'https://dt.miet.ru/ppo_it/api/hum/5'
    urlhum6 = 'https://dt.miet.ru/ppo_it/api/hum/6'

    import asyncio

    async def write():
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

        while True:
            resp1 = requests.get(urlth1)
            resp2 = requests.get(urlth2)
            resp3 = requests.get(urlth3)
            resp4 = requests.get(urlth4)
            resp21 = requests.get(urlhum1)
            resp22 = requests.get(urlhum2)
            resp23 = requests.get(urlhum3)
            resp24 = requests.get(urlhum4)
            resp25 = requests.get(urlhum5)
            resp26 = requests.get(urlhum6)

            th1 = resp1.json()
            th2 = resp2.json()
            th3 = resp3.json()
            th4 = resp4.json()
            hum1 = resp21.json()
            hum2 = resp22.json()
            hum3 = resp23.json()
            hum4 = resp24.json()
            hum5 = resp25.json()
            hum6 = resp26.json()
            s = str(maxID)+', '
            s1 = ''
            for k in th1.values():
                s1 += str(k)
                s1 += ', '
            s1 = s1[3::]
            s += s1
            s2 = ''
            for k in th2.values():
                s2 += str(k)
                s2 += ', '
            s2 = s2[3::]
            s += s2
            s3 = ''
            for k in th3.values():
                s3 += str(k)
                s3 += ', '
            s3 = s3[3::]
            s += s3
            s4 = ''
            for k in th4.values():
                s4 += str(k)
                s4 += ', '
            s4 = s4[3::]
            s += s4
            s = s[:len(s) - 2:]
            print(s)
            sql = """\
            INSERT INTO sens_hum_temp_value
                VALUES ("""+s+""");
            """
            conn.executescript(sql)
            x = str(maxID)+', '
            x1 = ''
            for k in hum1.values():
                x1 += str(k)
                x1 += ', '
            x1 = x1[3::]
            x += x1
            x2 = ''
            for k in hum2.values():
                x2 += str(k)
                x2 += ', '
            x2 = x2[3::]
            x += x2
            x3 = ''
            for k in hum3.values():
                x3 += str(k)
                x3 += ', '
            x3 = x3[3::]
            x += x3
            x4 = ''
            for k in hum4.values():
                x4 += str(k)
                x4 += ', '
            x4 = x4[3::]
            x += x4
            x5 = ''
            for k in hum5.values():
                x5 += str(k)
                x5 += ', '
            x5 = x5[3::]
            x += x5
            x6 = ''
            for k in hum6.values():
                x6 += str(k)
                x6 += ', '
            x6 = x6[3::]
            x += x6
            x = x[:len(x) - 2:]
            print(x)
            sql = """\
            INSERT INTO hum_earth
                VALUES("""+x+""");
            """
            conn.executescript(sql)
            sql = f"""\
            INSERT INTO data
                VALUES ({maxID}, datetime('now'));
            """
            conn.executescript(sql)
            maxID+=1
            count += 1
            print(count)
            log = open('log.txt', 'w')
            log.write(str(count))
            log.close()
            await asyncio.sleep(0)
    asyncio.run(write())