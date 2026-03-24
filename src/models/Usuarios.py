import bcrypt
from .database import Database

class UsuariosModel:
    def __init__(self):
        self.db = Database()
        
    def registrar(self, usuario_data):
        salt= bcrypt.gensalt()
        hashed_pw = bcrypt.hashpw(usuario_data.password.encode('utf-8'),salt)
        
        conn = self.db.get_connection()
        cursor= conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO usuarios (Nombre, correo, contra) VALUES (%s, %s, %s)",
                (usuario_data.Nombre, usuario_data.correo, hashed_pw.decode('utf-8'))
            )
            conn.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            conn.close()
            
    def validar_login(self, correo, contra):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios WHERE correo=%s ",(correo,))
        user = cursor.fetchone()
        conn.close()
            