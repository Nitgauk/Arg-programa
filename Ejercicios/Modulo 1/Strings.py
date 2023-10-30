#1. Cree una variable de tipo String llamada cadena que contenga la frase: “Estoy aprendiendo
#Python”. Imprima en pantalla lo resultante.

cadena = "Estoy aprendiendo Python"

print (cadena)

#2. Cree una variable de tipo String llamada párrafo que contenga la sucesión de frases
#siguientes e imprima en pantalla lo resultante.:
#“En Python es posible
#armar un párrafo
#muy sencillamente”

parrafo = "En Python es posible\n\narmar un parrafo\n\nmuy sencillamente "

print (parrafo)

#3. Utilizando la variable cadena creada en el ejercicio 1 use Slicing para asignar a una nueva
#variable llamada hoy las primera dos palabras de la frase en la variable cadena. Imprima en
#pantalla lo resultante.

hoy = cadena [:17]
print (hoy)

#4. Utilizando la variable creada en el ejercicio 2 use Slicing para asignar una nueva variable
#llamada complejo que diga lo siguiente e imprima en pantalla lo resultante.:
#“Python es sencillamente muy posible”

complejo = parrafo [3:13] + parrafo [44:] + parrafo [40:43] +parrafo [12:20]

print (complejo)
