from tkinter import PhotoImage, ttk, messagebox, Toplevel, W, Tk, Scrollbar, Button, Frame, Entry, Label, END
import csv

class GestorLibros:
    def __init__(self, archivo):
        self.archivo = archivo

    def agregar_libro(self, libro):
        with open(self.archivo, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(libro)

    def mostrar_libros(self):
        with open(self.archivo, 'r') as file:
            reader = csv.reader(file)
            return list(reader)

    def borrar_libro(self, libro_a_borrar):
        with open(self.archivo, 'r') as file:
            reader = csv.reader(file)
            libros = list(reader)
        indice = None
        for i, row in enumerate(libros):
            if [str(value).strip().lower() for value in row] == [str(value).strip().lower() for value in libro_a_borrar]:
                indice = i
                break
        if indice is not None:
            libros.pop(indice)
            with open(self.archivo, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(libros)
            return True
        return False

    def editar_libro(self, libro_original, nuevos_datos):
        with open(self.archivo, 'r') as file:
            reader = csv.reader(file)
            libros = list(reader)
        with open(self.archivo, 'w', newline='') as file:
            writer = csv.writer(file)
            for row in libros:
                if [str(value).strip().lower() for value in row] == [str(value).strip().lower() for value in libro_original]:
                    writer.writerow(nuevos_datos)
                else:
                    writer.writerow(row)

class BibliotecaApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestión de Biblioteca")
        # Cambiar el ícono de la ventana
        self.master.iconphoto(False, PhotoImage(file='icono.png'))
        self.master.configure(bg='#e0e0e0')
        # Configuración del estilo
        s = ttk.Style()
        s.theme_use('clam')
        # Inicializar el gestor de libros
        self.gestor_libros = GestorLibros('library.csv')
        # Crear un marco para los campos de entrada
        self.frame_campos = Frame(master, bg='#e0e0e0')
        self.frame_campos.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        # Crear etiquetas y campos de entrada
        self.crear_campos_entrada()
        # Crear un marco para los botones
        self.frame_botones = Frame(master, bg='#e0e0e0')
        self.frame_botones.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        # Crear botones
        self.crear_botones()
        # Crear un marco para el Treeview y el Scrollbar
        self.frame_treeview = Frame(master)
        self.frame_treeview.grid(row=2, column=0, columnspan=2, sticky='nsew', padx=10, pady=10)
        # Crear el Treeview
        self.tree = ttk.Treeview(self.frame_treeview, columns=(1, 2, 3, 4), show="headings")
        self.tree.tag_configure('evenrow', background='#f0f0f0')
        self.tree.tag_configure('oddrow', background='#ffffff')
        self.tree.grid(row=0, column=0, sticky='nsew')
        # Crear el Scrollbar
        self.scrollbar = Scrollbar(self.frame_treeview, orient="vertical", command=self.tree.yview)
        self.scrollbar.grid(row=0, column=1, sticky='ns')
        # Asociar el Scrollbar con el Treeview
        self.tree.configure(yscrollcommand=self.scrollbar.set)
        # Configurar los encabezados del Treeview
        self.configurar_encabezados()
        # Mostrar libros existentes al iniciar el programa
        self.mostrar_libros()

    def crear_campos_entrada(self):
        labels = ["Nombre:", "Autor:", "Género:", "Año:"]
        self.entries = []
        for i, label in enumerate(labels):
            Label(self.frame_campos, text=label, bg='#e0e0e0').grid(row=i, column=0, padx=5, pady=5, sticky=W)
            entry = Entry(self.frame_campos)
            entry.grid(row=i, column=1, padx=5, pady=5)
            self.entries.append(entry)

    def crear_botones(self):
        Button(self.frame_botones, text="Agregar Libro", command=self.agregar_libro).grid(row=0, column=0, padx=10, pady=10)
        Button(self.frame_botones, text="Borrar Libro", command=self.borrar_libro).grid(row=0, column=1, padx=10, pady=10)
        Button(self.frame_botones, text="Editar Libro", command=self.editar_libro).grid(row=0, column=2, padx=10, pady=10)

    def configurar_encabezados(self):
        self.tree.heading(1, text="Nombre", anchor="w")
        self.tree.heading(2, text="Autor", anchor="w")
        self.tree.heading(3, text="Género", anchor="w")
        self.tree.heading(4, text="Año", anchor="w")
        self.frame_treeview.grid_rowconfigure(0, weight=1)
        self.frame_treeview.grid_columnconfigure(0, weight=1)

    def agregar_libro(self):
        nombre = self.entries[0].get().title()  # Convertir a formato Title Case
        autor = self.entries[1].get().title()   # Convertir a formato Title Case
        genero = self.entries[2].get().title()   # Convertir a formato Title Case
        año = self.entries[3].get()               # El año puede mantenerse como está
        if nombre and autor and genero and año:
            self.gestor_libros.agregar_libro([nombre, autor, genero, año])
            self.limpiar_campos()
            self.mostrar_libros()
        else:
            messagebox.showerror("Error", "Por favor, completa todos los campos.")

    def limpiar_campos(self):
        for entry in self.entries:
            entry.delete(0, END)

    def mostrar_libros(self):
        self.tree.delete(*self.tree.get_children())
        libros = self.gestor_libros.mostrar_libros()
        for row in libros:
            self.tree.insert("", "end", values=row)

    def borrar_libro(self):
        selected_item = self.tree.selection()
        if selected_item:
            for item in selected_item:
                libro_a_borrar = self.tree.item(item)['values']
                if self.gestor_libros.borrar_libro(libro_a_borrar):
                    self.mostrar_libros()
                else:
                    messagebox.showwarning("Advertencia", "Libro no encontrado.")
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona un libro para borrar.")

    def editar_libro(self):
        selected_item = self.tree.selection()
        if selected_item:
            for item in selected_item:
                libro = self.tree.item(item)['values']
                ventana_editar = Toplevel(self.master)
                ventana_editar.title("Editar Libro")
                ventana_editar.geometry("200x180")
                entries_editar = []
                for i, value in enumerate(libro):
                    Label(ventana_editar, text=["Nombre:", "Autor:", "Género:", "Año:"][i]).grid(row=i, column=0, padx=5, pady=5)
                    entry = Entry(ventana_editar)
                    entry.grid(row=i, column=1, padx=5, pady=5)
                    entry.insert(0, value)
                    entries_editar.append(entry)
                boton_guardar = Button(ventana_editar, text="Guardar Cambios", command=lambda: self.guardar_cambios(libro, entries_editar, ventana_editar))
                boton_guardar.grid(row=4, columnspan=2, padx=10, pady=10)

    def guardar_cambios(self, libro, entries_editar, ventana_editar):
        nuevos_datos = [entry.get().title() for entry in entries_editar]  # Convertir a formato Title Case
        if all(nuevos_datos):
            self.gestor_libros.editar_libro(libro, nuevos_datos)
            ventana_editar.destroy()
            self.mostrar_libros()
        else:
            messagebox.showerror("Error", "Por favor, completa todos los campos.")

def main():
    root = Tk()
    app = BibliotecaApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()