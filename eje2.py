class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    
    def presentarse(self):
        return (f"hola mi nombre es {Persona1.nombre} y tengo {Persona1.edad} años")
    
class Estudiante(Persona):
    def __init__(self,nombre,edad,grado):
        super().__init__(nombre,edad)
        self.grado=grado
    
    def nivel(self):
        return(f"hola estoy en el grado {gradoo.grado}")

        
    
nombree=input("digite su nombre ")
edadd=int(input("digite su edad "))
gradoo=int(input("digite su grado "))

Persona1=Persona(nombree,edadd)

gradoo = Estudiante (nombree,edadd,gradoo)
print(Persona1.presentarse())
print(gradoo.nivel())
