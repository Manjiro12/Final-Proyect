# Biblioteca para la interfaz gráfica
import tkinter as tk

# Ventanas emergentes de confirmación
from tkinter import messagebox

# Obtener fecha y hora actual
from datetime import datetime

# Manejo de archivos
from pathlib import Path


# ==================================================
# VARIABLES GENERALES
# ==================================================

# Lista donde se almacenan las actividades
actividades = []

# Archivo donde se guardarán las actividades
archivo = Path("actividades.txt")


# ==================================================
# FUNCIÓN: GUARDAR ACTIVIDADES
# ==================================================
def guardar_actividades():

    # Guarda todas las actividades en un archivo
    archivo.write_text(
        "\n".join(actividades),
        encoding="utf-8"
    )


# ==================================================
# FUNCIÓN: ACTUALIZAR ESTADÍSTICAS
# ==================================================
def actualizar_estadisticas():

    # Total de actividades
    total = len(actividades)

    # Contador de completadas
    completadas = 0

    for actividad in actividades:
        if actividad.startswith("✅"):
            completadas += 1

    # Contador de pendientes
    pendientes = total - completadas

    # Actualizar etiquetas
    lbl_total.config(text=f"📋 Total: {total}")
    lbl_pendientes.config(text=f"⏳ Pendientes: {pendientes}")
    lbl_completadas.config(text=f"✅ Completadas: {completadas}")

    # Calcular porcentaje
    if total > 0:
        porcentaje = int((completadas / total) * 100)
    else:
        porcentaje = 0

    # Actualizar barra de progreso
    canvas.coords(
        barra,
        0,
        0,
        porcentaje * 2,
        20
    )

    # Mostrar porcentaje
    lbl_progreso.config(
        text=f"Avance: {porcentaje}%"
    )


# ==================================================
# FUNCIÓN: CARGAR ACTIVIDADES
# ==================================================
def cargar_actividades():

    # Verifica que exista el archivo
    if archivo.exists():

        # Leer todas las líneas
        datos = archivo.read_text(
            encoding="utf-8"
        ).splitlines()

        # Agregar actividades recuperadas
        for actividad in datos:

            actividades.append(actividad)

            lista.insert(
                tk.END,
                actividad
            )

    # Actualizar estadísticas
    actualizar_estadisticas()


# ==================================================
# FUNCIÓN: AGREGAR ACTIVIDAD
# ==================================================
def agregar():

    # Obtener texto escrito
    nombre = entrada.get().strip()

    # Evitar campos vacíos
    if nombre == "":
        return

    # Obtener fecha y hora actual
    fecha = datetime.now().strftime(
        "%d/%m/%Y %H:%M"
    )

    # Construir actividad
    nueva_actividad = f"[{fecha}] {nombre}"

    # Guardar en lista
    actividades.append(nueva_actividad)

    # Mostrar en pantalla
    lista.insert(
        tk.END,
        nueva_actividad
    )

    # Limpiar caja de texto
    entrada.delete(0, tk.END)

    # Guardar cambios
    guardar_actividades()

    # Actualizar datos
    actualizar_estadisticas()


# ==================================================
# FUNCIÓN: ELIMINAR ACTIVIDAD
# ==================================================
def eliminar():

    # Obtener selección
    seleccion = lista.curselection()

    # Si no seleccionó nada
    if not seleccion:
        return

    # Confirmación
    confirmar = messagebox.askyesno(
        "Eliminar",
        "¿Deseas eliminar esta actividad?"
    )

    if confirmar:

        # Índice seleccionado
        indice = seleccion[0]

        # Eliminar de pantalla
        lista.delete(indice)

        # Eliminar de memoria
        actividades.pop(indice)

        # Guardar cambios
        guardar_actividades()

        # Actualizar estadísticas
        actualizar_estadisticas()


# ==================================================
# FUNCIÓN: MARCAR COMO COMPLETADA
# ==================================================
def completar():

    # Obtener selección
    seleccion = lista.curselection()

    if not seleccion:
        return

    indice = seleccion[0]

    actividad = actividades[indice]

    # Evitar marcar dos veces
    if not actividad.startswith("✅"):

        actividad = "✅ " + actividad

        actividades[indice] = actividad

        lista.delete(indice)

        lista.insert(indice, actividad)

        guardar_actividades()

        actualizar_estadisticas()


# ==================================================
# FUNCIÓN: MOSTRAR RESUMEN
# ==================================================
def mostrar():

    if actividades:

        lbl_info.config(
            text=f"Actualmente existen {len(actividades)} actividades registradas."
        )

    else:

        lbl_info.config(
            text="No existen actividades registradas."
        )


