# GUI LISTA DE TAREAS

Interfaz gráfica con Tkinter que permite
gestionar tareas diarias usando tanto mouse como teclado.

## Atajos de teclado

| Tecla          | Acción                       |
|----------------|------------------------------|
| `Enter`        | Agregar tarea                |
| `C`            | Marcar tarea como completada |
| `Delete` / `D` | Eliminar tarea seleccionada  |
| `Escape`       | Cerrar la aplicación         |

## Cómo ejecutar
```bash
python main.py
```

## Estructura del proyecto
```
S16_GUI_LISTA_TAREAS/
├── main.py
├── .gitignore
├── README.md
├── modelos/
    └── __init.py
│   └── tarea.py
├── servicios/
    └──__init__.py
│   └── tarea_servicio.py
└── ui/
    └──__init__.py
    └── app_tkinter.py
```

## Arquitectura

- `modelos/` → Clase Tarea (datos y estado)
- `servicios/` → Lógica CRUD sin dependencia de UI
- `ui/` → Interfaz Tkinter con eventos `command=` y `.bind()`
- `main.py` → Punto de entrada