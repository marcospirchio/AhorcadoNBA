import random

letras_correctas = []
letras_incorrectas = []
vidas=6
aciertos = 0
juego_terminado = False
#Lista con nombres de jugadores
lista_de_jugadores = ['jordan', 'lebron', 'kobe', 'ginobili', 'oberto', 'campazzo', 'curry', 'bird', 'lillard','iverson', 'magic', 'antetokounmpo', 'harden', 'westbrook', 'durant', 'nash', 'barkley', 'chamberlain', 'pippen', 'malone', 'duncan', 'rodman', 'wade','doncic','young','holgrem','davis','tatum','derozan','butler','embiid','jokic','george','booker','towns','mitchell']

# ------------------------------  Funciones -------------------------------------------------------------

def elegir_palabra(lista_palabras):
    #Esta funcion elige una palabra al azar
    palabra_elegida = random.choice(lista_palabras)
    letras_unicas = len(set(palabra_elegida))

    return palabra_elegida,letras_unicas
def pedir_letra():
    letra_elegida = ''
    es_valida = False
    abecedario = 'abcdefghijklmnopqrstuvwxyz'

    while not es_valida:
        letra_elegida = input('Ingresa una letra para adivinar: ').lower()
        if letra_elegida in abecedario and len(letra_elegida) == 1:
            es_valida = True
        else:
            print('Lo siento, debes ingresar una letra de la A a la Z')

    return letra_elegida
def actualizar_tablero(palabra_elegida):
    lista_oculta = []

    for l in palabra_elegida:
        if l in letras_correctas:
            lista_oculta.append(l)
        else:
            lista_oculta.append('-')

    print(' '.join(lista_oculta))
def chequear_letra(letra_elegida, palabra_oculta, vidas, coincidencias):
    fin = False

    if letra_elegida in palabra_oculta and letra_elegida not in letras_correctas:
        letras_correctas.append(letra_elegida)
        coincidencias += 1
    elif letra_elegida in palabra_oculta and letra_elegida in letras_correctas:
        print('Ya has adivinado esa letra, intenta con una nueva.')
    else:
        letras_incorrectas.append(letra_elegida)
        vidas -= 1

    if vidas == 0:
        fin = perder()
    elif coincidencias == letras_unicas:
        fin = ganar(palabra_oculta)

    return vidas, fin, coincidencias
def perder():
    print('JUEGO FINALIZADO\nTe has quedado sin vidas')
    print('El jugador escogido era: ' + palabra)

    return True
def ganar(palabra_descubierta):
    actualizar_tablero(palabra_descubierta)
    print('Felicidades, has adivinado al jugador!')
    return True

# ------------------------------  Codigo principal ------------------------------------------------------

palabra, letras_unicas = elegir_palabra(lista_de_jugadores)
print('Bienvenido al ahorcado de la NBA. Para ganar, debes adivinar al jugador.')
while not juego_terminado:
    print('*' *20 + '\n')
    actualizar_tablero(palabra)
    print('Letras incorrectas: ' + '-'.join(letras_incorrectas))
    print(f'Vidas restantes: {vidas}')
    print('')
    letra = pedir_letra()
    vidas, terminado, aciertos = chequear_letra(letra,palabra,vidas,aciertos)

    juego_terminado = terminado