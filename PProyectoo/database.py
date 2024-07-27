import sqlite3
import hashlib
import getpass
from tkinter import messagebox
def create_database():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS entries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        user TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

def register_user(user, password):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    hash_password = hashlib.sha256(password.encode()).hexdigest()

    try:
        cursor.execute('''
        INSERT INTO users (user, password)
        VALUES (?, ?)
        ''', (user, hash_password))

        conn.commit()
        messagebox.showinfo("Registro", "Usuario registrado exitosamente.")
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "El nombre de usuario ya existe. Inténtalo de nuevo.")
    finally:
        conn.close()

def login(user, password):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    hash_password = hashlib.sha256(password.encode()).hexdigest()

    cursor.execute('''
    SELECT * FROM users WHERE user = ? AND password = ?
    ''', (user, hash_password))

    valid_user = cursor.fetchone()

    conn.close()

    return valid_user

def add_entries(user, date, title, content):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO entries (date, title, content, user)
    VALUES (?, ?, ?, ?)
    ''', (date, title, content, user))

    conn.commit()
    conn.close()

def read_entries(user):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM entries WHERE user = ?', (user,))
    entries = cursor.fetchall()

    conn.close()
    return entries

def update_entries(user, entry_id, new_title, new_content):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''
    UPDATE entries
    SET title = ?, content = ?
    WHERE id = ? AND user = ?
    ''', (new_title, new_content, entry_id, user))

    conn.commit()
    conn.close()

def delete_entries(user, entry_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''
    DELETE FROM entries
    WHERE id = ? AND user = ?
    ''', (entry_id, user))

    conn.commit()
    conn.close()
create_database()