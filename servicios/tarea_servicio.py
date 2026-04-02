from modelos.tarea import Tarea


class TareaServicio:
    def __init__(self):
        self._tareas: list[Tarea] = []

    def agregar_tarea(self, descripcion: str) -> Tarea:
        descripcion = descripcion.strip()
        if not descripcion:
            raise ValueError("La descripción no puede estar vacía.")
        tarea = Tarea(descripcion)
        self._tareas.append(tarea)
        return tarea

    def obtener_tareas(self) -> list[Tarea]:
        return list(self._tareas)

    def marcar_completada(self, indice: int) -> Tarea:
        if not (0 <= indice < len(self._tareas)):
            raise IndexError("Índice de tarea inválido.")
        self._tareas[indice].marcar_completada()
        return self._tareas[indice]

    def eliminar_tarea(self, indice: int) -> None:
        if not (0 <= indice < len(self._tareas)):
            raise IndexError("Índice de tarea inválido.")
        self._tareas.pop(indice)