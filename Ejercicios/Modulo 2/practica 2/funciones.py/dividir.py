def dividir(num1, num2):
    resultado = num1 / num2
    modulo = num1 % num2
    
    return resultado, modulo


val1= float(input("Ingrese el primer numero : "))
val2= float(input("Ingrese el seguno numero : "))

resultado, modulo = dividir(val1, val2) 

print(f"el resultado de la divicion es {resultado} y el residuo es {modulo}")


