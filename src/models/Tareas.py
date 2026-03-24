from .database import Database
class TareasModel:
    def __init__(self):
        self.db = Database()
        
    def listar_por_usuario(self, ID_usuario):
        conn = self.db.get_connection()
        cursor = self.db.get_connection()
        query = "SELECT * FROM tareas WHERE ID_usuario = %s ORDEN BY fecha_lim ASC"
        cursor.execute(query, (ID_usuario,))
        resultado = cursor.fetchall()
        conn.close
        return resultado
    
    def crear(self, ID_usuario, Nombre_tarea, descripcion, prioridad, tipo):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        query = """INSERT tareas (ID_usuario, Nombre_tarea, descripcion, prioridad, tipo)
                VALUES (%s, %s, %s, %s, %s)"""
        cursor.execute(query, (ID_usuario, Nombre_tarea, descripcion, prioridad, tipo))
        conn.commit()
        conn.close()