import sqlite3

note_pad_db = "note_pad.db"

def crear_base_de_datos():
    conn = sqlite3.connect(note_pad_db)
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS entradas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha TEXT NOT NULL,
        titulo TEXT NOT NULL,
        contenido TEXT NOT NULL
    )
    ''')

    conn.commit()
    conn.close()

def leer_entradas(id_entrada):
    conn = sqlite3.connect(note_pad_db)
    cursor = conn.cursor()
    entrada=None
    try:
        cursor.execute('''
        SELECT * FROM entradas
        WHERE id = ?
        ''',(id_entrada,))
        entrada= cursor.fetchone()
    except sqlite3.Error as e:
        print(f"Error al leer la entrada: {e}")
    finally:
        conn.close()
    return entrada 

def agregar_entrada(fecha_actual, titulo, contenido):
    conn = sqlite3.connect(note_pad_db)
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO entradas (fecha, titulo, contenido)
    VALUES (?, ?, ?)
    ''', (fecha_actual, titulo, contenido))

    conn.commit()
    conn.close()

    print("Entrada agregada exitosamente.")

def actualizar_entrada(id_entrada, nuevo_titulo, nuevo_contenido):
    conn = sqlite3.connect(note_pad_db)
    cursor = conn.cursor()

    try:
        cursor.execute('''
        UPDATE entradas
        SET titulo = ?, contenido = ?
        WHERE id = ?
        ''', (nuevo_titulo, nuevo_contenido, id_entrada))

        conn.commit()
        print("Entrada actualizada exitosamente.")
    except sqlite3.Error as e:
        print(f"Error al actualizar la entrada: {e}")
    finally:
        conn.close()
        
def eliminar_entrada(id_entrada):
    conn = sqlite3.connect(note_pad_db)
    cursor = conn.cursor()

    cursor.execute('''
    DELETE FROM entradas
    WHERE id = ?
    ''', (id_entrada,))

    conn.commit()
    conn.close()

    print("Entrada eliminada exitosamente.")
