from tkinter import messagebox
from database import register_user, login, update_entries, delete_entries, read_entries, add_entries

class AppLogic:
    def __init__(self, app):
        self.app = app
    
    def register(self):
        user = self.app.entry_registro_usuario.get()
        password = self.app.entry_registro_contrasena.get()

        if user and password:
            register_user(user, password)
            messagebox.showinfo("Registro exitoso")
        else:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")

    def login(self):
        user = self.app.entry_login_usuario.get()
        password = self.app.entry_login_contrasena.get()

        if user and password:
            valid_user = login(user, password)
            if valid_user:
                self.app.current_user = user
                self.app.show_main_menu()
            else:
                messagebox.showerror("Error", "Nombre de usuario o contraseña incorrectos.")
        else:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")

    def add_new_entry(self):
        fecha = self.app.entry_fecha.get()
        titulo = self.app.entry_titulo.get()
        contenido = self.app.text_contenido.get("1.0", "end-1c")

        if fecha and titulo and contenido:
            add_entries(self.app.current_user, fecha, titulo, contenido)
            messagebox.showinfo("Éxito", "Entrada agregada exitosamente.")
        else:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")

    def read_entries(self):
        entradas = read_entries(self.app.current_user)
        self.app.text_lectura.delete("1.0", "end")
        for entrada in entradas:
            self.app.text_lectura.insert("end", f"ID: {entrada[0]}\nFecha: {entrada[1]}\nTítulo: {entrada[2]}\nContenido: {entrada[3]}\n\n")

    def update_selected_entry(self):
        id_entrada = self.app.entry_id_actualizar.get()
        nuevo_titulo = self.app.entry_nuevo_titulo.get()
        nuevo_contenido = self.app.text_nuevo_contenido.get("1.0", "end-1c")

        if id_entrada and nuevo_titulo and nuevo_contenido:
            update_entries(self.app.current_user, int(id_entrada), nuevo_titulo, nuevo_contenido)
            messagebox.showinfo("Éxito", "Entrada actualizada exitosamente.")
        else:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")

    def delete_selected_entry(self):
        id_entrada = self.app.entry_id_eliminar.get()

        if id_entrada:
            delete_entries(self.app.current_user, int(id_entrada))
            messagebox.showinfo("Éxito", "Entrada eliminada exitosamente.")
        else:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
