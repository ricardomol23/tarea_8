class Persona:
    def __init__(self, nombre, edad, dni, sexo, peso, altura):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        self.sexo = sexo
        self.peso = peso
        self.altura = altura

    def calcularIMC(self):
        imc = self.peso / (self.altura ** 2)
        if imc < 20:
            return -1  # Bajo peso
        elif 20 <= imc <= 25:
            return 0  # Peso normal
        else:
            return 1  # Sobrepeso

    def esMayorDeEdad(self):
        return self.edad >= 18

    def comprobarSexo(self, sexo):
        if sexo.upper() == 'H' or sexo.upper() == 'M':
            self.sexo = sexo.upper()
        else:
            self.sexo = 'H'

    def __str__(self):
        return f"Nombre: {self.nombre}\nEdad: {self.edad}\nDNI: {self.dni}\nSexo: {self.sexo}\nPeso: {self.peso}\nAltura: {self.altura}"

# Ejemplo de uso
persona1 = Persona("Ricardo", 20, "357456978", "H", 83, 1.83)
print(persona1)
print(f"IMC: {persona1.calcularIMC()}")
print(f"Es mayor de edad: {persona1.esMayorDeEdad()}")
persona1.comprobarSexo('F')
print(f"Sexo corregido: {persona1.sexo}")

