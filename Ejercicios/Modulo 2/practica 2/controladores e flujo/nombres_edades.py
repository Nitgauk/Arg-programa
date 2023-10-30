#Crea un diccionario que contenga nombres como claves y edades como valores. Luego,
#utiliza un bucle para recorrer el diccionario e imprimir cada nombre junto con su edad.

diccionario = {
    "Juan": 30,
    "María": 25,
    "Carlos": 35,
    "Ana": 28
}

for nombre, edad in diccionario.items():
    print(f"el nombre {nombre} tiene {edad} años")