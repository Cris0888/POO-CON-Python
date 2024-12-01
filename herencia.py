class Persona:
    def __init__(self,nombre,cedula,grado,profecion):
        self.nombre=nombre
        self.cedula=cedula
        self.grado=grado
        self.profecion=profecion


class Corredor(Persona):
    def __init__(self, nombre, cedula, grado, profecion,moto,licencia,categoria):
        super().__init__(nombre,cedula,grado,profecion)
        self.moto=moto
        self.licencia=licencia
        self.categoria=categoria

#la herencia la estamos aplicando desde que creamos la funcion corredor que le estamos diciendo que herede los atributos
#de la clase persona y ay ponemos el parametro super y despues el __init__ en los corchetes del parametro super ponemos
#todos los atributos que queremos que herede de la clase padre que en este caso se llama persona de la clase persona
#nos esta heredando el nombre , cedula , grado , profecion

    def corredores(Corredor):
        print(f" mi nombre es {corredor1.nombre} mi cedula es {corredor1.cedula} \n mi grado es {corredor1.grado} mi profecion es {corredor1.profecion} \n mi motocicleta es una {corredor1.moto} licecencia {corredor1.licencia} y mi categoria es {corredor1.categoria} ")

corredor1=Corredor('juan',1112235,11,'corredor de moto_gp','kawasaki ninja h2r','si','A3')
    

corredor1.corredores()


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

toyota=Marcas('rojo',2024,'toyota','euro 10','carroseria-88')
print(toyota.marca)

#aqui la herencia la estamos haciendo de la clase automovil y le estamos añadiendo los atrubutos turbo y carroceria_1_1
#que son los atributos de la clase marcas los demas lo hereda de la clase automovil y despues estamos metiendole
#datos de forma manual en el anterior ejemplo estamos ejecutandolo atravez de una funcion aqui no solo le decimos la 
#instancia punto y nombre del atributo que queremos que nos muestre




