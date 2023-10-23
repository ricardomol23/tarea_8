class Formula:
    def __init__(self):
        return

    def primos(self, cantidad):
        arreglo_primos = []
        numero_iteracion = 1
        while len(arreglo_primos) < cantidad:
            if not (self.es_divisible_por_dos(numero_iteracion) or
                    self.es_divisible_por_tres(numero_iteracion) or
                    self.es_divisible_por_cinco(numero_iteracion)):
                arreglo_primos.append(numero_iteracion)
            numero_iteracion += 1
        return arreglo_primos

    def operacion_modulo(self, cantidad):
        numeros_con_residuo_cero = []
        for numero_iteracion in range(1, cantidad + 1):
            if numero_iteracion % cantidad == 0:
                numeros_con_residuo_cero.append(numero_iteracion)
        return numeros_con_residuo_cero

    def sumar(self, entero1, entero2):
        return entero1 + entero2

    def fibonacci(self, cantidad):
        if cantidad <= 0:
            return []

        fibonacci_sequence = [0, 1]
        while len(fibonacci_sequence) < cantidad:
            next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
            fibonacci_sequence.append(next_number)

        return fibonacci_sequence

    def es_divisible_por_dos(self, numero):
        return numero % 2 == 0

    def es_divisible_por_tres(self, numero):
        return numero % 3 == 0

    def es_divisible_por_cinco(self, numero):
        return numero % 5 == 0

formula_uno = Formula()

# Realizar la suma de dos enteros
suma_result = formula_uno.sumar(5, 7)
print("Suma de 5 y 7:", suma_result)

# Obtener los primeros 10 números de Fibonacci
fibonacci_result = formula_uno.fibonacci(10)
print("Números de Fibonacci:", fibonacci_result)

# Obtener los números con residuo 0 al operar modulo 3
mod_result = formula_uno.operacion_modulo(3)
print("Números con residuo 0 al operar modulo 3:", mod_result)

# Obtener los primeros 10 números primos
primos_result = formula_uno.primos(10)
print("Primeros 10 números primos:", primos_result)
