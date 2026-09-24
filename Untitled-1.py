import tkinter as tk   
from tkinter import ttk

#Ventana principal
root = tk.Tk() 
root.title("Registro de Actividades Diarias")   
root.geometry("500x600")

#Notebook(contenedor de pestañas)
notebook = ttk.Notebook(root)
notebook.pack(padx=10, pady=10, fill="both", expand=True)

#frame para cada pestaña 
tab_hoy = ttk.Frame(notebook)
tab_historial = ttk.Frame(notebook)
tab_recomendaciones = ttk.Frame(notebook)

#Agregar pestañas al notebook con su nombre visible
notebook.add(tab_hoy, text="Hoy")
notebook.add(tab_historial, text="Historial")
notebook.add(tab_recomendaciones, text="Recomendaciones")

root.mainloop