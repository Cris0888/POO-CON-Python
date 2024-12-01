class Banco :
    def __init__(self,propietario,moneda,saldo):
        self.__propietario = propietario
        self.__moneda= moneda
        self.__saldo=saldo


    def get__propietario(self):
        return self.__propietario
    
    def get__moneda(self):
        return self.__moneda
    
    
    def get__saldo(self):
        return self.__saldo
    
    def set__moneda(self,moneda):
        self.__moneda = moneda

    def atributo_publico(self):
        print("soy un atributo publico")

propietario1=Banco("christian","pesos",1000000)
print(propietario1.get__propietario())
print(propietario1.get__moneda())
print(propietario1.get__saldo())
propietario1.set__moneda("dolares")
print(propietario1.get__moneda())



print(propietario1.atributo_publico())


'''Los getters y setters son métodos especiales utilizados en la encapsulación en Python para obtener y modificar
los valores de los atributos privados de una clase. Un getter es un método que permite obtener el valor de un
atributo, mientras que un setter es un método que permite modificar el valor de un atributo.'''


'''
def get__moneda(self):
        return self.__moneda

def set__moneda(self,moneda):
        self.__moneda = moneda

aqui tenemos dos metodos uno get que es para mostrar y otro set que es para modificar ese dato privado
ejemplo: arriba tenemos dos metodos el primero que es get es para llamar el atributo privado y el segundo
que es set es para modificarlo el tiene un atributo llamado moneda que abajo tenemos un self le estamos diciendo que 
self.__moneda es igual al atributo moneda de este metodo
mas abajo creamos una instancia que se llama propietario1 que es igual ala clase y le pasamos 3 datos en las posiciones
de esa clase despues como queremos modificar ese dato privado ponemos que poner
propietario1.set__moneda(dolares) y ya esta modificado  esto solo se llama para modificarlo 
si queremos mostrar con ese dato ya  actualizado ne pantalla tenemos que poner bajo el metodo get
por medio de un print(propietario1.get__moneda()) ya nos arroja con el dato actualizado

un atributo es  privado en python cuando el ponemos doble o triple guiones bajos el atributo es privado porque
no tengo aceso a el cuando lo dentro de la clase y  hago un print y ejecutarlo me dice 
AttributeError: 'Banco' object has no attribute '__propietario' osea  quiere decir que le atributo de la clase banco no puede ser
imprimido em pantalla porque esta definido como privado no solo los atributos tambien los metodos creamos un metodo
llamado __moneda y al llamarlo para imprimirlo en pantalla me dice 
AttributeError: 'Banco' object has no attribute '__moneda' osea que el metodo __moneda esta privado y no puede
ser imprimido en pantalla y si ponemos que nos muestre el metodo atributo_publico si lo muestra porque ese
metodo no esta definido como privado esto nos ayuda mucho almacenas password y datos que queremos que se mantengan
privados ''' 

