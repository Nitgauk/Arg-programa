# la cualdiades de nuestro heroe
nombre = "Máximo" #=> Maximo nombre de heroe(?)
nivel = 1
ataque = nivel
vida = nivel * 10
mochila = []

# definimos cuales son las criaturas que hay en el bosque
criaturas_del_bosque = {
    "duende" : {
        "vida": 2,
        "ataque":1,
        "dialogo": "*El duende te gruñe y atina a morderte*"
        },
    "hada" : {
        "vida": 1,
        "ataque":2,
        "dialogo": "*el hada se te acerca revoloteando* ¿Como estás aventurero? ¿Que estás buscando por aquí?"
        },
    "dragón" : {
        "vida": 20,
        "ataque":10,
        "dialogo": "*Cuando intentas hablar con el dragón, el mismo utiliza su aliento de fuego para calcinarte*"
        #"comportamiento": "agresivo"
        },
    "unicornio" : {
        "vida": 10,
        "ataque":5,
        "dialogo": "*Al acercarte al unicornio el mismo te apunta con su cuerno y sientes una nova sanadora*"
    },
    "lobo" : {
        "vida": 5,
        "ataque":3,
        "dialogo": "*Te acercas a acariciar al lobo y el mismo se deja acariciar*"
        },
    #=> en python si nosotros dejamos una "trailing coma" o sea, una coma al final, no va a pasar nada
    # Pero en otros lenguajes de programación, esto se interepta como un error de sintaxis
}

# Definimos los artefactos que están en el bosque
lista_de_artefactos = [
    "mapa del tesoro",
    "espada afilada",
    "poción mágica",
    "herramientas de herrero"
    ]

def comenzar_aventura():
  # la cualdiades de nuestro heroe
  nombre_heroe = "Máximo" #=> Maximo nombre de heroe(?)
  nivel_heroe = 1
  ataque_heroe = nivel # + 100
  vida_heroe = nivel * 10
  mochila_heroe = list() #=> las listas vacías habría que expresarlas con la función list()
  # [] => () => {}
  # list() => tuple() => dict()
  # definimos cuales son las criaturas que hay en el bosque
  criaturas_del_bosque = {
      "duende" : {
          "vida": 2,
          "ataque":1,
          "dialogo": "*El duende te gruñe y atina a morderte*"
          },
      "hada" : {
          "vida": 1,
          "ataque":2,
          "dialogo": "*el hada se te acerca revoloteando* ¿Como estás aventurero? ¿Que estás buscando por aquí?"
          },
      "dragón" : {
          "vida": 20,
          "ataque":10,
          "dialogo": "*Cuando intentas hablar con el dragón, el mismo utiliza su aliento de fuego para calcinarte*"
          },
      "unicornio" : {
          "vida": 10,
          "ataque":5,
          "dialogo": "*Al acercarte al unicornio el mismo te apunta con su cuerno y sientes una nova sanadora*"
      },
      "lobo" : {
          "vida": 5,
          "ataque":3,
          "dialogo": "*Te acercas a acariciar al lobo y el mismo se deja acariciar*"
          },
      #=> en python si nosotros dejamos una "trailing coma" o sea, una coma al final, no va a pasar nada
      # Pero en otros lenguajes de programación, esto se interepta como un error de sintaxis
  }
  # Definimos los artefactos que están en el bosque
  lista_de_artefactos = [
      "mapa del tesoro",
      "espada afilada",
      "poción mágica",
      "herramientas de herrero"
      ]
  # predefiniciones
  movimientos_posibles = ("izquierda", "derecha")
  acciones_posibles = ("atacar","huir","hablar")
  # Presentación de la aventura
  print("Luego de una noche llena de conflictos, la luz del sol te despierta, parece que ya ha amanecido")
  print("Te haz adentrado en el bosque con el objetivo de recuperar el mapa del tesoro para salvar a tu pueblo")
  print("Incontables peligros te han acechado hasta ahora, y no sabes cuales están por venir")
  print("luego de apagar tu fogata y prepararte para continuar avanzando")
  print("dos senderos se bifurcan, tus opciones son:"
  , movimientos_posibles )

  #Erorr de Unidecode a la hora de definir variables con apostrofes o tildes
  while nivel < 3 or vida_heroe > 0: #=> or and
    movimiento = input("¿Que sendero eliges? ")
    if movimiento == movimientos_posibles[0]: #=> izquierda
      enemigo = choice(list(criaturas_del_bosque.keys()))
      vida_enemigo = criaturas_del_bosque[enemigo]["vida"]
      ataque_enemigo = criaturas_del_bosque[enemigo]["ataque"]
      dialogo_enemigo = criaturas_del_bosque[enemigo]["dialogo"]
      print(
          "Luego de avanzar por un camino entre arboles y lianas,"+
          "llegas a un claro donde la luz del sol se refleja contra un pequeño lago"
          )
      print(f"miras a tu alrededor un rato y te encuentras con un {enemigo}")
      while vida_enemigo > 0: #=> mientras el enemigo tenga mas de 0 de vida
        print("tus opciones son: ", acciones_posibles )
        accion = input("¿Que quieres hacer? ")
        if accion == acciones_posibles[0]: #=> atacar
          print(f"te acercas hacia el enemigo y lo atacas con tu espada, infligiendo {ataque_heroe} de daño")
          vida_enemigo = vida_enemigo - ataque_heroe
          if vida_enemigo > 0:
            print("el enemigo recibe el golpe y no está muy contento, se da vuelta hacia ti y te ataca fuertemente")
            print(f"te inflinge {ataque_enemigo} de daño")
            vida_heroe = vida_heroe - ataque_enemigo
        if accion == acciones_posibles[1]: #=> huír
          print("Huyes despavorido de tu enemigo y logras escapar")
          # if no logramos escapar #=> definimos como escapar según aleatoriedad
          # el enemigo nos golpea o persigue
          break
        if accion == acciones_posibles[2]: #=> hablar
          print("te acercas a la criatura e intentas entablar una conversación")
          print(dialogo_enemigo)
          # if comportamiento == comportamientos_posibles[0]: #=> agresivo
          #    print("la criatura te inflinge {ataque_enemigo} de daño")
          #    vida_heroe = vida_heroe - ataque_enemigo
      else:
        # en caso de que el enemigo tenga 0 o menos de vida, se ejecuta este codigo
        print("haz matado a tu enemigo, puedes continuar con tu aventura")
        nivel_heroe += 1
        vida_heroe += nivel_heroe * 10
    if movimiento == movimientos_posibles[1]:# derecha
      recompensa = choice(lista_de_artefactos)
      if "mapa del tesoro" in mochila_heroe:
        print("Utilizando el mapa del tesoro, logras encontrar el castillo donde se encuentra el idolo dorado")
        print("luego de pelear contra incontables enemigos sales vencedor y logras recuperarlo")
        print("ahora tu pueblo tiene esperanzas y podrás liberarlo usando los poderes que te brinda el idolo dorado")
        break
      print("avanzas por un pantano el cual luego de traspasar entre el fango y la mugre, logras encontrar unas ruinas")
      print("luego de adentrarte en ellas durante horas, logras encontrar un cofre")
      print(f"al abrirlo, hay {recompensa} en su interior")
      print("guardas el artefacto en tu mochila")
      mochila_heroe.append(recompensa)
  if vida_heroe > 0:
    print("haz aprendido mucho en tu viaje, logras volver a tu pueblo y liberarlo de la tiranía")
  else:
    print("Haz muerto en tu aventura, tu pueblo está condenado a la destruccion total y es tu culpa")
    
