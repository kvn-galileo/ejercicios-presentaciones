# Ejemplo #5: Escriba un programa que lea del teclado un
# numero entero positivo N mayor que 5 (y verifique que lo
# sea), después genere una lista , y en cada posición X,
# ingrese el valor de (X+1)! , es decir el factorial de X+1. ,
# hasta llegar a la posición N. Luego despliegue la lista.
# Ejemplo:
# N = 5
# lista → [1, 2, 6, 24, 120]
try:
    n = int(input("Enter a number equal or higher than 5: "))

    if (n < 5):
        print("The number must be equal or higher than 5")
    else:
        arr = []
        prev = 1

        for i in range(1, n + 1):
            new_number=i * prev
            arr.append(new_number)
            prev = new_number

        print(arr)

except ValueError:
    print("The thing you enter is not a number")