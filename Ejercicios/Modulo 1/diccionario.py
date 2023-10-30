# 1. Cree un diccionario llamado ingredientes que contenga como clave nombres de ingredientes y
# como valor su cantidad según alguna receta de cocina. 

ingredientes = {
    "revanada de pan" : 2,
    "aguacate maduro" : 1,
    "huevos": 2,
    "sal y pimienta": "al gusto"
}

print(ingredientes)

# 2. Utilizando la lista persona cree un diccionario llamado usuario que reemplace la estructura de
# lista creada en el Ejercicio V.1 con sus respectivas claves y valores. TIP: dict = {“clave”:”valor”}


persona = ["Agustin","Ferrer", 41171629,1998,0]
usuario = {
    "Nombre" : persona[0],
    "Apellio" : persona [1],
    "DNI" : persona [2],
    "clave": persona [3]
}
print(usuario)



