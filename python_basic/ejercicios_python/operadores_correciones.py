# 1. Calcula el área de un rectángulo con largo = 8 y ancho = 5. Usa la fórmula: área = largo * ancho.
largo = 8
ancho = 5
area = largo * ancho
print(area)

# 2. Calcula el resto de dividir 27 entre 4 usando el operador módulo %.
div = 27 % 4
print(div)

# 3. Dado a = 12 y b = 7, muestra si a es mayor que b (True/False).
a = 12
b = 7
print(a>b)
# 4. Pide dos números al usuario y muestra su suma, resta, multiplicación y división.
num1 = float(input("Dime un numero:"))
num2 = float(input("Dime el segundo numero:"))

suma = num1 + num2
resta = num1 - num2
mult = num1 * num2
division = num1 / num2
print(suma,resta,mult,division)
# 5. Usa operadores lógicos para comprobar: Si a = 5, b = 10 y c = 15, ¿es a menor que b y c mayor que b?
a = 5
b = 10
c = 15
# nos acordamos que and es true si todos sus valores son true
resultado = a<b and c > b
print(resultado)
