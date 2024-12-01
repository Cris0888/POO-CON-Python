class Estudiante:
    def __init__(self,nombre,edad,grado):
        self.nombre=nombre
        self.edad=edad
        self.grado=grado
    
    def Estudiar(self):
        return(f"")

nombre=input("digite su nombre: ")
edad= int(input("digite su edad: "))
grado= int(input("digite su grado: "))

alumno = Estudiante (nombre,edad,grado)
# la variable alumno que esta arriba de este comentario se convirtio en una instancia ay estamos diciendo que la instancia
#alumno es igual ala clase estudiante que tiene unos atributos que son nombre edad y grado en la instancia alumno estamos
#diciendo que en la pociciones de la clase estudiante nos añada los atributos que estan en los input que son 
#nombre edad grado digitadas por el usuario cada vez que creemos una instacia y ponemos la clase y
#estamos diciendo que esa instancia tiene unos atributos unicos cada instacia tiene datos difentes y eso es lo que hace que
#podamos hacer varias lineas de codigo con datos difentes

print(f"el estudiante {alumno.nombre} de {alumno.edad} años de edad y de grado {alumno.grado} esta estudiando ")





