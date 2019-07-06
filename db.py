import sqlite3

def db(data):
    con = sqlite3.connect('wmu.db')
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS WMU(chat_id text, message text, time text)')

    cur.execute('INSERT INTO WMU VALUES(?, ?, ?)', data)

    con.commit()
