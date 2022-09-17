import random
import time

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

#Para contabilizar las veces que corre la trivia
iniciar_trivia = True
intentos = 0
lista = []

print("*****Bienvenido a mi trivia sobre la serie How I met your Mother*****\n")
time.sleep(1.5)
print("Pondremos a prueba tus conocimientos\n")
time.sleep(1)
nombre = input(GREEN+"Por favor, ingresa tu nombre para continuar:"+RESET+" ").capitalize()
time.sleep(1)
print(BLUE+f"\nTu nombre es {nombre}"+RESET)
time.sleep(1)
seguro = input(MAGENTA+"\n¿Es esto correcto? Responda con 'si' si lo es: "+RESET).lower()

while seguro != "si":
  nombre = input(GREEN+"\nPor favor, ingresa tu nombre correctamente para continuar:"+RESET+" ").capitalize()
  time.sleep(1)
  print(BLUE+f"\nTu nombre es {nombre}"+RESET)
  time.sleep(1)
  seguro = input(MAGENTA+"\n¿Es esto correcto? Responda con 'si' si lo es: "+RESET).lower()

edad = input(GREEN+"\nPor favor, ingresa tu edad:"+RESET+" ")
time.sleep(1)
while edad.isnumeric() == False or int(edad) not in range(1, 151):
  edad = input(RED+"\nDebes responder con un número entre 1 y 150, ingresa una edad válida:"+RESET+" ")
time.sleep(1)
print(BLUE+f"\nTu edad es {edad} años"+RESET)
time.sleep(1)
seguro = input(MAGENTA+"\n¿Es esto correcto?  Responda con 'si' si lo es: "+RESET).lower()

while seguro != "si":
  edad = input(GREEN+"\nPor favor, ingresa tu edad correcta:"+RESET+" ")
  time.sleep(1)
  while edad.isnumeric() == False or int(edad) not in range(1, 151):
    edad = input(RED+"\nDebes responder con un número entre 1 y 150, ingresa una edad válida:"+RESET+" ")
  print(BLUE+f"\nTu edad es {edad} años"+RESET)
  time.sleep(1)
  seguro = input(MAGENTA+"\n¿Es esto correcto? Responda con 'si' si lo es: "+RESET).lower()
  time.sleep(1)

# Es importante dar instrucciones sobre cómo jugar:
print("\nHola", nombre,", de", edad, "años, responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta. Primero decidiremos con cuántos puntos comenzarás y, para eso, jugarás una 'Random Battle' con la computadora, si ganas comenzarás con los puntos con los que te quedes, si pierdes, con puntos random entre 0 y 5, podrás jugarlo hasta que ganes, si deseas \n")
time.sleep(2)

input(GREEN+"Presiona Enter para continuar\n"+RESET)

iniciar_juego = True

print("*** Bienvenido a la 'Random Battle' ***")
time.sleep(1)
while iniciar_juego == True:
  jugador1 = f"{nombre}"
  jugador2 = "Computadora"
  
  jugador_1_puntos = 20
  jugador_2_puntos = 20
  
  jugador_1_turnos = []
  jugador_2_turnos = []
  
  turno = []
  
  turnos = 0
  jugar = True
  
  print(BLUE+"\nEstos son los puntos con los que comienzan los jugadores\n"+RESET)
  time.sleep(1)
  print(f"{jugador1} comienza con {jugador_1_puntos} puntos")
  print(f"{jugador2} comienza con {jugador_2_puntos} puntos\n")
  input(GREEN+"Presiona Enter para continuar\n"+RESET)
  
  while jugar == True:
    k = random.randint(0,1)
    if jugador_1_puntos <= 0 or jugador_2_puntos <= 0:
      jugar = False
    elif k == 0:
      turnos += 1
      print(f"El turno {turnos} es turno de {jugador1}, se le restará puntos a {jugador2}")
      l = random.randint(0,6)
      jugador_2_puntos -= l
      print(f"Se le restaron"+RED+f" {l} "+RESET+ f"puntos al jugador {jugador2}")
      jugador_1_turnos.append(jugador_1_puntos)
      jugador_2_turnos.append(jugador_2_puntos)
      print(BLUE+f"\nLos puntos de {jugador1} son {jugador_1_puntos} y los de {jugador2} son {jugador_2_puntos}\n"+RESET)
      turno.append("J1")
      input(GREEN+"Presiona Enter para continuar\n"+RESET)
    elif k == 1:
      turnos += 1
      print(f"El turno {turnos} es turno de {jugador2}, se le restará puntos a {jugador1}")
      m = random.randint(0,6)
      jugador_1_puntos -= m
      print(f"Se le restaron"+RED+f" {m} "+RESET+ f"puntos al jugador {jugador1}")
      jugador_1_turnos.append(jugador_1_puntos)
      jugador_2_turnos.append(jugador_2_puntos)
      print(BLUE+f"\nLos puntos de {jugador1} son {jugador_1_puntos} y los de {jugador2} son {jugador_2_puntos}\n"+RESET)
      turno.append("J2")
      input(GREEN+"Presiona Enter para continuar\n"+RESET)
  
  
  print("*** Secuencia de puntos ***")
  print("Nr", "Turno", f"{jugador1}", f"{jugador2}", sep="\t\t")
  time.sleep(1)
  for x in range(0,turnos):
    print(f"{x+1}" + "\t\t" + f"{turno[x]}" + "\t\t\t" + f"{jugador_1_turnos[x]}" + "\t\t\t\t" + f"{jugador_2_turnos[x]}")

  print(BLUE+"\n¿Deseas jugar nuevamente?\n"+RESET)
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar, y presiona Enter: ").lower()
  print()
  
  if repetir_trivia != "si":
    iniciar_juego = False

