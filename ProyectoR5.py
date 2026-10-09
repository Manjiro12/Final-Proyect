import tkinter as tk

# Lista de actividades
actividades = []

def agregar():
    nombre = entrada.get()
    if nombre:  # Solo agrega si hay texto
        actividades.append(nombre)
        lista.insert(tk.END, nombre)  # Lo muestra en la lista
        entrada.delete(0, tk.END)     # Limpia el cuadro de texto

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
ventana.title("Gestión de Actividades")

# Cuadro de texto para escribir la actividad
entrada = tk.Entry(ventana, width=40)
entrada.pack(pady=5)

btn_agregar = tk.Button(ventana, text="Agregar Actividad", command=agregar)
btn_agregar.pack(pady=5)

btn_eliminar = tk.Button(ventana, text="Eliminar Seleccionada", command=eliminar)
btn_eliminar.pack(pady=5)

btn_mostrar = tk.Button(ventana, text="Mostrar Actividades", command=mostrar)
btn_mostrar.pack(pady=5)

# Lista visual de actividades
lista = tk.Listbox(ventana, width=40)
lista.pack(pady=10)

# Etiqueta para mostrar información
lbl_info = tk.Label(ventana, text="Aquí aparecerá la información")
lbl_info.pack(pady=10)

ventana.mainloop()
