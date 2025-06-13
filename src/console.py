# consola.py

from controller import metFactoriales_controller

def mostrar_menu():
    print("=== Calculadora Matemática (Consola) ===")
    print("1. e^x")
    print("2. sen(x)")
    print("3. cos(x)")
    print("4. arcsen(x)")
    print("5. arccos(x)")
    print("6. senh(x)")
    print("7. cosh(x)")
    print("0. Salir")

def obtener_operacion(opcion):
    operaciones = {
        "1": "exp",
        "2": "sen",
        "3": "cos",
        "4": "arcsen",
        "5": "arccos",
        "6": "senh",
        "7": "cosh"
    }
    return operaciones.get(opcion, None)

def iniciar_consola():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una operación: ")
        if opcion == "0":
            print("Saliendo...")
            break
        operacion = obtener_operacion(opcion)
        if not operacion:
            print("Opción no válida.")
            continue
        try:
            x = float(input("Ingrese el valor de x: "))
            resultado = metFactoriales_controller.calcular(operacion, x)
            print(f"Resultado: {resultado}")
        except ValueError:
            print("Entrada inválida. Intente de nuevo.")

if __name__ == '__main__':
    iniciar_consola()