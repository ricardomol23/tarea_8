# Crea una clase cuenta que tendrá los siguientes atributos: titular (que es nombre de la persona) 
# y cantidad. El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos para la clase:
class Cuentas:
    #Caracterisitcas
    def __init__(self, titular_atributo, cantidad_atributo=0):
        self.titular = titular_atributo
        self.cantidad = cantidad_atributo
    
    def depositar(self, cantidad):
        if cantidad <= 0:
            return
        else:
            self.cantidad += cantidad

    def retirar(self, cantidad_ingresado):
        if cantidad_ingresado > self.cantidad:
            raise ValueError("No hay suficiente saldo")
        self.cantidad -= cantidad_ingresado
    
    def mostrar_saldo(self):
        print(f"El saldo de la cuenta es {self.cantidad}")

cuenta_1 = Cuentas("Duvan Ortiz")

cuenta_1.depositar(100)

cuenta_1.retirar(50)

cuenta_1.mostrar_saldo()