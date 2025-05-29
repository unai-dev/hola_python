### Listas ###

my_list = list()
my_other_list = []
print(len(my_list))

# agregamos dentro de [] los valores que queremos en nuestra lista
my_list = [17,34,56,23,77,77]
print(len(my_list))

# da igual el tipo de lista que sea le podemos meter tanto numeros como nombres o palabras
my_other_list =  [17, 1.74, "Unai", "Villar"]
# nos acordamos que el type nos dice la clase de cadena de texto que es una varible, en este caso es una lista
print(type(my_other_list))
print(type(my_list))

# acedemos a los valores de nuestra lista
print(my_other_list[0])
print(my_other_list[2])
print(my_other_list[-1])
print(my_other_list[3])
print(my_other_list[-4])
# IndexError
#print(my_other_list[-5])
#print(my_other_list[4])

# cuenta los valores iguales
print(my_list.count(77))

# esto es un foco de erroes(no recomendable)
age, height, name, surname, = my_other_list[1],my_other_list[0],my_other_list[2],my_other_list[3]
print(age)

# concatenar 2 listas
print(my_list + my_other_list)

# inserta una variable al final de nuestra lista
my_other_list.append("UnaiDev")
print(my_other_list)

# podemos cambiar el orden de la lista agregando la str en la posicion que definimos
my_other_list.insert(1, "Morado")
print(my_other_list)
# cambiamos el valor anterior
my_other_list[1] = "Rojo"
print(my_other_list)

# borramos el valor de una lista
my_list.remove(77)
print(my_list)

# desapilamos el ultimo valor de la lista
print(my_list.pop())
print(my_list)
# desapilamos el valor que definamos de la lista
my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)
# del elimina por indice
del my_list[2]
print(my_list)

# copia la lista a una otra
my_new_list = my_list.copy()
# borra la lista y a la vez imprime la lista copiada
my_list.clear()
print(my_list)
print(my_new_list)
# desordena lam lista
my_new_list.reverse()
print(my_new_list)
# ordena la lista
my_new_list.sort()
print(my_new_list)

print(my_new_list[1:2])
# podemos cambiar las listas por strings
my_list ="Hola Py"
print(my_list)
print(type(my_list))