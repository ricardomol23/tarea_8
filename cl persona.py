class Personas:
    def __init__(self, nombre_atributo, edad_atributo, cedula_atributo):
     self.nombre = nombre_atributo
     self.edad = edad_atributo
     self.cedula = cedula_atributo

    def mayor_edad(self):
      return self.edad >= 18
persona_1 = Personas("Juan", 25, "10143243")

print(persona_1.edad)
print(persona_1.nombre)
print(persona_1.cedula)
print(persona_1.mayor_edad())


