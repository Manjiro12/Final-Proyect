import tkinter as tk   # Importamos la librería Tkinter para crear la interfaz gráfica

# Lista donde se guardarán las actividades
actividades = []

# Función para agregar una actividad escrita en el cuadro de texto
def agregar():
    nombre = entrada.get()  # Obtiene el texto escrito en la caja de entrada
    if nombre:              # Verifica que no esté vacío
        actividades.append(nombre)          # Lo agrega a la lista de actividades
        lista.insert(tk.END, nombre)        # Lo muestra en la lista visual
        entrada.delete(0, tk.END)           # Limpia el cuadro de texto

# Función para eliminar la actividad seleccionada en la lista
def eliminar():
    seleccion = lista.curselection()  # Obtiene el índice de la actividad seleccionada
    if seleccion:
        index = seleccion[0]          # Toma el primer índice seleccionado
        lista.delete(index)           # Elimina de la lista visual
        actividades.pop(index)        # Elimina de la lista interna

# Función para mostrar todas las actividades en la etiqueta de información
def mostrar():
    if actividades:
        lbl_info.config(text="Actividades:\n" + "\n".join(actividades))  # Muestra todas
    else:
        lbl_info.config(text="No hay actividades registradas")           # Mensaje si está vacío

# Creación de la ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Actividades")   # Título de la ventana
ventana.geometry("650x400")              # Tamaño de la ventana
ventana.config(bg="#2c3e50")             # Color de fondo (oscuro elegante)

# Etiqueta de título principal
lbl_titulo = tk.Label(
    ventana, 
    text="Gestor de Actividades", 
    font=("Arial", 20, "bold"), 
    bg="#2c3e50", 
    fg="white"
)
lbl_titulo.pack(pady=15)   # Se coloca arriba con espacio

# Frame principal que contendrá los paneles
frame = tk.Frame(ventana, bg="#34495e")
frame.pack(fill="both", expand=True, padx=20, pady=10)

# Panel izquierdo para los botones y entrada de texto
panel_botones = tk.Frame(frame, bg="#34495e")
panel_botones.pack(side="left", fill="y", padx=15)

# Caja de texto para escribir el nombre de la actividad
entrada = tk.Entry(panel_botones, width=25, font=("Arial", 12))
entrada.pack(pady=5)

# Botón para agregar actividad
btn_agregar = tk.Button(
    panel_botones, 
    text="➕ Agregar", 
    command=agregar, 
    bg="#27ae60", 
    fg="white", 
    font=("Arial", 11)
)
btn_agregar.pack(pady=5, fill="x")

# Botón para eliminar actividad seleccionada
btn_eliminar = tk.Button(
    panel_botones, 
    text="🗑️ Eliminar", 
    command=eliminar, 
    bg="#c0392b", 
    fg="white", 
    font=("Arial", 11)
)
btn_eliminar.pack(pady=5, fill="x")

# Botón para mostrar todas las actividades
btn_mostrar = tk.Button(
    panel_botones, 
    text="📋 Mostrar", 
    command=mostrar, 
    bg="#2980b9", 
    fg="white", 
    font=("Arial", 11)
)
btn_mostrar.pack(pady=5, fill="x")

# Panel derecho para la lista de actividades
panel_lista = tk.Frame(frame, bg="#ecf0f1")
panel_lista.pack(side="right", fill="both", expand=True)

# Lista visual donde se mostrarán las actividades
lista = tk.Listbox(panel_lista, width=40, font=("Arial", 12), bg="#ecf0f1", fg="#2c3e50")
lista.pack(pady=10, fill="both", expand=True)

# Etiqueta para mostrar información adicional
lbl_info = tk.Label(panel_lista, text="Aquí aparecerá la información", font=("Arial", 11), bg="#ecf0f1", fg="#34495e")
lbl_info.pack(pady=10)

# Mantiene la ventana abierta y esperando interacción
ventana.mainloop()
