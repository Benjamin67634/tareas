from src.models.TareasModel import TareasModel

class TareasController:
    def __init__(self):
        self.model = TareasModel()
    
    def obtener_lista(self, ID_usuario):
        return self.model.listar_por_usario(ID_usuario)
    
    def guardar_nueva(self, ID_usuario, Nombre_tarea, descripcion, prioridad, tipo):
        if not Nombre_tarea:
            return False, "EL titulo es obrigatorio"
        
            self.model.crear(ID_usuario, Nombre_tarea, descripcion, prioridad, tipo)
            return True, "Tarea guardada"