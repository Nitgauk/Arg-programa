mi_lista = [1,2,"3",0]
def muchas_excepciones(lista):
    for elemento in mi_lista:
        try:
            if elemento == 0:
                resultado=10/elemento
            elif elemento == 2:
                resultado=10/elemento
                
            else:
                resultado = 10 / elemento
                
            print (f"resiltado: {resultado}")
            
        except ZeroDivisionError:
            return  elemento
        except TypeError:
            return resultado
        except NameError:
            return elemento
        except Exception as e:
            return resultado
        
    return elemento
muchas_excepciones(mi_lista)