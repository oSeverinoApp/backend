import psycopg2

DB_HOST = 'localhost'
DB_NAME = 'severinoapp_db'
DB_USER = 'severinoapp'
DB_PASS = 'severinoapp'
DB_PORT = '5433'

def connect():
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )
    return conn

def create_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS user_data (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100),
            type VARCHAR(20)
        )
    ''')
    conn.commit()
    cur.close()
    conn.close()

create_table()


