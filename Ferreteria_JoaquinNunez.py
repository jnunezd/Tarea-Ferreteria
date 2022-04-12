import platform
from os import system


def limpiar_pantalla():
    system('cls' if platform.system() == 'Windows' else 'clear')


class Ferreteria():
    def __init__(self) -> None:
        self.productos = {
            "1": {
                "nombre": "Clavos",
                "precio": 100
            },
            "2": {
                "nombre": "Tornillos",
                "precio": 200
            },
            "3": {
                "nombre": "Alambre",
                "precio": 300
            },
            "4": {
                "nombre": "Martillo",
                "precio": 400
            },
            "5": {
                "nombre": "Cerradura",
                "precio": 500
            },
            "6": {
                "nombre": "Desatornillador",
                "precio": 600
            },
            "7": {
                "nombre": "Cable",
                "precio": 700
            },
        }

        self.carrito = {}
        self.carrito_ej = {
            "1": {
                "nombre": "Clavos",
                "precio": 100,
                "cantidad": 1
            }
        }
        self.total = 0
        limpiar_pantalla()
        self.proceso_compra()

    def listar_productos(self):
        limpiar_pantalla()
        for key, value in self.productos.items():
            print(
                f"Producto {key} :\nNombre: { value['nombre'] } - Precio: {value['precio']}\n")
        input("Enter para continuar")

    def agregar_al_carrito(self):
        indice = input(
            "Ingrese el numero del producto que desea agregar al carrito: ")
        cantidad = int(input("ingrese al cantidad del producto a comprar: "))

        dict_cantidad = {"cantidad": cantidad}

        self.carrito[indice] = {**self.productos[indice], **dict_cantidad}

    def calcular_total(self):
        suma = 0
        for key, value in self.carrito.items():
            valor = int(value['precio'])*int(value['cantidad'])
            suma = suma + valor
        self.total = suma
        return int(suma)

    def ver_carrito(self):
        limpiar_pantalla()
        print("los productos en el carrito son:\n")
        for key, value in self.carrito.items():
            print(
                f"Producto {key} :\nNombre: { value['nombre'] } - Precio: {value['precio']} - Cantidad del producto: {value['cantidad']}\n")

        print(f"El total de la compra es: {self.calcular_total()}\n")
        input("Enter para continuar")

    def eliminar_del_carrito(self):
        print("Su carrito es:")
        self.ver_carrito()
        n = input("Ingrese el numero del articulo que desea quitar del carrito: ")
        del self.carrito[n]
        print("Se ha quitado el articulo del carrito")
        input("Enter para continuar")

    def proceso_compra(self):
        nosalir = True
        while nosalir:
            limpiar_pantalla()
            print("Bienvenido a la ferreteria\nPara ver los productos presione 1\nPara comprar un producto presione 2\nPara ver el carrito presione 3\nPara eliminar un producto del carrit presione 4\nPara salir presione 5\n")

            opcion = input("Seleccione una opcion: ")

            if opcion == '1':
                self.listar_productos()
            elif opcion == '2':
                self.listar_productos()
                self.agregar_al_carrito()
            elif opcion == '3':
                self.ver_carrito()
            elif opcion == '4':
                self.eliminar_del_carrito()
            elif opcion == '5':
                limpiar_pantalla()
                print("Muchas gracias por comprar en la ferreteria")
                nosalir = False
            else:
                print("Seleccione una opcion valida")


if __name__ == "__main__":
    Ferreteria()
