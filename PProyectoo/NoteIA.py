import sqlite3
import openai
from datetime import datetime
import os
from transformers import GPT2Tokenizer, TFGPT2LMHeadModel, pipeline

####
note_pad = "note_pad.db"

tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

tokenizer.pad_token = tokenizer.eos_token

model = TFGPT2LMHeadModel.from_pretrained('gpt2')

summarizer = pipeline('summarization', model="facebook/bart-large-cnn")

def error():
    print("Error")
    input()
    os.system("cls")
#####
def crear_base_de_datos():
    conn = sqlite3.connect(note_pad)
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

def agregar_entrada(fecha, titulo, contenido):
    conn = sqlite3.connect(note_pad)
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO entradas (fecha, titulo, contenido)
    VALUES (?, ?, ?)
    ''', (fecha, titulo, contenido))

    conn.commit()
    conn.close()

    print("Entrada agregada exitosamente.")

def leer_entradas():
    conn = sqlite3.connect(note_pad)
    cursor = conn.cursor()

    cursor.execute('''
    SELECT * FROM entradas
    ''')
    entradas = cursor.fetchall()

    for entrada in entradas:
        print(f"ID: {entrada[0]}")
        print(f"Fecha: {entrada[1]}")
        print(f"Título: {entrada[2]}")
        print(f"Contenido: {entrada[3]}\n")
        input()
        print("\n1. Resumirlo\n")
        print("2. Generar texto aleatorio\n")
        print("3. Regresar\n")
        print("4. Volver al menu principal\n")
        ans= input()
        if ans == '1':
            resumen_generado = summarizer(entrada[3], max_length=200, min_length=50, do_sample=True)
            print(f"\nContenido Resumido: {resumen_generado[0]['summary_text']}\n")
        elif ans== '2':
            try:
                text = entrada[3]
                encoded_input = tokenizer(text, return_tensors='tf')
                output = model.generate(encoded_input['input_ids'], attention_mask=encoded_input['attention_mask'], max_length=80, num_return_sequences=1)
                decoded_output = tokenizer.decode(output[0], skip_special_tokens=False)
                print(decoded_output)
            except Exception as error: 
                print(f"Error durante la generacion de texto {error}")
        elif ans== '3':
            break     
        elif ans == '4':
            conn.close()
            return

    conn.close()

def actualizar_entrada(id_entrada, nuevo_titulo, nuevo_contenido):
    conn = sqlite3.connect(note_pad)
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
    conn = sqlite3.connect(note_pad)
    cursor = conn.cursor()

    cursor.execute('''
    DELETE FROM entradas
    WHERE id = ?
    ''', (id_entrada,))

    conn.commit()
    conn.close()

    print("Entrada eliminada exitosamente.")

def menu():
    while True:
        print("\nNotas Personales")
        print("1. Agregar nueva entrada")
        print("2. Leer entradas")
        print("3. Actualizar una entrada")
        print("4. Eliminar una entrada")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            fecha_actual = datetime.now().strftime('%Y-%m-%d %H:%M')
            titulo = input("Título: ")
            contenido = input("Contenido: ")
            agregar_entrada(fecha_actual, titulo, contenido)
        elif opcion == '2':
            leer_entradas()
        elif opcion == '3':
            id_entrada = int(input("ID de la entrada a actualizar: "))
            nuevo_titulo = input("Nuevo título: ")
            nuevo_contenido = input("Nuevo contenido: ")
            actualizar_entrada(id_entrada, nuevo_titulo, nuevo_contenido)
        elif opcion == '4':
            id_entrada = int(input("ID de la entrada a eliminar: "))
            eliminar_entrada(id_entrada)
        elif opcion == '5':
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
            error()

if __name__ == '__main__':
    crear_base_de_datos()
    menu()
