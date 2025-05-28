### Listas ###

nombres = ["UnaiDEV", "Python", "Copilot"]
for nombre in nombres:
    print(f"Nombre: {nombre}")
    for numero in range(1, 6):
        print(f"  Número: {numero}")
        if numero in range(1, 5):
            print("\t Está dentro \n del rango")
        else:
            print("\t No está dentro \n del rango")