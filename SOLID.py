class Notificador:
    def __init__(self,nombre,correo):
        self.nombre=nombre 
        self.correo=correo
    def notificar(self):
        raise NotImplementedError
    
class SMS(Notificador):
    def notificar(self):
        return print(f"notificar por  {self.nombre.sms}")
    
class email(Notificador):
    def notificar(self):
        return print(f"notificar por  {self.nombre.email}")
        