from colorama import init,Fore,Back,Style
init()
class Xtz:
    def correr(self):
        print("la xtz esta corriendo duro ")

    def parar(self):
        print("la xtz esta mermando la velocidad")

class Rx_115:
    def correr(self):
        print("la rx 115 esta corriendo duro ")

    def parar(self):
        print("la rx 115 esta mermando la velocidad")

class Persona:
    def agarar_moto(self,xtz,rx_115):
        xtz.correr()
        rx_115.parar()
        print("la ande re durooo")


for moto in [Xtz(),Rx_115()]:
    moto.parar()

#esto lo que hace es crear dos clases xtz y rx 115 las dos clases tienen dos metodos que es correr y parar esto
#es un ejemplo de polimorfismo porque se llaman iguales los metodos pero no las clases en resumen aqui estamos
#creando las dos clases y en la parte de abajo hacemos un for que nos recorra esas dos clases el tiene una 
#variable que se llama moto que es la que recorre las clases y despues le pasamos entre corchetes las 
# clases que queremos recorrer ay ponemos el nombre moto que el que recorre las dos clases punto y el nombre del metodo
#queremos  que nos recorra al poner parar el va y recorre las dos clases y donde haiga un metodo llamadado parar lo 
#imprime en pantalla solo que cada clase tiene un mensaje difrente pero se llama igual los metodos de las clases
    
xtz = Xtz()
rx_115 = Rx_115()
persona= Persona()
persona.agarar_moto(xtz,rx_115)

''' este metodo lo que hace es crear 3 instancias de las clases persona xtz y rx 115 despues le decimos que 
nos cree en la clase persona un metodo llamadado agarrar_moto ese metodo le estamos entregando 2 instancias que 
creamos mas abajo que es la intancia rx 115 que hace referencia la clase Rx 115 despues la instancia
xtz que hace referencia ala clase Xtz despues le decimos que nos imprima xtz.correr y rx_115.parar 
y que nos retorne el mensaje la ande re duro que sucede para poder llamar este metodo llamado agarrar_moto
estamos abajo en la intancia persona agregandole el metodo agarrar_ moto y pasandole los dos instancias que son
rx_115 y xtz si no le pasamos esos parametros el metodo no podra retornarnos ningun mensaje solamente el print
que es la ande re duro pero para que se ejecute debemos eliminar los dos instancias  que le pasamos
que son   rx_115 y xtz'''
