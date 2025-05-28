### Strings ###

my_string = "Mi string"
my_other_string = 'Mi otro string'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

# \n => separa el texto en linea
my_new_line_string = "Este es un string \n con salto de linea"
print(my_new_line_string)

# \t => tabulacion del texto
my_tab_string = "\tEste es un string con tabulacion"
print(my_tab_string)

my_escape_string = "\\tEste es un string \\n escapado"
print(my_escape_string)

# Formateo

name, surname, age = "Unai", "Villar", 17


# .format(en los valores que queremos asginar las variables le ponemos {})
# % (en los valores que queremos asignar las variables le ponemos %s) pero para los nunmeros podemos poner tambien %d

print("Mi nombre es {} {} y mi edad es {}".format(name,surname,age))
print("Mi nombre es %s %s y mi edad es %d" %(name,surname,age))

# Esta es una version mas larga y no es tan recomendada
print("Mi nombre es:" + name + " " + surname + " " "y mi edad es" " " + str(age))

# Otra manera de ejecurtar texto es la siguiente, ponemos las variables dentro de {}.

# Este print estaria mal 
print("Mi nombre es {name} {surname} y mi edad es {age}")
# Este print esta bien, le aplicamos una f al principio del ()
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaquetado de caracteres
language = "python"
# a,b,d,e,f hacen referencia al orden a la palabra Python
a,b,c,d,e,f = language
# si imprimimos a y e, imprimira las letras P y O
print(a)
print(e)

# División

# lo que hace el [1:3] es exactamente lo mismo que antes, recorre desde la letra 1 que seria la y hasta la letra 3 sin contar la 3 osea que cuenta la 2 que es la t
language_slice = language[1:3]
print(language_slice)

# en este caso recorre de la letra 1 al final porque no tiene un numero de STOP
language_slice = language[1:]
print(language_slice)
# este caso recorre desde el final de la palabra hasta la letra 2 que es la o
language_slice = language[-2]
print(language_slice)
# en este caso lo que hace es mostrar las unicas letras que asignamos, evita caracteres
language_slice = language[0:6:2]
print(language_slice)

# Reverse
# el [::-1] lo que hace es revertir la palabra
reversed_language = language[::-1]
print(reversed_language)

# Funciones
"""
En este caso si nosotros hacemos un print con nuestra variable(en este caso language)
y ponemos un . despues de la variable, lo que hacemos es asignar una funcion del lenguaje
vamos a ver unos ejemplos
IMPORTANTE: todas las funciones para que se ejectuen correctamente le aplicamos tambien ()
"""
# .capitalize, aplica la primera letra en mayuscula
print(language.capitalize())
# .upper, aplica mayusculas en toda la variable
print(language.upper())
# .count lo que hace es contar cuantos valores hay de si mismo
print(language.count("t"))
# .isnumeric nos dice si la variable es un numero
print(language.isnumeric())
print("4".isnumeric())
# .lower nos transfiere de mayusculas a minusculas
minu = "HOLA"
print(minu.lower())
"""
aqui estamos concatenando 2 funciones
como ya sabemos .upper y .lower transfiere a mayusculas o minusculas
despues concatenamos otra funcion que verifica si el texto esta en mayuscula o minuscula
"""
print(language.upper().isupper())
print(language.lower().islower())
print(language.upper().islower())
print(language.lower().isupper())
# .startswith nos verifica si la variable comienza por las letras correctas
print(language.startswith("py"))