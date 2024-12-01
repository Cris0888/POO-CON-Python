from abc import  ABC,abstractclassmethod
class Moto:
    def __init__(self):
        self._estado = "apagado"

    def encender(self):
        self._estado = "encendido"
        print("moto encendida")
        
    def conducir(self):
        if self._estado == "apagado":
            self.encender()
            print("conduciendo la moto")

mi_moto=Moto()
mi_moto.conducir()




class persona(ABC):
    @abstractclassmethod
    def __init__(self,nombre,trabajo,ciudad):
        self.nombre=nombre
        self.trabajo=trabajo
        self.ciudad=ciudad

    def precentarse(self):
        return f"hola mi nombre es {self.nombre} y y trabajo como {self.trabajo} y vivo en {self.ciudad}"
    
class Corredor(persona):
    def __init__(self,nombre,trabajo,ciudad,moto,corredor):
        super().__init__(nombre,trabajo,ciudad)
        self.moto=moto
        self.corredor=corredor

corredor=Corredor('juan','corredor','miami','gs bmw','valentino rossi')
print(corredor.precentarse())
""" las clases absatractas son para ocultar la logica de el codigo y cuando se usa parace facil eso pasa porque el 
progrmador oculta la logica cuando definimos ABC Y astractclassmethod es es que creamos la clase base y ella
si la llammos no hace nada porque es como un molde ella funciona si la heredamos y le añadimos mas cosas
y si creamos un metodo astracto estamos obligados a usarlo si o si con las clases abstractas  """