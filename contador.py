class Contador:
    def __init__(self,valor_inicial=0):
        self.valor= valor_inicial
    
    def reset(self):
        self.valor=0

    def inc(self):
        self.valor+=1

    def dec(self):
        self.valor-=1

    def valor_actual(self):
        return self.valor
    
    def valorActual(self,nuevo_valor):
        self.valor=nuevo_valor

    

contador_1=Contador()
contador_2=Contador()
contador_3=Contador()

contador_1.valorActual(10)
contador_1.inc()
contador_1.inc()
contador_1.dec()
contador_1.inc()
print(contador_1.valor_actual())

contador_2.valorActual(17)
contador_2.dec()
contador_2.dec()
contador_2.dec()
contador_2.inc()
print(contador_2.valor_actual())

contador_3.valorActual(1)
contador_3.inc()
contador_3.dec()
contador_3.dec()
contador_3.inc()
print(contador_3.valor_actual())