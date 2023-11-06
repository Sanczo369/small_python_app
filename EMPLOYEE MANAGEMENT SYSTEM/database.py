import sqlite3

def create_table():
    conn = sqlite3.connect('Employees.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Employees (
            id TEXT PRIMARY KEY,
            name TEXT,
            role TEXT,
            gender TEXT,
            status TEXT)''')
    conn.commit()
    conn.close()

def fetch_employees():
    conn = sqlite3.connect('Employees.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Employees')
    employees = cursor.fetchall()
    conn.close()
    return employees