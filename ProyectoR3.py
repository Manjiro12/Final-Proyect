import tkinter as tk
from tkinter import ttk
from datetime import datetime

# Lista de actividades
actividades = []

def agregar():
    nombre = entrada.get()
    prioridad = prioridad_var.get()
    categoria = categoria_var.get()
    fecha = fecha_var.get()

    if nombre:
        actividad = {
            "tarea": nombre,
            "prioridad": prioridad,
            "categoria": categoria,
            "fecha": fecha,
            "estado": "Pendiente"
        }
        actividades.append(actividad)
        mostrar_lista()
        entrada.delete(0, tk.END)
        lbl_info.config(text=f"Actividad agregada.\nTotal: {len(actividades)}")
    else:
        lbl_info.config(text="Escribe una actividad antes de agregar")

def eliminar():
    seleccion = lista.curselection()
    if seleccion:
        index = seleccion[0]
        actividades.pop(index)
        mostrar_lista()
        lbl_info.config(text=f"Actividad eliminada.\nTotal: {len(actividades)}")
    else:
        lbl_info.config(text="Selecciona una actividad para eliminar")

def completar():
    seleccion = lista.curselection()
    if seleccion:
        index = seleccion[0]
        actividades[index]["estado"] = "Completada"
        mostrar_lista()
        lbl_info.config(text="Actividad marcada como completada")
    else:
        lbl_info.config(text="Selecciona una actividad para completar")

def mostrar():
    if actividades:
        texto = ""
        for act in actividades:
            texto += f"{act['tarea']} ({act['categoria']}, {act['prioridad']}, {act['fecha']}) → {act['estado']}\n"
        lbl_info.config(text=texto)
    else:
        lbl_info.config(text="No hay actividades registradas")

def resumen():
    pendientes = sum(1 for act in actividades if act["estado"] == "Pendiente")
    completadas = sum(1 for act in actividades if act["estado"] == "Completada")
    lbl_info.config(text=f"Pendientes: {pendientes}\nCompletadas: {completadas}")

def mostrar_lista():
    lista.delete(0, tk.END)
    for act in actividades:
        texto = f"{act['tarea']} [{act['prioridad']}] ({act['categoria']}) - {act['estado']}"
        lista.insert(tk.END, texto)
        # Colores según estado/prioridad
        if act["estado"] == "Completada":
            lista.itemconfig(tk.END, {'fg': 'green'})
        elif act["prioridad"] == "Alta":
            lista.itemconfig(tk.END, {'fg': 'orange'})
        else:
            lista.itemconfig(tk.END, {'fg': 'red'})

# --- Ventana principal ---
ventana = tk.Tk()
ventana.title("Gestión de Actividades Avanzada")

# Entrada de texto
entrada = tk.Entry(ventana, width=40)
entrada.pack(pady=5)

# Menú desplegable de prioridad
prioridad_var = tk.StringVar(value="Media")
opciones_prioridad = ["Alta", "Media", "Baja"]
menu_prioridad = tk.OptionMenu(ventana, prioridad_var, *opciones_prioridad)
menu_prioridad.pack(pady=5)

# Menú desplegable de categoría
categoria_var = tk.StringVar(value="Personal")
opciones_categoria = ["Escuela", "Trabajo", "Personal"]
menu_categoria = tk.OptionMenu(ventana, categoria_var, *opciones_categoria)
menu_categoria.pack(pady=5)

# Campo de fecha límite
fecha_var = tk.StringVar(value=datetime.now().strftime("%d/%m/%Y"))
lbl_fecha = tk.Label(ventana, text="Fecha límite (dd/mm/yyyy):")
lbl_fecha.pack()
entrada_fecha = tk.Entry(ventana, textvariable=fecha_var, width=20)
entrada_fecha.pack(pady=5)

# Botones principales
btn_agregar = tk.Button(ventana, text="Agregar Actividad", command=agregar)
btn_agregar.pack(pady=5)

btn_eliminar = tk.Button(ventana, text="Eliminar Actividad", command=eliminar)
btn_eliminar.pack(pady=5)

btn_completar = tk.Button(ventana, text="Marcar como Completada", command=completar)
btn_completar.pack(pady=5)

btn_mostrar = tk.Button(ventana, text="Mostrar Actividades", command=mostrar)
btn_mostrar.pack(pady=5)

btn_resumen = tk.Button(ventana, text="Resumen del Día", command=resumen)
btn_resumen.pack(pady=5)

# Lista de actividades
lista = tk.Listbox(ventana, width=70, height=10)
lista.pack(pady=10)

# Etiqueta de información
lbl_info = tk.Label(ventana, text="Aquí aparecerá la información")
lbl_info.pack(pady=20)

ventana.mainloop()
