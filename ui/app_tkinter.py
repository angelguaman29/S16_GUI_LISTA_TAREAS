import tkinter as tk
from tkinter import messagebox
from servicios.tarea_servicio import TareaServicio


class AppTkinter:
    def __init__(self, root: tk.Tk, servicio: TareaServicio):
        self.root = root
        self.servicio = servicio
        self._configurar_ventana()
        self._construir_ui()
        self._registrar_atajos()

    # ── Configuración ──────────────────────────────────────────────
    def _configurar_ventana(self):
        self.root.title("Lista de Tareas – S16")
        self.root.geometry("520x480")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e2e")

    # ── Construcción de la UI ───────────────────────────────────────
    def _construir_ui(self):
        COLOR_BG      = "#1e1e2e"
        COLOR_PANEL   = "#2a2a3e"
        COLOR_ACCENT  = "#7c6af7"
        COLOR_BTN_OK  = "#3ddc84"
        COLOR_BTN_DEL = "#f28b82"
        COLOR_BTN_COM = "#ffb74d"
        COLOR_TEXT    = "#cdd6f4"

        # Título
        tk.Label(
            self.root, text="📋 Lista de Tareas",
            font=("Segoe UI", 16, "bold"),
            bg=COLOR_BG, fg=COLOR_ACCENT
        ).pack(pady=(18, 6))

        # Leyenda de atajos
        leyenda = (
            "Enter: Agregar  |  C: Completar  |  "
            "Delete / D: Eliminar  |  Esc: Salir"
        )
        tk.Label(
            self.root, text=leyenda,
            font=("Segoe UI", 8),
            bg=COLOR_BG, fg="#6c7086"
        ).pack()

        # Frame de entrada
        frame_entrada = tk.Frame(self.root, bg=COLOR_BG)
        frame_entrada.pack(padx=20, pady=10, fill="x")

        self.entry_tarea = tk.Entry(
            frame_entrada,
            font=("Segoe UI", 12),
            bg=COLOR_PANEL, fg=COLOR_TEXT,
            insertbackground=COLOR_TEXT,
            relief="flat", bd=6
        )
        self.entry_tarea.pack(side="left", fill="x", expand=True, ipady=4)
        self.entry_tarea.focus_set()

        tk.Button(
            frame_entrada, text="➕ Agregar",
            font=("Segoe UI", 10, "bold"),
            bg=COLOR_BTN_OK, fg="#1e1e2e",
            relief="flat", cursor="hand2", padx=10,
            command=self._agregar_tarea
        ).pack(side="left", padx=(8, 0))

        # Listbox con scrollbar
        frame_lista = tk.Frame(self.root, bg=COLOR_PANEL)
        frame_lista.pack(padx=20, pady=4, fill="both", expand=True)

        scrollbar = tk.Scrollbar(frame_lista, bg=COLOR_PANEL)
        scrollbar.pack(side="right", fill="y")

        self.listbox = tk.Listbox(
            frame_lista,
            font=("Segoe UI", 11),
            bg=COLOR_PANEL, fg=COLOR_TEXT,
            selectbackground=COLOR_ACCENT,
            selectforeground="#ffffff",
            activestyle="none",
            relief="flat", bd=0,
            yscrollcommand=scrollbar.set
        )
        self.listbox.pack(fill="both", expand=True, padx=4, pady=4)
        scrollbar.config(command=self.listbox.yview)

        # Botones de acción
        frame_botones = tk.Frame(self.root, bg=COLOR_BG)
        frame_botones.pack(padx=20, pady=10, fill="x")

        tk.Button(
            frame_botones, text="✔ Completar (C)",
            font=("Segoe UI", 10),
            bg=COLOR_BTN_COM, fg="#1e1e2e",
            relief="flat", cursor="hand2",
            command=self._marcar_completada
        ).pack(side="left", expand=True, fill="x", padx=(0, 6))

        tk.Button(
            frame_botones, text="🗑 Eliminar (Del)",
            font=("Segoe UI", 10),
            bg=COLOR_BTN_DEL, fg="#1e1e2e",
            relief="flat", cursor="hand2",
            command=self._eliminar_tarea
        ).pack(side="left", expand=True, fill="x")

    # ── Atajos de teclado con .bind() ──────────────────────────────
    def _registrar_atajos(self):
        self.root.bind("<Return>", lambda e: self._agregar_tarea())
        self.root.bind("<c>",      lambda e: self._marcar_completada())
        self.root.bind("<C>",      lambda e: self._marcar_completada())
        self.root.bind("<Delete>", lambda e: self._eliminar_tarea())
        self.root.bind("<d>",      lambda e: self._eliminar_tarea())
        self.root.bind("<D>",      lambda e: self._eliminar_tarea())
        self.root.bind("<Escape>", lambda e: self._cerrar())

    # ── Acciones ───────────────────────────────────────────────────
    def _agregar_tarea(self):
        texto = self.entry_tarea.get()
        try:
            self.servicio.agregar_tarea(texto)
            self.entry_tarea.delete(0, tk.END)
            self._refrescar_lista()
        except ValueError as e:
            messagebox.showwarning("Campo vacío", str(e))

    def _marcar_completada(self):
        indice = self.listbox.curselection()
        if not indice:
            messagebox.showinfo("Sin selección", "Selecciona una tarea primero.")
            return
        try:
            self.servicio.marcar_completada(indice[0])
            self._refrescar_lista()
        except IndexError as e:
            messagebox.showerror("Error", str(e))

    def _eliminar_tarea(self):
        indice = self.listbox.curselection()
        if not indice:
            messagebox.showinfo("Sin selección", "Selecciona una tarea primero.")
            return
        try:
            self.servicio.eliminar_tarea(indice[0])
            self._refrescar_lista()
        except IndexError as e:
            messagebox.showerror("Error", str(e))

    def _cerrar(self):
        if messagebox.askyesno("Salir", "¿Deseas cerrar la aplicación?"):
            self.root.destroy()

    def _refrescar_lista(self):
        self.listbox.delete(0, tk.END)
        for tarea in self.servicio.obtener_tareas():
            self.listbox.insert(tk.END, str(tarea))
            idx = self.listbox.size() - 1
            if tarea.completada:
                self.listbox.itemconfig(idx, fg="#6c7086")
            else:
                self.listbox.itemconfig(idx, fg="#cdd6f4")

    def iniciar(self):
        self.root.mainloop()