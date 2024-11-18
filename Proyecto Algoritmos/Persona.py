class Persona:
    def __init__(self, nombre, apellido, correo, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.telefono = telefono
        
    def show(self):
        print( f'''
    Nombre: {self.nombre}
    Apellido: {self.apellido}
    Correo: {self.correo}
    Telefono: {self.telefono}''')
    
    def to_dict(self):
        return {
            "nombre": self.nombre,
            "apellido": self.apellido,
            "correo": self.correo,
            "telefono": self.telefono
        }
    
class Cliente_Nat(Persona):
    def __init__(self, nombre, apellido, correo, telefono, cedula, direccion):
        super().__init__(nombre, apellido, correo, telefono)
        self.cedula = cedula
        self.direccion = direccion 
    def show(self):
        super().show()
        print(f'''
            Cedula: {self.cedula}
            Direccion: {self.direccion}''')
    
    def to_dict(self):
        return {
            "nombre": self.nombre,
            "apellido": self.apellido,
            "correo": self.correo,
            "telefono": self.telefono,
            "cedula": self.cedula,
            "direccion": self.direccion
        }
    
class Cliente_Jur():
    def __init__(self, nombre, rif, correo, direccion, telefono, contacto):
        self.nombre = nombre
        self.rif = rif
        self.correo = correo
        self.direccion = direccion
        self.telefono = telefono
        self.contacto = contacto
        
    def show(self):
        print(f'''
    Nombre de empresa: {self.nombre}
    RIF: {self.rif}
    Correo: {self.correo}
    Direccion: {self.direccion}
    Telefono: {self.telefono}
    Contacto:''')
        self.contacto.show()
    
    def to_dict(self):
        return {
            "nombre": self.nombre,
            "rif": self.rif,
            "correo": self.correo,
            "direccion": self.direccion,
            "telefono": self.telefono,
            "contacto": self.contacto.to_dict()
        }