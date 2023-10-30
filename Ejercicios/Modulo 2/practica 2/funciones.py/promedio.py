def promedio(*args):
    if len(args)==0:
        return 0
    suma=sum(args)
    promedio = suma / len(args)
    return promedio

numeros1 = [10, 20, 30, 40, 50]
numeros2 = [5, 15, 25]
numeros3 = [100, 200, 300, 400, 500, 600]

resultado1 = promedio(numeros1)
resultado2 = promedio(numeros2)
resultado3 = promedio(numeros3)

print(f"los resultados correspondientes son : promedio 1 {resultado1}, promedio 2: {resultado2} promedio 3 {resultado3}")