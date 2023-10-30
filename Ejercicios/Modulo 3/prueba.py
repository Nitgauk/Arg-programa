archivo = open ("arch.txt", "r")
archivo.write ("probando 1")
archivo.close ()

archivo=open ("arch.txt","r")
for linea in archivo:
    if "probando" in linea:
        print("el archivo se escribio correctamente")
        
archivo.close()