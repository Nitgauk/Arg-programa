dato = "La ciencia nunca resuelve un problema sin crear otros 10 más."

conteo={
    "a":0,
    "e":0,
    "i":0,
    "o":0,
    "u":0
}

for vocales in dato:
    if vocales in "aeiou":
        conteo[vocales] +=1
        
        
print(conteo)
