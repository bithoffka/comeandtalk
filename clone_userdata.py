import sqlite3 as sq

with sq.connect("main_db.db") as con:
    cur = con.cursor()

    #cur.execute(''' CREATE TABLE IF NOT EXISTS main_db (
    #cat_id INTEGER PRIMARY KEY, 
    #class_id TEXT,
    #paid_lessons INTEGER
    #)''')
    #con.commit()
    #
    #cur.execute('''INSERT INTO main_db (class_id, paid_lessons)
    #VALUES ('id111', 1)
    #''')
    #cur.execute("""UPDATE main_db
    #SET class_id = 'id212', paid_lessons = '5', cat_id = 2
    #WHERE cat_id = 1;                 
    #""")


    data1 = cur.execute("SELECT * FROM catid_db").fetchall()

    

print(data1)