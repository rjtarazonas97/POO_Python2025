class Notificador:
    def __init__(self,usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje
        
    def notificar(self):
        raise NotImplementedError # agrega funciones para no eliminarlas principio solid abierto cerrado
    
class NotificadorEmail(Notificador):
    def Notificar(self):
        print(f"Enviando mensaje por mail a {self.usuario.email}")
        
class NotificadorSMS(Notificador):
    def Notificar(self):
        print(f"Enviando SMS a {self.usuario.sms}")
        
class NotificadorWhatsApp(Notificador):
    def Notificar(self):
        print(f"Enviando whatsapp a {self.usuario.whatsapp}")
        
class NotificadorX(Notificador):
    def Notificar(self):
        print(f"Enviando X a {self.usuario.X}")