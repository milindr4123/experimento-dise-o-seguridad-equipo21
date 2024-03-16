class Entrenamiento:
    def __init__(self, nombre, numero_cuenta):
        self.nombre = nombre
        self.numero_cuenta = numero_cuenta


# Ejemplo de uso
nombre_usuario = "Juan Pérez"
numero_cuenta_usuario = "123456789"
usuario = Entrenamiento(nombre_usuario, numero_cuenta_usuario)

print("Nombre:", usuario.nombre)
print("Número de cuenta:", usuario.numero_cuenta)