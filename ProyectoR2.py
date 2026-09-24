import json
import tkinter as tk
from pathlib import Path

# Los archivos de datos quedan junto a este programa, sin depender
# de la carpeta desde la que se ejecute.
ARCHIVO_JSON = Path(__file__).with_name("actividades.json")
ARCHIVO_ANTERIOR = Path(__file__).with_name("actividades.txt")

# Lista de actividades
actividades = []

# --- Funciones ---
def guardar(mostrar_mensaje=True):
    """Guarda las actividades actuales en formato JSON."""
    try:
        ARCHIVO_JSON.write_text(
            json.dumps(actividades, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        if mostrar_mensaje:
            lbl_info.config(text=f"Actividades guardadas en {ARCHIVO_JSON.name}.")
        return True
    except OSError as error:
        lbl_info.config(text=f"No se pudieron guardar las actividades: {error}")
        return False


def actualizar_lista():
    lista.delete(0, tk.END)
    for actividad in actividades:
        lista.insert(tk.END, actividad)


def cargar():
    """Carga el JSON; si no existe, importa el TXT usado por la versión anterior."""
    try:
        if ARCHIVO_JSON.exists():
            datos = json.loads(ARCHIVO_JSON.read_text(encoding="utf-8"))
            if not isinstance(datos, list) or not all(isinstance(act, str) for act in datos):
                raise ValueError("El archivo JSON debe contener una lista de actividades de texto.")
            origen = ARCHIVO_JSON.name
        elif ARCHIVO_ANTERIOR.exists():
            # Compatibilidad con los datos guardados por la versión anterior.
            datos = [linea.strip() for linea in ARCHIVO_ANTERIOR.read_text(encoding="utf-8").splitlines() if linea.strip()]
            origen = ARCHIVO_ANTERIOR.name
        else:
            actividades.clear()
            actualizar_lista()
            lbl_info.config(text="No hay archivo guardado todavía.")
            return

        actividades.clear()
        actividades.extend(datos)
        actualizar_lista()
        # Convierte también los datos antiguos al nuevo formato JSON.
        if origen == ARCHIVO_ANTERIOR.name:
            guardar(mostrar_mensaje=False)
        lbl_info.config(text=f"Actividades cargadas desde {origen}.")
    except (OSError, json.JSONDecodeError, ValueError) as error:
        lbl_info.config(text=f"No se pudieron cargar las actividades: {error}")


def agregar():
    nombre = entrada.get().strip()
    prioridad = prioridad_var.get()
    if nombre:
        actividad = f"{nombre} [Prioridad: {prioridad}]"
        actividades.append(actividad)
        actualizar_lista()
        entrada.delete(0, tk.END)
        if guardar(mostrar_mensaje=False):
            lbl_info.config(text=f"Actividad agregada.\nTotal: {len(actividades)}")
    else:
        lbl_info.config(text="Escribe una actividad antes de agregar")


def eliminar():
    seleccion = lista.curselection()
    if seleccion:
        index = seleccion[0]
        actividad_eliminada = actividades.pop(index)
        actualizar_lista()
        if guardar(mostrar_mensaje=False):
            lbl_info.config(text=f"Actividad eliminada.\nTotal: {len(actividades)}")
        else:
            actividades.insert(index, actividad_eliminada)
            actualizar_lista()
    else:
        lbl_info.config(text="Selecciona una actividad para eliminar")


def completar():
    seleccion = lista.curselection()
    if seleccion:
        index = seleccion[0]
        actividad_anterior = actividades[index]
        if "Completada" not in actividad_anterior:
            actividades[index] = actividad_anterior + " ✔ Completada"
            if guardar(mostrar_mensaje=False):
                actualizar_lista()
                lista.selection_set(index)
                lbl_info.config(text="Actividad marcada como completada")
            else:
                actividades[index] = actividad_anterior
                actualizar_lista()
        else:
            lbl_info.config(text="La actividad ya está marcada como completada")
    else:
        lbl_info.config(text="Selecciona una actividad para completar")


def mostrar():
    if actividades:
        lbl_info.config(text="Actividades:\n" + "\n".join(actividades))
    else:
        lbl_info.config(text="No hay actividades registradas")


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

# Recupera automáticamente las actividades al iniciar.
cargar()
ventana.mainloop()
