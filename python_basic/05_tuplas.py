### Tuples ###

# nombramos a la tupla
my_tuple = tuple()
my_other_tuple = ()
# asignamos los valores de la tupla
my_tuple = (17, 1.74, "Unai", "Villar")
# imprimos la tupla
print(my_tuple)
print(type(my_tuple)) 

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) IndexError
#print(my_tuple[-7]) IndexError

# count como ya sabemos cuenta el numero de valores que hay de la misma variable
# index te dice el numero donde se encuentra ese valor en la lista
print(my_tuple.count("Unai"))
print(my_tuple.count("UnaiDev"))
print(my_tuple.index("Villar"))
print(my_tuple.index("Unai"))

# a diferencia de las listas las tuplas son inmutables, basicamente no se pueden modificar o manipular
#my_tuple[1] = 1.90 IndexError

# las tuplas no son mutables pero podemos sumarlas
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

# de esta manera cambiamos una tupla a una lista
my_tuple = list(my_tuple)
print(type(my_tuple))

# de esta manera ya podemos cambiar los valores de nuestra "tupla/lista"
my_tuple[3] = "UnaiDev"
my_tuple.insert(1, "Azul")
print(my_tuple)

"""
las tuplas siempre son seguras de la manera que no tengamos que cambiar nada a futuro
es mejor que una lista porque es menos lio y evitas erroes de valores
pero a futuro puedes cambiar a lista y manipular los datos
"""

# si queremos volver a que sea una tupla de nuevo hacemos lo siguiente: 
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

# con del podemos borrar la variable entera, es como un clear
#del my_tuple
#print(my_tuple)

del my_tuple[2]
print(my_tuple)