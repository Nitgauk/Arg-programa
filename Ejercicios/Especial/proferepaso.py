cadena_de_texto = "Hola, ¿Como estás?" #=> se definen con "" o ''
enteros = 5 #=> se definen escribiendo el numero en cuestión
flotantes = 5.0 # flotantes se definen con un numero "." y otro numero
listas = ["contenido", 1, 2.4] #=> Tiene la particularidad de ser mutable
tuplas = ("contenido",1,2.4) #=> Tiene la particularidad de ser inmutable
booleano_v = True
booleano_f = False
diccionarios = {
    "clave": "valor"
#=> el valor puede ser cualquier tipo de dato (listas, tuplas, numeros, flotantes, etc...)
}

len(listas) #=> sacar la longitud expresada en un numero entero
# recordemos que los indices comienzan a partir del numero 0
listas.append("contenido nuevo") #=> añadimos contenido a las listas
print(diccionarios.items())
listas[0] = "1"
print(listas)

if booleano_f: #=> If significa "sí", y en caso de que la condición sea verdadera
# va a permitir que ejecutemos el codigo identado
  print(cadena_de_texto)
elif booleano_f:
# "elif" significa "si nó, intenta esto" generamos una nueva condición
# que en caso de cumplirse, ejecutara el codigo identado
  print(diccionarios)
else:
# "en caso de no cumplirse" siempre que todas las validaciones anteriores sean falsas
# se va a ejecutar siempre este codigo
  print("Ninguna de las anteriores validaciones era verdadera")
  
  for numero in range(1,11): #=> con la palabra reservada for, declararmos un bucle
# en el cual utilizando la palabra in vamos a determinar que objeto vamos a iterar
  print(numero) #=> utilizando la variable que definimos podemos acceder al valor de cada iteración
  while True:
    print(cadena_de_texto)
    break #=> rompemos la ejecución del iterador mas cercano, en este caso el while

# "anidar" significa poner un bucle dentro de otro bucle
# también se utiliza para referirse a los condicionales dentro de condicionales
# En inglés es "nested" #=> "anidado"

while booleano_v:
# "while" significa "mientras" y va a validar que
# la condición sea verdadera antes de volver a iterar
  print(cadena_de_texto)
  break #=> "break" significa "romper" y va a romper la ejecución de
  # cualquier bucle que se esté iterando en ese momento
  # rompiendo siempre el mas cercano
  
# para definir una función utizamos la palabra reservada "def"
def funcion(argumento):
#=> dentro de los parentesis vamos a definir los argumentos
  try: #=> "try" significa intentar, y va a intentar ejecutar el codigo
    if type(argumento) != type(str()):
      raise TypeError("El tipo de dato utilizado no corresponde, debe ser un str")
      # "raise" significa levantar, y con ella podemos tirar un error que nosotros queramos
    print(argumento)
  except TypeError:
    #=> except va a definir que pasa en caso de que lo anterior no logre ejecutarse
    #=> pep8 guia de estilos
    print(argumento * 2)
  return argumento