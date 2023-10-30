num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
operacion = input("eliga la operacion (sumar, restar, multiplicar, dividir): ")


try:
    if operacion == "sumar":
        resultado = num1+num2

    elif operacion == "restar":
        resultado = num1-num2

    elif operacion == "multiplicar":
        resultado = num1*num2


    elif operacion == "dividir":
        resultado = num1/num2
    
    
    else:
        print("la operacion ingresada no es valida")
        
except ZeroDivisionError:
    print("no se puede dividir por 0 mi rey")
    
    
if operacion in ["sumar", "restar", "multiplicar", "dividir"]:
    print(f"el resultado de la operacion es {resultado}")


