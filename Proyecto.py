import tkinter as tk
from tkinter import ttk
#Librería para obtener la fecha actual
from datetime import date 

# Ventana principal
root = tk.Tk()
root.title("Registro de Actividades Diarias")
root.geometry("500x600")

# Notebook (contenedor de pestañas)
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True, padx=10, pady=10)

# Frame para cada pestaña
tab_hoy = ttk.Frame(notebook)
tab_historial = ttk.Frame(notebook)
tab_recomendaciones = ttk.Frame(notebook)

# Agregar las pestañas al notebook con su nombre visible
notebook.add(tab_hoy, text="Hoy")
# Agregamos la fecha actual dentro de la pestaña hoy#
# Date es la clase | today() es un método que devuelve la fecha actual | strftime() Es un método que toma ese objeto fecha y lo convierte en un string (texto) legible
#%d/%m/%Y es el formato de fecha que queremos mostrar (día/mes/año)
fecha_actual = date.today().strftime("%d/%m/%Y")
#Crea un texto (Label) dentro de la pestaña "Hoy" que muestra "Actividades del día:" seguido de la fecha actual, en Arial 12 negrita.
label_fecha = ttk.Label(tab_hoy, text=f"Actividades del día : {fecha_actual}", font=("Arial", 14, "bold"))
#dibuja ese texto en pantalla, dejando 10px de espacio vertical arriba y abajo.
label_fecha.pack(pady=10)
#Nombre de variable que contiene la lista de actividades
list_actividades = ["Leer" , "Ejercicio", "Trabajo", "Estudiar"]
#Diccionario para guardar la variable boolean de cada actividad (si está seleccionada o no)
variables_actividades = {}
#Frame para contener los checkboxes
frame_checkboxes = ttk.Frame(tab_hoy)
frame_checkboxes.pack(fill="both", expand=True, padx=10, pady=10)
#Creación de checkboxes para cada actividad en la lista con un for 
for actividad in list_actividades:
    var = tk.BooleanVar()  # Variable booleana para cada checkbox
    checkbox = ttk.Checkbutton(frame_checkboxes, text=actividad, variable=var)
    checkbox.pack(anchor="w", pady=5)  # Alinea a la izquierda y agrega espacio vertical
    variables_actividades[actividad] = var  # Guardar la variable en el dic
notebook.add(tab_historial, text="Historial")

notebook.add(tab_recomendaciones, text="Recomendaciones")

# Bucle principal (mantiene la ventana abierta)
root.mainloop()