def criaturas_del_bosque()
  diccionario = {

  }
  enemigo_a_devolver = choice(list(diccionario.keys()))
  stats = diccionario[enemigo_a_devolver]
  return enemigo_a_devolver, stats #=> siempre que separemos los resultados con una coma
  # lo que va a devolver es una tupla
  # siempre que usemos una tupla, podemos definir variables usando
  # "," siempre y cuando haya la misma cantidad
  # de variables que de objetos dentro de la tupla

enemigo, stats = criaturas_del_bosque()

for criatura, stats in criaturas_del_bosque.items():
  print(criatura)
  print(stats)

for criatura, stats in criaturas_del_bosque.items():
  print(criatura)
  print(stats)
  
comenzar_aventura(
)

list(criaturas_del_bosque.keys())

# Posibilidades de nuestro codigo

#Una de las posibilidades es que cuando avancemos en una dirección, lo que suceda sea aleatorio, tanto encontrar un objeto o pelear contra un enemigo
#la espada afilada nos aumente el ataque de nuestro personaje multiplicandolo x2
#haya nuevos terrenos o posibilidaades los cuales estén dentro de un diccionario

terrenos_a_vencer = {
    "Bosque": {
        "descripción": "",
        "enemigos_posibles": criaturas_del_bosque,
        "penalizadores/bonificadores": {
            "penalizador":"-1 de vida por turno"
            }
        },
    "Tundra": {
        "descripción": "",
        "enemigos_posibles": "" #criaturas_de_la_tundra a desarrollar
    }
}

niveles = {
    "nivel 1": comenzar_aventura, #=> es blanco
    "nivel 2": print #=> es como amarillo
}

niveles["nivel 2"]("Hola")