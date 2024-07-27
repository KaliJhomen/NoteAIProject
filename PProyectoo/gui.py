import tkinter as tk
from PIL import ImageTk, Image
from gui_logic import AppLogic

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Diario Personal Digital")
        self.geometry("800x600")
        self.iconbitmap("images/noteia.ico")
        self.configure(bg="gray10")
        self.attributes("-alpha", 0.9)
        self.resizable(False, False)
        
        self.logic = AppLogic(self)
        self.setup_ui()
    
    def setup_ui(self):
        self.show_login_screen()
    
    def show_login_screen(self):
        self.clear_window()
        self.logo = tk.Label(self, bg="gray10", bd=0)
        self.logo.place(relx=0.5, rely=0.3, anchor="center")
        self.set_image(self.logo, "images/logo.png", 100, 100)
        
        tk.Label(self, text="Selecciona un usuario", fg="snow", font=("Roboto", 20, "bold"), bg="gray15", bd=0).place(x=40, y=50)
        
        tk.Label(self, text="Usuario", font=("Segoe UI", 9, "bold"), fg="snow", bg="gray15", bd=0).place(x=350, y=50)
        self.entry_login_usuario = tk.Entry(self, bg="gray15", fg="snow", bd=0)
        self.entry_login_usuario.pack(pady=5)

        tk.Label(self, text="Contraseña", font=("Roboto", 9, "bold"), fg="snow", bg="gray15", bd=0).pack()
        self.entry_login_contrasena = tk.Entry(self, bg="gray15", bd=0, fg="snow", show="*")
        self.entry_login_contrasena.pack(pady=5)
        
        login_button = tk.Button(self, text="Iniciar Sesión", font=("Roboto", 9, "bold"), fg="snow", bg="gray15", bd=0, command=self.logic.login)
        login_button.pack(pady=0)
        self.Tooltip(login_button, "Iniciar Sesión")
        
        go_to_register_button = tk.Button(self, text="¿No tienes una cuenta?", font=("Roboto", 9, "bold"), fg="snow", bg="gray15", bd=0, command=self.show_register_screen)
        go_to_register_button.pack(pady=0)
        self.Tooltip(go_to_register_button, "Registrarse")

    def show_register_screen(self):
        self.clear_window()
        tk.Label(self, text="Registrar Usuario", fg="snow", font=("Roboto", 20, "bold"), bg="gray15", bd=0).pack(pady=10)
        
        tk.Label(self, text="Nombre de Usuario", font=("Segoe UI", 9, "bold"), fg="snow", bg="gray15", bd=0).pack()
        self.entry_registro_usuario = tk.Entry(self, bg="gray15", fg="snow", bd=0)
        self.entry_registro_usuario.pack(pady=5)

        tk.Label(self, text="Contraseña", font=("Roboto", 9, "bold"), fg="snow", bg="gray15", bd=0).pack()
        self.entry_registro_contrasena = tk.Entry(self, bg="gray15", fg="snow", bd=0, show="*")
        self.entry_registro_contrasena.pack(pady=5)

        register_button = tk.Button(self, text="Registrarse", font=("Roboto", 9, "bold"), fg="snow", bg="gray15", bd=0, command=self.logic.register)
        register_button.pack(pady=20)
        self.Tooltip(register_button, "Registrarse")
        
        back_button = tk.Button(self, text="Volver", font=("Roboto", 9, "bold"), fg="snow", bg="gray15", bd=0, command=self.show_login_screen)
        back_button.pack(pady=10)
        self.Tooltip(back_button, "Volver")

    def show_main_menu(self):
        self.clear_window()
        
        add_button = tk.Button(self, text="Agregar Nueva Entrada", font=("Roboto", 9, "bold"), command=self.show_add_entry_screen)
        add_button.pack(pady=5)
        self.Tooltip(add_button, "Agregar Nueva Entrada")
        self.set_image(add_button, "images/add.png", 100,100)
        
        read_entries_button = tk.Button(self, text="Leer Entradas", font=("Roboto", 9, "bold"), command=self.show_read_entries_screen)
        read_entries_button.pack(pady=5)
        self.Tooltip(read_entries_button, "Leer Entradas")

        update_entries_button = tk.Button(self, text="Actualizar Entrada", font=("Roboto", 9, "bold"), command=self.show_update_entry_screen)
        update_entries_button.pack(pady=5)
        self.Tooltip(update_entries_button, "Actualizar Entrada")
        
        delete_entry_button = tk.Button(self, text="Eliminar Entrada", font=("Roboto", 9, "bold"), command=self.show_delete_entry_screen)
        delete_entry_button.pack(pady=5)
        self.Tooltip(delete_entry_button, "Eliminar Entrada")
        
        sign_off_button = tk.Button(self, text="Cerrar Sesión", font=("Roboto", 13, "bold"), command=self.show_login_screen)
        sign_off_button.pack(pady=20)
        self.Tooltip(sign_off_button, "Cerrar Sesión")

    def show_add_entry_screen(self):
        self.clear_window()
        tk.Label(self, text="Agregar Nueva Entrada", font=("Helvetica", 16)).pack(pady=10)

        tk.Label(self, text="Fecha (YYYY-MM-DD)").pack()
        self.entry_fecha = tk.Entry(self)
        self.entry_fecha.pack(pady=5)

        tk.Label(self, text="Título").pack()
        self.entry_titulo = tk.Entry(self)
        self.entry_titulo.pack(pady=5)

        tk.Label(self, text="Contenido").pack()
        self.text_contenido = tk.Text(self, height=10, width=40)
        self.text_contenido.pack(pady=5)

        tk.Button(self, text="Agregar", command=self.logic.add_new_entry).pack(pady=20)
        tk.Button(self, text="Volver", command=self.show_main_menu).pack()

    def show_read_entries_screen(self):
        self.clear_window()
        tk.Label(self, text="Leer Entradas", font=("Helvetica", 16)).pack(pady=10)

        self.text_lectura = tk.Text(self, height=20, width=80)
        self.text_lectura.pack(pady=5)

        self.logic.read_entries()

        tk.Button(self, text="Volver", command=self.show_main_menu).pack(pady=20)

    def show_update_entry_screen(self):
        self.clear_window()
        tk.Label(self, text="Actualizar Entrada", font=("Helvetica", 16)).pack(pady=10)

        tk.Label(self, text="ID de la Entrada").pack()
        self.entry_id_actualizar = tk.Entry(self)
        self.entry_id_actualizar.pack(pady=5)

        tk.Label(self, text="Nuevo Título").pack()
        self.entry_nuevo_titulo = tk.Entry(self)
        self.entry_nuevo_titulo.pack(pady=5)

        tk.Label(self, text="Nuevo Contenido").pack()
        self.text_nuevo_contenido = tk.Text(self, height=10, width=40)
        self.text_nuevo_contenido.pack(pady=5)

        tk.Button(self, text="Actualizar", command=self.logic.update_selected_entry).pack(pady=20)
        tk.Button(self, text="Volver", command=self.show_main_menu).pack()

    def show_delete_entry_screen(self):
        self.clear_window()
        tk.Label(self, text="Eliminar Entrada", font=("Helvetica", 16)).pack(pady=10)

        tk.Label(self, text="ID de la Entrada").pack()
        self.entry_id_eliminar = tk.Entry(self)
        self.entry_id_eliminar.pack(pady=5)

        tk.Button(self, text="Eliminar", command=self.logic.delete_selected_entry).pack(pady=20)
        tk.Button(self, text="Volver", command=self.show_main_menu).pack()

    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()

    def set_image(self, widget, image_path, width, height):
        original_image = Image.open(image_path)
        resized_image = original_image.resize((width, height), Image.LANCZOS)
        photo_image = ImageTk.PhotoImage(resized_image)
        widget.config(image=photo_image)
        widget.image = photo_image 

    class Tooltip:
        def __init__(self, widget, text):
            self.widget = widget
            self.text = text
            self.tooltip_window = None
            widget.bind("<Enter>", self.show_tooltip)
            widget.bind("<Leave>", self.hide_tooltip)
        
        def show_tooltip(self, event):
            x = event.widget.winfo_rootx() + 0
            y = event.widget.winfo_rooty() + 27
            self.tooltip_window = tw = tk.Toplevel(event.widget)
            tw.wm_overrideredirect(True)
            tw.wm_geometry(f"+{x}+{y}")
            label = tk.Label(tw, text=self.text, fg="snow", font=("Roboto", 9, "bold"), bg="black", relief="solid", borderwidth=1)
            label.pack()
        
        def hide_tooltip(self, event):
            if self.tooltip_window:
                self.tooltip_window.destroy()
                self.tooltip_window = None

if __name__ == "__main__":
    app = App()
    app.mainloop()
