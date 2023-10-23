import random

class Contraseña:

    def __init__(self, longitud=8):
        self.longitud = longitud
        self.contraseña = self.generar_password()

    def es_fuerte(self):
        mayuscula = 0
        minuscula = 0
        numeros = 0
        especiales = 0

        for caracter in self.contraseña:
            if caracter.isupper():
                mayuscula += 1
            elif caracter.islower():
                minuscula += 1
            elif caracter.isdigit():
                numeros += 1
            else:
                especiales += 1
        
        return mayuscula > 2 and minuscula > 1 and numeros > 5 and especiales > 0

    def generar_password(self):
        caracteres = "CarroAzul_21"
        contrasena = ""
        for i in range(self.longitud):
            contrasena += caracteres[random.randint(0, len(caracteres) - 1)]
        return contrasena
    
    def seguridad_contrasena(self):
        if self.longitud <= 6:
            return "Debil"
        elif self.longitud <= 10:
            return "Media"
        else:
            return "Fuerte"

# Crear una instancia de la clase Contraseña
contrasena_1 = Contraseña(12)
print(contrasena_1.contraseña)
print(contrasena_1.es_fuerte())
print(contrasena_1.seguridad_contrasena())
