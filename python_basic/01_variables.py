### Variables ###

# Se declara una variable de tipo string y se imprime su valor.
my_string_variable = "My String variable"
print(my_string_variable)

# Se declara una variable de tipo entero y se imprime su valor.
my_int_variable = 5
print(my_int_variable)

# Se convierte el entero a string usando str() y se imprime el nuevo valor y su tipo.
my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))  # <class 'str'>

# Se declara una variable booleana (falsa) y se imprime.
my_bool_variable = False
print(my_bool_variable)

# Concatenación de distintas variables en una sola instrucción print.
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

# Uso de la función len() para saber la longitud de la cadena.
print(len(my_string_variable))

# Declaración de múltiples variables en una sola línea (string, string, string, entero).
# Aunque es válido, se recomienda no abusar de esta práctica para mantener el código legible.
name, surname, alias, age = "Unai", "Villar", 'UnaiDev', 17
print("Me llamo:", name, surname, ". Mi edad es:", age, ". Y mi alias es:", alias)

# Inputs: se solicita al usuario que introduzca su nombre y su edad.
# Estas variables serán de tipo string por defecto.
name = input('¿Cuál es tu nombre? ')
age = input('¿Cuántos años tienes? ')
print(name)
print(age)

# Se cambian los valores y tipos de las variables 'name' y 'age' a propósito.
# Esto demuestra que las variables son dinámicas en Python (pueden cambiar de tipo).
name = 14
age = "hola"
print(name)
print(age)

# Declaración de una variable con anotación de tipo 'str'.
# Sin embargo, se sobrescribe con distintos tipos (bool, int, float).
# Python permite esto aunque contradiga la anotación de tipo, ya que no es estrictamente tipado.
address: str = "Mi dirección"
address = True
address = 5
address = 1.2
print(type(address))  # <class 'float'>
