import tkinter as tk
from servicios.tarea_servicio import TareaServicio
from ui.app_tkinter import AppTkinter


def main():
    servicio = TareaServicio()
    root = tk.Tk()
    app = AppTkinter(root, servicio)
    app.iniciar()


if __name__ == "__main__":
    main()