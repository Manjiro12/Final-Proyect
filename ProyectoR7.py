import tkinter as tk

actividades = []

def agregar():
    nombre = entrada.get()
    if nombre:
        actividades.append(nombre)
        lista.insert(tk.END, nombre)
        entrada.delete(0, tk.END)

def eliminar():
    seleccion = lista.curselection()
    if seleccion:
        index = seleccion[0]
        lista.delete(index)
        actividades.pop(index)

def mostrar():
    if actividades:
        lbl_info.config(text="Actividades:\n" + "\n".join(actividades))
    else:
        lbl_info.config(text="No hay actividades registradas")

# Ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Actividades")
ventana.geometry("400x400")
ventana.config(bg="#f0f0f0")  # Fondo gris claro

# Título
lbl_titulo = tk.Label(ventana, text="Gestor de Actividades", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#2c3e50")
lbl_titulo.pack(pady=10)

# Entrada de texto
entrada = tk.Entry(ventana, width=30, font=("Arial", 12))
entrada.pack(pady=5)

# Botones con estilo
btn_agregar = tk.Button(ventana, text="Agregar Actividad", command=agregar, bg="#3498db", fg="white", font=("Arial", 11))
btn_agregar.pack(pady=5)

btn_eliminar = tk.Button(ventana, text="Eliminar Seleccionada", command=eliminar, bg="#e74c3c", fg="white", font=("Arial", 11))
btn_eliminar.pack(pady=5)

btn_mostrar = tk.Button(ventana, text="Mostrar Actividades", command=mostrar, bg="#2ecc71", fg="white", font=("Arial", 11))
btn_mostrar.pack(pady=5)

# Lista visual
lista = tk.Listbox(ventana, width=40, font=("Arial", 11))
lista.pack(pady=10)

# Etiqueta de información
lbl_info = tk.Label(ventana, text="Aquí aparecerá la información", font=("Arial", 11), bg="#f0f0f0", fg="#34495e")
lbl_info.pack(pady=10)

ventana.mainloop()
