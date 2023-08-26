class FicherosProducto:
    def __init__(self):
        self.menu = (
            "1. Crear fichero\n2. Mostrar fichero\n3. Mostrar línea de fichero\n4. Salir"
        )
    def guardar_fichero(self, num):
            if num>=1 and num<=10:
                tabla = [f"{num} x {i} = {num * i}\n" for i in range(1, 11)]
                with open(f"tabla-{num}.txt", "w") as file:
                    file.writelines(tabla)
            else:
                print("Número fuera de rango (1-10).\n")

    def leer_mostrar_fichero(self, num):
            try:
                with open(f"tabla-{num}.txt", "r") as file:
                    leer_tabla = file.read()
                    print(leer_tabla)
            except FileNotFoundError:
                print(f"El fichero tabla-{num}.txt no existe.\n")

    def linea_fichero(self, num, linea):
            try:
                with open(f"tabla-{num}.txt", "r") as file:
                    lineas = file.readlines()
                    if 1 <=linea and linea<=len(lineas):
                        print(lineas[linea - 1].strip())
                    else:
                        print("Línea fuera de rango.")
            except FileNotFoundError:
                print(f"El fichero tabla-{num}.txt no existe.\n")
    def run(self):
        while True:
            print(self.menu)
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                num = int(input("Ingrese un número entre 1 y 10: "))
                self.guardar_fichero(num)
            elif opcion == "2":
                num = int(input("Ingrese un número entre 1 y 10: "))
                self.leer_mostrar_fichero(num)
            elif opcion == "3":
                num = int(input("Ingrese un número entre 1 y 10: "))
                line_num = int(input("Ingrese el número de línea a mostrar: "))
                self.linea_fichero(num, line_num)
            elif opcion == "4":
                print("¡Hasta luego!")
                break
            else:
                print("Opción inválida. Seleccione nuevamente.")

if __name__ == "__main__":
    root = FicherosProducto()
    root.run()