if jugador_1_turnos[turnos-1] <= 0:
  puntaje = random.randint(0,6)
elif jugador_2_turnos[turnos-1] <= 0:
  puntaje = jugador_1_turnos[turnos-1]

for x in range(5,0,-1):
  print("La trivia comenzará en ", x, "segundos""\t\t", x*"*")
  time.sleep(1) #Lo más cercano a 5 segundos reales seria 1.5, pero se hace larga la espera
  
  #PARA PONER LOS INTENTOS
while iniciar_trivia == True:
  intentos += 1
  lista.clear()
  lista = [puntaje]
  print(GREEN+"\nComenzarás este intento con ",puntaje, "puntos\n"+RESET)
  time.sleep(1)
  print(BLUE+"Intento número:", intentos,""+RESET)
  time.sleep(1)
  input("\nPresiona Enter para continuar")
  p = 0
  
  #Listas de preguntas, respuestas y opciones
  preguntas = ["¿Cuál es el segundo nombre del hijo de Marshall y Lily?\n", "¿Cuáles son las iniciales de la madre en HIMYM?\n", "¿Cómo se llama la segunda parte de The Playbook?\n", "¿Cómo se llama el bar al que van los protagonistas?\n", "¿Cuántos episodios tiene HIMYM? Puedes pedir una pista, escribiendo pista!\n", "¿De qué color es el paraguas de la mamá?\n"]
  respuestas = ["Anastasio", "Jonathan", "Diego", "Wait for it","F. M.","D. M.","T. M.","T. N.", "The Playbook II: Electric Boogaloo", "The Playbook II: Electric Bangaloo", "The Playbook II: Electric Switcheroo", "The Playbook II: General Electrics","McLaren's Pug", "MacLaren's Bar", "McLaren's Pub", "McLovin's Bar", "Azul", "Amarillo", "Verde", "Negro"]
  opciones = ["a", "b", "c", "d", "stinson", 208]
  
  # Pregunta 1
  print(BLUE+f"\n{str(p+1)}) {preguntas[p]}"+RESET)
  time.sleep(1)
  for x in range(0,4):
    print(f"{opciones[x]}) {respuestas[x+(p*4)]}")

  time.sleep(1)
    
  res_1 = input("\nEscriba la respuesta, por favor: ").lower()
  
  while res_1 not in opciones:
    res_1 = input(RED+f"\nDebes responder {opciones[0]}, {opciones[1]}, {opciones[2]} o {opciones[3]}. Ingresa nuevamente tu respuesta:"+RESET+" ").lower()
  
  if res_1 == opciones[0]:
    r = random.randint(0,10)
    puntaje -= r
    lista.append(-abs(r))
    print(RED+"\n¡Incorrecto!", nombre, ", Anastasio es el nombre del aliado de Jolyne Cujoh.\n"+RESET)
    time.sleep(1)
  elif res_1 == opciones[1]:
    r = random.randint(0,10)
    puntaje -= r
    lista.append(-abs(r))
    print(RED+"\n¡Incorrecto!", nombre, ", Jonathan Joestar es el primer JoJo\n"+RESET)
    time.sleep(1)
  elif res_1 == opciones[2]:
    r = random.randint(0,10)
    puntaje -= r
    lista.append(-abs(r))
    print(RED+"\n¡Incorrecto!", nombre, ", Diego Brando es el nombre alternativo de Dio en 'Steelball Run'\n"+RESET)
    time.sleep(1)
  elif res_1 == opciones[4]:
    s = 1000
    puntaje += s
    lista.append(+abs(s))
    print(MAGENTA+"\nEsto va a ser legen-, espera por ello, dario, legendario\n"+RESET)
    time.sleep(1)
  else:
    s = random.randint(5,20)
    puntaje += s
    lista.append(+abs(s))
    print(CYAN+"\n¡Muy bien, ", nombre, "!\n"+RESET)
    time.sleep(1)
    
  print(GREEN+nombre, ", tu puntaje actual es de ", puntaje, "\n"+RESET)
  time.sleep(1)
  
  # Pregunta 2
  p += 1
  print(BLUE+f"\n{str(p+1)}) {preguntas[p]}"+RESET)
  time.sleep(1)
  for x in range(0,4):
    print(f"{opciones[x]}) {respuestas[x+(p*4)]}")

  time.sleep(1)
  
  res_2 = input("\nEscriba la respuesta, por favor: ").lower()
  
  while res_2 not in opciones:
    res_2 = input(RED+f"\nDebes responder {opciones[0]}, {opciones[1]}, {opciones[2]} o {opciones[3]}. Ingresa nuevamente tu respuesta:"+RESET+" ").lower()
  
  if res_2 == opciones[0]:
    r = random.randint(0, 5)
    puntaje -= r
    lista.append(-abs(r))
    print(RED+"\n¡Incorrecto!", nombre, ", F. M. es Frecuencia Modulada\n"+RESET)
    time.sleep(1)
  elif res_2 == opciones[1]:
    r = random.randint(0, 5)
    puntaje -= r
    lista.append(-abs(r))
    print(RED+"\n¡Incorrecto!", nombre, ", D. M. es Diego Maradona\n"+RESET)
    time.sleep(1)
  elif res_2 == opciones[3]:
    r = random.randint(0, 5)
    puntaje -= r
    lista.append(-abs(r))
    print(RED+"\n¡Incorrecto!", nombre, ", T. N. es Tracy Nance\n"+RESET)
    time.sleep(1)
  elif res_2 == opciones[2]:
    s = random.randint(5,11)
    puntaje += s
    lista.append(+abs(s))
    print(CYAN+"\n¡Muy bien, ", nombre, "!\n"+RESET)
    time.sleep(1)
  
  print(GREEN+nombre, ", tu puntaje actual es de ", puntaje, "\n"+RESET)
  time.sleep(1)
  
  # Pregunta 3
  p += 1
  print(BLUE+f"\n{str(p+1)}) {preguntas[p]}"+RESET)
  time.sleep(1)
  for x in range(0,4):
    print(f"{opciones[x]}) {respuestas[x+(p*4)]}")

  time.sleep(1)
  
  res_3 = input("\nEscriba la respuesta, por favor: ").lower()
  
  while res_3 not in opciones:
    res_3 = input(RED+f"\nDebes responder {opciones[0]}, {opciones[1]}, {opciones[2]} o {opciones[3]}. Ingresa nuevamente tu respuesta:"+RESET+" ").lower()
  
  if res_3 == opciones[0]:
    r = random.randint(5, 10)
    puntaje -= r
    lista.append(-abs(r))
    print(RED+"\n¡Incorrecto!", nombre, ", Electric Boogaloo es el nombre de la película original\n"+RESET)
    time.sleep(1)
  elif res_3 == opciones[2]:
    r = random.randint(5, 10)
    puntaje -= r
    lista.append(-abs(r))
    print(RED+"\n¡Incorrecto!", nombre, ", Swichteroo no va en el contexto de hook ups\n"+RESET)
    time.sleep(1)
  elif res_3 == opciones[3]:#Este trabajo es propiedad de George Humberto Bernui Urday
    r = random.randint(5, 10)
    puntaje -= r
    lista.append(-abs(r))
    print(RED+"\n¡Incorrecto!", nombre, ", esta es una marca de instrumentos eléctricos\n"+RESET)
    time.sleep(1)
  elif res_3 == opciones [1]:
    s = random.randint(10,20)
    puntaje += s
    lista.append(+abs(s))
    print(CYAN+"\n¡Muy bien, ", nombre, "!\n"+RESET)
    time.sleep(1)
  
  print(GREEN+nombre, ", tu puntaje actual es de ", puntaje, "\n"+RESET)
  time.sleep(1)
  
  # Pregunta 4
  p += 1
  print(BLUE+f"\n{str(p+1)}) {preguntas[p]}"+RESET)
  time.sleep(1)
  for x in range(0,4):
    print(f"{opciones[x]}) {respuestas[x+(p*4)]}")

  time.sleep(1)
    
  res_4 = input("\nEscriba la respuesta, por favor: ").lower()
    
  while res_4 not in opciones:
    res_4 = input(RED+f"\nDebes responder {opciones[0]}, {opciones[1]}, {opciones[2]} o {opciones[3]}. Ingresa nuevamente tu respuesta:"+RESET+" ").lower()
  
  if res_4 == opciones[0]:
    s = 5
    puntaje += s
    lista.append(+abs(s))
    print(RED+"\n¡Incorrecto!\n"+RESET)
    time.sleep(1)
  elif res_4 == opciones[1]:
    r = 5
    puntaje -= r
    lista.append(-abs(r))
    print(RED+"\n¡Incorrecto!\n"+RESET)
    time.sleep(1)
  elif res_4 == opciones[3]:
    lista.append(-abs(puntaje/2))
    puntaje /= 2
    print(RED+"\n¡Incorrecto!\n"+RESET)
    print(YELLOW+"Se dividió tu puntaje entre 2\n"+RESET)
    time.sleep(1)
  elif res_4 == opciones[2]:
    lista.append(+abs(puntaje))
    puntaje *= 2
    print(CYAN+"\n¡Muy bien, ", nombre, "!\n"+RESET)
    print(YELLOW+"Tu puntaje se multiplicó por 2\n"+RESET)
    time.sleep(1)
  
  print(GREEN+nombre, ", tu puntaje actual es de ", puntaje, "\n"+RESET)
  time.sleep(1)
  
  # Pregunta 5
  p += 1
  print(BLUE+f"\n{str(p+1)}) {preguntas[p]}"+RESET)
  time.sleep(1)
  
  res_5 = input("Escriba la respuesta, por favor: ")
  
  while res_5 != str(opciones[5]):    
    if res_5.isnumeric() == False and res_5.lower() == "pista":
      res_5 = input(GREEN+"\nEl número está entre 175 y 225, pruebe con otro número:"+RESET+" ")
    elif res_5.isnumeric() == False and res_5.lower() != "pista":
      res_5 = input(RED+"\nIntenta escribiendo 'pista', sin las comillas:"+RESET+" ")
    elif res_5.isnumeric() == True and int(res_5) < opciones[5]:
      res_5 = input(GREEN+"\nEl número es más grande, pruebe con otro:"+RESET+" ")
    elif res_5.isnumeric() == True and int(res_5) > opciones[5]:
      res_5 = input(GREEN+"\nEl número es más pequeño, pruebe con otro:"+RESET+" ")
      
  s = 20
  puntaje += s
  lista.append(+abs(20))  
  print(CYAN+"\n¡Correcto!\n"+RESET)
  time.sleep(1)
  print(GREEN+f"{nombre}, tu puntaje actual es de {puntaje}"+RESET)
              
  time.sleep(1)
  
  #Pregunta 6
  p += 1
  print(BLUE+f"\n{str(p+1)}) {preguntas[p]}"+RESET)
  time.sleep(1)
  colores = [MAGENTA, BLUE, GREEN, YELLOW]
  for x in range(0,4):
    print(f"{opciones[x]}) "+colores[x]+f"{respuestas[x+((p-1)*4)]}"+RESET)

  time.sleep(1)
  
  res_6 = input("\nEscriba la respuesta, por favor: ").lower()
  
  while res_6 not in opciones:
    res_6 = input(RED+f"\nDebes responder {opciones[0]}, {opciones[1]}, {opciones[2]} o {opciones[3]}. Ingresa nuevamente tu respuesta:"+RESET+" ").lower()
  
  if res_6 == opciones[0]:
    r = random.randint(0,5)
    puntaje -= r
    lista.append(-abs(r))
    print(RED+"\n¡Incorrecto, ", nombre, "!\n"+RESET)
    time.sleep(1)
  elif res_6 == opciones[2]:
    r = random.randint(0,5)
    puntaje -= r
    lista.append(-abs(r))
    print(RED+"\n¡Incorrecto, ", nombre, "!\n"+RESET)
    time.sleep(1)
  elif res_6 == opciones[3]:
    r = random.randint(0,5)
    puntaje -= r
    lista.append(-abs(r))
    print(RED+"\n¡Incorrecto, ", nombre, "!\n"+RESET)
    time.sleep(1)
  elif res_6 == opciones[1]:
    s = random.randint(5,11)
    puntaje += s
    lista.append(+abs(s))
    print(CYAN+"\n¡Muy bien, ", nombre, "!\n"+RESET)
    time.sleep(1)
    
  print(GREEN+nombre, ", tu puntaje actual es de ", puntaje, ", procederemos a modificar tu puntaje a través de nuestro dado de puntaje final\n"+RESET)
  
  time.sleep(1)
  
  b = input(GREEN+"\nIngresa un número del 1 al 10, que usaremos para cambiar tus puntos: "+RESET)

  time.sleep(1)
  
  while b.isnumeric() == False or int(b) not in range(1,11):
    b = input(GREEN+"\nIngresa un número del 1 al 10:"+RESET+" ")
  time.sleep(1)
  
  b = int(b)
  print(BLUE+"\nEstas son las reglas del dado\n"+RESET)
  
  time.sleep(1)
  
  print(YELLOW+f"Si cae en 1, se suman {b} puntos")
  print(f"Si cae en 2, se suman {2*b} puntos")
  print(f"Si cae en 3, se restan {3*b} puntos ")
  print(f"Si cae en 4, se multiplican los puntos por {b/2}")
  print(f"Si cae en 5, se divide entre {b} y se redondea hacia abajo")
  print(f"Si cae en 6, se multiplica por {b}"+RESET)
  
  time.sleep(4)
  input(BLUE+"\nPresiona Enter para hacer rodar nuestro dado\n"+RESET)
  
  a = random.randint(1, 6)
  b = int(b)
  print(RED+f"El dado cayo en el: {a}\n"+RESET)

  time.sleep(1)
  
  if a == 1:
    puntaje += b
  elif a == 2:
    puntaje += 2*b
  elif a == 3:
    puntaje -= 3*b
  elif a == 4:
    puntaje *= b/2
  elif a == 5:
    puntaje //= b
  else:
    puntaje *= b
  
    
  print(GREEN + "\nGracias por jugar a mi trivia,", nombre, ", tu intento fue el número", intentos,
          "y tu puntaje final fue de", puntaje, "puntos." + RESET)

  time.sleep(1)

  print(BLUE + "\n¿Deseas intentar la trivia nuevamente?\n" + RESET)
  repetir_trivia = input(GREEN + "Ingresa 'si' para repetir, o cualquier tecla, y luego Enter, para finalizar:" + RESET + " ").lower()

  if repetir_trivia != "si":
    print()
    time.sleep(1)
    print(BLUE + f"Comenzaste tu intento número {intentos} con el siguiente puntaje: {lista[0]}\n" + RESET)
    for x in range(1, 7):
        print(f"En la pregunta {x} conseguiste estos puntos:\t {lista[x]}")
        time.sleep(1)
    print()
    print(BLUE + f"Tu total de puntos conseguidos, sin contar la ruleta, ni los puntos con los que comenzaste, fue: {sum(lista) - lista[0]} puntos" + RESET)
    time.sleep(1)
    print(GREEN + f"\nEspero que lo hayas pasado bien, {nombre}, hasta pronto!" + RESET)
    iniciar_trivia = False  # Cambiamos el valor de iniciar_trivia a False para evitar que se repita.
  else:
    puntaje = random.randint(0, 6)
    print("\nComenzarás este intento con un puntaje random entre 0 y 5\n")