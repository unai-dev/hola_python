### Dictionaries ###

# comenzamos creando un diccionario con dict()
my_dict = dict()
my_other_dict = {}
print(type(my_dict))
print(type(my_other_dict))

"""
para empezar añadiendo elementos, nos fijamos en la estructura que esta compuesta:
por una clave y un valor: "Nombre"(clave) "Unai"(valor)
"""
my_other_dict = {"Nombre":"Unai", "Apellido":"Villar", "Edad":17, 1:"Python"}

my_dict = {
    "Nombre":"Unai",
    "Apellido":"Villar",
    "Edad":17,
    "Lenguajes": {"Python","R","PHP"},
    1:1.74
}
print(my_other_dict)
print(my_dict)

# nada mas nos mostrara 4 elementos porque solo hemos añadido 4 valores las claves no cuentan
print(len(my_other_dict))
# pero en este caso tenemos 5 por el valor lenguajes, que lenguajes es una clave y los valores son Python,R etc...
print(len(my_dict))

# de esta manera podemos acceder a nuestro diccionario
print(my_dict ["Nombre"])
# aparte de acceder al valor en concreto tambien podemos modificarlo
my_dict["Nombre"] = "UnaiDev"
print(my_dict["Nombre"])

print(my_dict[1]) # tambien podemos buscar numeros int

# de esta manera podemos añadir datos al diccionario
my_dict["Calle"] = "Calle UnaiDev"
print(my_dict)

# del en este caso es de la manera que podemos eliminar elementos de un diccionario sin afectar a todo el dict
del my_dict["Calle"]
print(my_dict)
# en los diccionarios verifica si un valor esta buscando por la clave no por el valor
print("Unai" in my_dict)
print("Nombre" in my_dict)

print(my_dict.items()) # .items tenemos un listado de cada uno de los items
print(my_dict.keys()) # .keys tenemos un listado de las claves
print(my_dict.values()) # .values tenemos un listado de los valores

my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict)
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict, "UnaiDev")
print((my_new_dict))

my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))
print(tuple(my_new_dict))
print(set(my_new_dict))