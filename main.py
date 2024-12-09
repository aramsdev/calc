import sumar
import resta
import multiplicacion
import dividir
import suma_avanzada

def mostrar_menu():
    print("\nCalculadora")
    print("1. Sumar dos números")
    print("2. Restar dos números")
    print("3. Multiplicar dos números")
    print("4. Dividir dos números")
    print("5. Suma avanzada (N números)")
    print("6. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            print(f"Resultado: {sumar.sumar(a, b)}")
        elif opcion == "2":
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            print(f"Resultado: {resta.restar(a, b)}")
        elif opcion == "3":
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            print(f"Resultado: {multiplicacion.multiplicar(a, b)}")
        elif opcion == "4":
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            try:
                print(f"Resultado: {dividir.dividir(a, b)}")
            except ValueError as e:
                print(e)
        elif opcion == "5":
            numeros = list(map(float, input("Ingresa los números separados por espacios: ").split()))
            print(f"Resultado: {suma_avanzada.suma_avanzada(*numeros)}")
        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()