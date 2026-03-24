from src.models.UserModel import UsuariosModel
from src.models.SchemasModel import UsuariosSchema
from pydantic import ValidationError

class AutoController:
    def __init__(self):
        self.model = UsuariosModel()
    
    def regristrar_usuario(self, nombre, correo, contra):
        try:
            nuevo_usuario = UsuariosSchema(nombre=nombre, correo=correo, contra=contra)
            success = self.model.registrar(nuevo_usuario)
            return success, "Usuario creado correctamente"
        except ValidationError as e:
            return False, e.errors()[0]["msg"]