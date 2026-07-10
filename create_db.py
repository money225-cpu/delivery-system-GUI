import sqlite3

def create_db():
    con=sqlite3.connect("rms.db")
    cur=con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS type(
        cid INTEGER PRIMARY KEY AUTOINCREMENT,
        name text,
        duration text, 
        charges text, 
        description text
    )""")
    con.commit()

    
    cur.execute("""CREATE TABLE IF NOT EXISTS parcel(
        tracking_id text PRIMARY KEY, 
        name text,
        email text,
        gender text,
        dob text,
        contact text,
        admission text,
        type text, 
        state text,
        city text,
        pin text,
        address text
    )""")
    con.commit()

   
    cur.execute("""CREATE TABLE IF NOT EXISTS result(
        rid INTEGER PRIMARY KEY AUTOINCREMENT,
        tracking_id text,
        name text,
        type text,
        weight text,
        status text,
        per text
    )""")
    con.commit()

    
    cur.execute("""CREATE TABLE IF NOT EXISTS employee(
        eid INTEGER PRIMARY KEY AUTOINCREMENT,
        f_name text,
        l_name text,
        contact text,
        email text,
        question text,
        answer text,
        password text,
        utype text
    )""")
    con.commit()
    
    con.close()
    print("Database Created Successfully!")

if __name__ == "__main__":
    create_db()