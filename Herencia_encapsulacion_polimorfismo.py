# Clase inicio
class Dispositivo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.__modelo = modelo  # Atributo encapsulado

    # Método que será sobrescrito por las subclases
    def encender(self):
        raise NotImplementedError("Este método debe ser sobrescrito por las subclases")

    # Método para obtener el modelo (encapsulación)
    def obtener_modelo(self):
        return self.__modelo

# Clase derivada que hereda de Dispositivo
class Telefono(Dispositivo):
    def encender(self):
        return "Telefono prendido"

# Clase derivada que hereda de Dispositivo
class Computadora(Dispositivo):
    def encender(self):
        return "La portatil está encendiendo"

# Función que demuestra polimorfismo
def imprimir_encendido(dispositivo):
    print(f"{dispositivo.marca} {dispositivo.obtener_modelo()} está encendiendo: {dispositivo.encender()}")

# Crear instancias de las clases derivadas
mi_telefono = Telefono("huawei", "P30 lite")
mi_computadora = Computadora("ASUS VIVOBOOK", "RYZEN 3")

# Usar polimorfismo para llamar a la misma función con diferentes tipos de objetos
imprimir_encendido(mi_telefono)
imprimir_encendido(mi_computadora)