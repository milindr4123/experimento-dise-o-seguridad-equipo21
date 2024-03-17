class Pago:
    def __init__(self, nombre, numero_cuenta, correo, cedula, banco):
        self.name_partner = nombre
        self.account_number = numero_cuenta
        self.email = correo
        self.id_partner = cedula
        self.bank_name = banco


# Ejemplo de uso
nombre_usuario = "Juan Pérez"
numero_cuenta_usuario = "123456789"
correo = "diegog4321@gmail.com"
cedula = "123456"
banco = "Davivienda"
usuario = Pago(nombre_usuario, numero_cuenta_usuario, correo, cedula, banco)

print("Nombre:", usuario.name)
print("Número de cuenta:", usuario.account_number)
print("Banco:", usuario.bank_name)