class Persona:
    def __init__(self,nombre,cedula,grado,profecion):
        self.nombre=nombre
        self.cedula=cedula
        self.grado=grado
        self.profecion=profecion

class Automovil:
    def __init__(self,color,modelo,marca):
        self.color=color
        self.modelo=modelo
        self.marca=marca

class Marcas (Automovil):
    def __init__(self, color, modelo, marca,turbo,carroceria_1_1):
        super().__init__(color, modelo, marca)
        self.turbo=turbo
        self.carroceria_1_1=carroceria_1_1

    def mostrar_marca(self):
        print (f"hola mi marca es {persona1.marca}")


class Persona_marca(Persona,Marcas):
    def __init__(self,nombre,cedula,grado,profecion,color,modelo,marca,turbo,carroceria_1_1,concecionario,ciudad):
        Persona.__init__(self,nombre,cedula,grado,profecion)
        Marcas.__init__(self, color, modelo, marca,turbo,carroceria_1_1)
        self.concecionario=concecionario
        self.ciudad=ciudad

    def presentarse(self):
        print (super().mostrar_marca())


    

persona1=Persona_marca('christian',1112399654,11,'eletricista','amarillo',2025,'BMW','turbo-88','carroseria-99','sol-motos','buga')
persona2=Automovil('rojo',2024,"bmw")

#aqui estamos aplicando una herencia multiple herencia multiple es cuando la herencia tiene mas de dos clases
# no estamos poniendo el metodo super el metodo super se pone cuando la herencia es de padre
#a hijo directamente pero aqui es el hijo del hijo del hijo entonces al ser asi lo que hacemos es poner el nombre de la clase 
# y los atributos que queremos que nos herede de esa clase despues estamos creando la instacia persona1 que hace referencia 
# ala clase persona_marcas y que es de herencia multiple y no esta trallendo todos los atributos de las clases persona y marca


persona1.presentarse()

#aqui estamos heredando un metodo de la clase marcas que se llama mostrar_marca() este metodo lo que hace es retornar el 
#mensaje hola mi marca es {persona1.marca} y persona1.marca es que muestre el atributo marca de la instacia persona1
#y nos muestre esa marca de la instacia persona1 despues creamos un metodo en la clase persona_marca que se llama 
# precentarse el metodo lo que hace es retornar la funcion que queremos heredar que se llama mostrarmarca
#para poder que nos herede esa funcion debemos poner super().mostrar_marca porque el metodo super
# lo que hace en python es hacer refencia es que estamos trayedo un metodo desde arriba o llamado un metodo de la clase padre


herencia= issubclass(Persona_marca,Persona)
print(f"la subclase es {herencia}")

#con el metodo issubclass es para que python nos devuelva si la clase es una subclase de la clase padre
# python devuelve dos valores true o false como es el codigo creamos una variable despues le ponemos
# issubclass y entre corchetes la primera clase que se pone es la subclase y la 2 la clase padre y despues
#por medio de un print la mostramos si arroja true es una subclase y si arroja false es porque no es una subclase de
#la clase padre

istancia=isinstance(persona1,Persona_marca)
print(f"la instacia es {istancia}")

#con el metodo isintance es para que python nos devuelva si la variable es una instancia de la clase 
# python devuelve dos valores true o false como es el codigo creamos una variable despues le ponemos isintance 
#y entre corchetes la primera es variable que queremos saber si es una instacia de esa clase despues va la
#la clase que queremos saber si devuelve false es porque esa instacia no es de esa clase que pusimos
