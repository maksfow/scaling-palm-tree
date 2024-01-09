import sqlite3
connection = sqlite3.connect("shop.db", check_same_thread=False)
sql = connection.cursor()
sql.execute('CREATE TABLE IF NOT EXISTS users '
            '(id INTEGER, name TEXT, number TEXT, location TEXT);')
def register(user_id,name,number,location):
    sql.execute('INSERT INTO users VALUES( ?,?, ?, ?);', (user_id, name, number, location))
    connection.commit()
def checker(id):
    res = sql.execute("SELECT name FROM users WHERE id=?; ",(id,))
    if res.fetchone():
        return True
    else:
        return False