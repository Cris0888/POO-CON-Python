class Motocicleta:
    def correr(self):
        return 'a 100 km'
    
class Coche:
    def correr(self):
        return 'a 1000 km'

class Avion:
    def correr(self):
        return 'a 10000 km'
    
class Bicicleta:
    def correr(self):
        return 'a 10 km'

coche= Coche()
motocicleta=Motocicleta()
avion=Avion()
bicicleta=Bicicleta()
print(bicicleta.correr())
    
'''
#el polimorfismo es cuando los objetos se llaman iguales pero hacen difentes cosas en este ejemplo
#estamos usando las motos carros aviones bicicletas y el objeto se llama correr todos estos corren pero cada uno 
#corre a velocidades difentes eso es el polimorfismo los mismos obejetos pero con direntes maneras de comportamiento  
#estamos creando las intancias de cada uno de ellos pero cuando ponemos el nombre de la intacia de esa clase
#y el metodo que es correr cada uno arroja un valor diferente eso es el polimosrfismo todos los objetos se llaman
#de manera de dirente pero tienen un comportamiento difente
'''
