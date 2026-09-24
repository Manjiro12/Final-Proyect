import tkinter as tk

# Lista de actividades
actividades = []

# --- Funciones ---
def agregar():
    nombre = entrada.get()
    prioridad = prioridad_var.get()  # Tomamos la prioridad seleccionada
    if nombre:
        actividad = f"{nombre} [Prioridad: {prioridad}]"
        actividades.append(actividad)
        lista.insert(tk.END, actividad)
        entrada.delete(0, tk.END)
        lbl_info.config(text=f"Actividad agregada.\nTotal: {len(actividades)}")
    else:
        lbl_info.config(text="Escribe una actividad antes de agregar")

def eliminar():
    seleccion = lista.curselection()
    if seleccion:
        index = seleccion[0]
        lista.delete(index)
        actividades.pop(index)
        lbl_info.config(text=f"Actividad eliminada.\nTotal: {len(actividades)}")
    else:
        lbl_info.config(text="Selecciona una actividad para eliminar")

def completar():
    seleccion = lista.curselection()
    if seleccion:
        index = seleccion[0]
        actividades[index] = actividades[index] + " ✔ Completada"
        lista.delete(index)
        lista.insert(index, actividades[index])
        lbl_info.config(text="Actividad marcada como completada")
    else:
        lbl_info.config(text="Selecciona una actividad para completar")

def mostrar():
    if actividades:
        lbl_info.config(text="Actividades:\n" + "\n".join(actividades))
    else:
        lbl_info.config(text="No hay actividades registradas")

def guardar():
    with open("actividades.txt", "w") as f:
        for act in actividades:
            f.write(act + "\n")
    lbl_info.config(text="Actividades guardadas en archivo.")

def cargar():
    try:
        with open("actividades.txt", "r") as f:
            actividades.clear()
            lista.delete(0, tk.END)
            for linea in f:
                act = linea.strip()
                actividades.append(act)
                lista.insert(tk.END, act)
        lbl_info.config(text="Actividades cargadas desde archivo.")
    except FileNotFoundError:
        lbl_info.config(text="No hay archivo guardado todavía.")

def resumen():
    pendientes = sum(1 for act in actividades if "Completada" not in act)
    completadas = sum(1 for act in actividades if "Completada" in act)
    lbl_info.config(text=f"Pendientes: {pendientes}\nCompletadas: {completadas}")

# --- Ventana principal ---
ventana = tk.Tk()
ventana.title("Gestión de Actividades Diarias")

# Entrada de texto
entrada = tk.Entry(ventana, width=40)
entrada.pack(pady=5)

# Menú desplegable de prioridad
prioridad_var = tk.StringVar(value="Media")
opciones_prioridad = ["Alta", "Media", "Baja"]
menu_prioridad = tk.OptionMenu(ventana, prioridad_var, *opciones_prioridad)
menu_prioridad.pack(pady=5)

# Botones principales
btn_agregar = tk.Button(ventana, text="Agregar Actividad", command=agregar)
btn_agregar.pack(pady=5)

btn_eliminar = tk.Button(ventana, text="Eliminar Actividad", command=eliminar)
btn_eliminar.pack(pady=5)

btn_completar = tk.Button(ventana, text="Marcar como Completada", command=completar)
btn_completar.pack(pady=5)

btn_mostrar = tk.Button(ventana, text="Mostrar Actividades", command=mostrar)
btn_mostrar.pack(pady=5)

btn_guardar = tk.Button(ventana, text="Guardar Actividades", command=guardar)
btn_guardar.pack(pady=5)

btn_cargar = tk.Button(ventana, text="Cargar Actividades", command=cargar)
btn_cargar.pack(pady=5)

btn_resumen = tk.Button(ventana, text="Resumen del Día", command=resumen)
btn_resumen.pack(pady=5)

# Lista de actividades
lista = tk.Listbox(ventana, width=50, height=10)
lista.pack(pady=10)

# Etiqueta de información
lbl_info = tk.Label(ventana, text="Aquí aparecerá la información")
lbl_info.pack(pady=20)

ventana.mainloop()

