#1. Crea una lista llamada `numeros` con los números del 1 al 5. Luego, accede al tercer elemento
#de la lista e imprímelo en la pantalla. 

numeros = [1,2,3,4,5]
print (numeros[2])
#2. Declara una lista llamada `colores` con los colores "rojo", "verde" y "azul". Cambia el segundo
#elemento de la lista a "amarillo" y después imprime la lista completa.

colores = ["rojo","verde","azul"]
print (colores)
colores[1] = "amarillo" 
print(colores)

#3. Inicializa una lista llamada `frutas` con las frutas "manzana", "naranja" y "uva". Agrega "banana"
#como cuarto elemento y luego elimina la fruta "naranja" de la lista. Imprime la lista final resultante.

frutas = ["manzana","naranja","uva"]
frutas = frutas + ["banana"]
del frutas [1]

print (frutas)

#4. Cree una lista llamada persona que contenga sus datos personales: Nombre, apellido, DNI,
#Año de Nacimiento, Lugar de Nacimiento y Clave. NOTA: DNI y Año de Nacimiento deben ser
#Enteros, no Strings y Clave debe ser el número 0. Imprima en pantalla lo resultante.

persona = ["Agustin","Ferrer", 41171629,1998,0]
print (persona)

#5. Utilice la lista persona creada en el ejercicio 1 y asigne a una nueva variable llamada
#clave_personal la cual deberá tener de valor la multiplicación del campo DNI y el campo Año de
#Nacimiento. Dicha clave generada y guardada en la variable clave_personal debe sustituir el
#campo clave de la lista persona. Imprima en pantalla lo resultante.

cleve_personal = persona[2]* persona[3]
persona[4] = cleve_personal

print(persona)


#6. Cree una lista llamada ingredientes que contenga los ingredientes de alguna receta de cocina.
#Utilice los métodos propios de las listas para ordenar alfabéticamente la lista de ingredientes y
#luego ordenela inversamente.

ingredientes_ensalada = ["tomate","mozzarella","albahaca","aceite de oliva","vinagre balsamico"]
ingredientes_ensalada_ordenada = sorted(ingredientes_ensalada)
print (ingredientes_ensalada_ordenada)
