### Sets ###

# para crear un set, agregamos el valor set, se pueden cerrar con (), {}
# cerrar el set con {} Python lo interpreta como un diccionario
my_set = set()
my_other_set = {}
print(type(my_set))
print(type(my_other_set))

# pero al definir los valores dentro de los {} se vuelve un set
my_other_set = {"Unai", "Villar", 17, 1.74}
print(type(my_other_set))

# calculamos los valores que tenemos dentro del set
print(len(my_other_set))

#print(my_other_set[1]) no podemos acceder a elementos de un set

my_other_set.add("UnaiDev")
print(my_other_set) # Un set no es una estrctura ordenada

my_other_set.add("UnaiDev") # Un set no admite valores repetidos
print(my_other_set)

# esta sintaxis (in) sirve para verificar si un elemento esta dentro del set
print("Unai" in my_other_set)
print("Uni" in my_other_set)

# en un set si que podemos borrar un elemento en concreto
my_other_set.remove("Unai")
print(my_other_set)

# tambien podemos limpiar un set
my_other_set.clear()
print(len(my_other_set))

# tambien podemos utilizar el del que borra el set entero
#del my_other_set
#print(my_other_set) NameError: name 'my_other_set' is not defined

# podemos transformar un set a lista(no es recomendable)
my_set = {"Unai", "Villar" "UnaiDev", 17}
my_list = list(my_set)
print(type(my_list))

my_other_set = {"Python", "Java", "PHP"}

# con .union podemos concatenar 2 sets
my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set.union(my_set.union({"R", "C++"})))) # este union solo sirve para este print(no añade nignu a valor al set)

# con .difference lo que le estamos diciendo es que muestre los valores diferentes de los sets
print(my_new_set.difference(my_set))