# ==================================================
# CREACIÓN DE LA VENTANA PRINCIPAL
# ==================================================

ventana = tk.Tk()

# Título de la aplicación
ventana.title("TASKMASTER PRO")

# Tamaño
ventana.geometry("1000x650")

# Fondo principal
ventana.configure(bg="#121826")


# ==================================================
# ENCABEZADO
# ==================================================

titulo = tk.Label(
    ventana,
    text="📋 SGA ",
    font=("Segoe UI", 24, "bold"),
    bg="#121826",
    fg="white"
)

titulo.pack(pady=10)

subtitulo = tk.Label(
    ventana,
    text="Sistema Inteligente de Gestión de Actividades",
    font=("Segoe UI", 11),
    bg="#121826",
    fg="#94A3B8"
)

subtitulo.pack()


# ==================================================
# FRAME PRINCIPAL
# ==================================================

contenedor = tk.Frame(
    ventana,
    bg="#1E293B"
)

contenedor.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=20
)


# ==================================================
# PANEL IZQUIERDO
# ==================================================

panel_izquierdo = tk.Frame(
    contenedor,
    bg="#1E293B"
)

panel_izquierdo.pack(
    side="left",
    fill="y",
    padx=15
)


# Caja de texto
entrada = tk.Entry(
    panel_izquierdo,
    width=30,
    font=("Segoe UI", 12)
)

entrada.pack(pady=10)


# Botón agregar
btn_agregar = tk.Button(
    panel_izquierdo,
    text="➕ Agregar",
    command=agregar,
    bg="#22C55E",
    fg="white"
)

btn_agregar.pack(fill="x", pady=5)


# Botón eliminar
btn_eliminar = tk.Button(
    panel_izquierdo,
    text="🗑 Eliminar",
    command=eliminar,
    bg="#EF4444",
    fg="white"
)

btn_eliminar.pack(fill="x", pady=5)


# Botón completar
btn_completar = tk.Button(
    panel_izquierdo,
    text="✅ Completar",
    command=completar,
    bg="#F59E0B",
    fg="white"
)

btn_completar.pack(fill="x", pady=5)


# Botón mostrar
btn_mostrar = tk.Button(
    panel_izquierdo,
    text="📄 Mostrar",
    command=mostrar,
    bg="#3B82F6",
    fg="white"
)

btn_mostrar.pack(fill="x", pady=5)


# ==================================================
# ESTADÍSTICAS
# ==================================================

lbl_total = tk.Label(
    panel_izquierdo,
    text="📋 Total: 0",
    bg="#1E293B",
    fg="white"
)

lbl_total.pack(anchor="w", pady=2)

lbl_pendientes = tk.Label(
    panel_izquierdo,
    text="⏳ Pendientes: 0",
    bg="#1E293B",
    fg="white"
)

lbl_pendientes.pack(anchor="w", pady=2)

lbl_completadas = tk.Label(
    panel_izquierdo,
    text="✅ Completadas: 0",
    bg="#1E293B",
    fg="white"
)

lbl_completadas.pack(anchor="w", pady=2)


# ==================================================
# BARRA DE PROGRESO
# ==================================================

canvas = tk.Canvas(
    panel_izquierdo,
    width=200,
    height=20,
    bg="#0F172A",
    highlightthickness=0
)

canvas.pack(pady=10)

barra = canvas.create_rectangle(
    0,
    0,
    0,
    20,
    fill="#22C55E"
)

lbl_progreso = tk.Label(
    panel_izquierdo,
    text="Avance: 0%",
    bg="#1E293B",
    fg="white"
)

lbl_progreso.pack()


# ==================================================
# PANEL DERECHO
# ==================================================

panel_derecho = tk.Frame(
    contenedor,
    bg="#E2E8F0"
)

panel_derecho.pack(
    side="right",
    fill="both",
    expand=True
)


# Lista donde se muestran las actividades
lista = tk.Listbox(
    panel_derecho,
    font=("Segoe UI", 11)
)

lista.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=10
)


# Mensajes informativos
lbl_info = tk.Label(
    panel_derecho,
    text="Bienvenido a TaskMaster Pro",
    bg="#E2E8F0",
    fg="#334155"
)

lbl_info.pack(pady=10)


# ==================================================
# CARGA INICIAL DE DATOS
# ==================================================

cargar_actividades()


# ==================================================
# INICIAR APLICACIÓN
# ==================================================

ventana.mainloop()