"""
PRUEBAS DE RETO
"""
"""
Programa para ayudar a jóvenes de 15 años prepararse para la prueba de matemáticas en el examen PISA
Proyecto Integrador: Güsenville

Autores:
José Antonio Juárez Pacheco   A00572186
Armando Terrazas Gómez        A01640924
Lunes 18 de octubre de 2021
"""

from random import randint,uniform
from time import sleep
from os import getcwd,remove,path
from pathlib import Path
from math import hypot
from statistics import median



#FUNCIONES
def crea_rutaDeCarpetas():
    directorio = getcwd() #Obtener tu path de la carpeta en donde tienes guardado este código 
    Path('gusenville').mkdir(exist_ok=True) #Crea la carpeta si no existe y si ya existe no pasa nada
    if not path.exists(f'{directorio}/gusenville/jugadores.csv'): #Verifica que el archivo exista. Devuelve un valor booleano (True or False)
        
        with open(f'{directorio}/gusenville/jugadores.csv','w',encoding="UTF-8") as file:
            file.write('NOMBRE,EDAD,VIDAS RESTANTES,RANGO\n')

    with open(f'{directorio}/gusenville/jugadores.csv','r') as file1: #Convierte a lista de strings
        matrix = []
        for row in file1:
            matrix.append(row)

        lista = []       
        for i in matrix: #Convierte a lista de listas
            lista.append(i.strip().split(','))
    return lista
        
def guarda_datos(players): #Recibe como argumento la lista de la función anterior (datos históricos del juego) más los datos de la corrida actual
    directorio = getcwd()
    with open(f'{directorio}/gusenville/jugadores.csv','w') as myFile: #Sobreescribir con los nuevos datos
        for run in players:
            data = ','.join(run)
            myFile.write(f'{data}\n')
    

def imprime_tabla(ma): #Imprime la matriz de la función guarda_datos(players)
    print("\tNOMBRE\t\tEDAD\t  VIDAS RESTANTES\tRANGO")
    print('-------------------------------------------------------------------------------')
    for i in range(1,len(ma)):
        for j in range(len(ma[1])):
            print(f"\t{ma[i][j]}", end="\t   ")
        print()
    print()

def imprime_pregunta(level,first,corrects,lives,question): #Nivel, #Tipos de enemigos en matriz, Rango de datos para los variables 1,2 y 3; variable firstTime, número de correctas, Nivel actual, número de pregunta
    
    #Formato de matriz de banco de preguntas: [[pregunta1, solución1],[pregunta2, solución2]]
    
    if level == 1:
        datoVariable1 = randint(1,100)
        datoVariable2 = randint(1,100)
        datoVariable3 = randint(1,10)
        
        preguntasNivel = [[f'Pepito quiere {datoVariable1} manzanas y cada {datoVariable2} manzanas cuesta ${datoVariable3} ¿Cuánto dinero necesita para comprar sus manzanas?',datoVariable1/datoVariable2*datoVariable3],[f'Mei-Ling cambió {datoVariable1} dólares de Singapur en rands sudafricanos con este tipo de cambio. Mei-Ling se enteró de que el tipo de cambio entre el dólar de Singapur y el rand sudafricano era de: 1 SGD = {datoVariable2} ZAR ¿Cuánto dinero recibió Mei-Ling en rands sudafricanos?', datoVariable1*datoVariable2],[f'La población de una ciudad pasó de {datoVariable1} millones de habitantes a {datoVariable2} millones en tan solo un año. ¿Qué porcentaje de decrecimiento poblacional hubo (%)?',100 - datoVariable2/datoVariable1*100],[f'Si una tienda aplica descuentos del {datoVariable1}% en todos sus productos, ¿cuál será el precio final de un jersey de {datoVariable2} €?',(100-datoVariable1)*datoVariable2/100],[f'A 2009, la población de un pueblo cuenta con {datoVariable1} viviendas y al año crece exponencialmente un {datoVariable2}%. ¿Cuántas viviendas tendrá en {datoVariable3} años?',datoVariable1*(1+datoVariable2/100)**datoVariable3],[f'Una empresa imprime {datoVariable1} copias a la hora. Un día, le agregan una impresora y ahora pueden imprimir {datoVariable2} más. ¿Cuántas copias generan a las {datoVariable3} horas con la nueva impresora?',(datoVariable1+datoVariable2)*datoVariable3]]
        
        ubicacion = 'pantano misterioso'
        typeProblem = 'aritmética'
        enemigosNivel = [['rana carnívora','una','La'], ['araña gigante','una','La']]
        ubicacionSiguiente = 'muelle de los deseos'
        
    
    elif level == 2:
        datoVariable1 = randint(1,50)
        datoVariable2 = round(uniform(1,50),2)
        datoVariable3 = randint(1,50)
        
        preguntasNivel = [[f'¿Cuál es el área de un triangulo, si su base mide {datoVariable1} cm y su altura mide {datoVariable2} cm?', datoVariable1 * datoVariable2/2],[f'¿Cuál es la suma de los ángulos internos de una figura convexa que tiene {datoVariable1} caras?',180 * (datoVariable1 - 2)],[f'Nicolás quiere pavimentar el patio rectangular de su nueva casa. El patio mide {datoVariable1} metros de largo y {datoVariable2} metros de ancho. Nicolás necesita {datoVariable3} ladrillos por metro cuadrado. ¿Cuántos ladrillos necesita para cubrir el área?',datoVariable1*datoVariable2*datoVariable3],[f'Una escalera con {datoVariable1} peldaños tiene una altura de {datoVariable2} metros. ¿Cuánto mide la separación entre cada peldaño en cm?',datoVariable2/datoVariable1*100],[f'¿Cuál es el área de un hexágono si un lado mide {datoVariable1} cm y su apotema mide {datoVariable2} cm?',6*datoVariable1*datoVariable2/2],[f'Calcula la hipotenusa de un triángulo rectángulo si sus catetos miden {datoVariable1} m y el otro {datoVariable2} m',hypot(datoVariable1,datoVariable2)]]
        
        ubicacion = 'muelle de los deseos'
        typeProblem = 'geometría'

        enemigosNivel = [['pirata','un','El'],['tiburón','un','El'],['calamar gigante','un','El']]
        ubicacionSiguiente = 'Pueblo de Arcadia'
        
    elif level == 3:
        datoVariable1 = randint(1,10)
        datoVariable2 = randint(1,100)
        datoVariable3 = randint(1,100)
        
        preguntasNivel = [[f'Resuelve para x: sqrt({datoVariable2}x) + {datoVariable1} = 0',(-datoVariable1)**2/datoVariable2 ],[f'Encuentra el valor de x en una función lineal, si m = {datoVariable1}, b = {datoVariable3} y f(x) = {datoVariable2}',(datoVariable2-datoVariable3)/datoVariable1],[f'Si la pendiente de una función vale {datoVariable2} y el valor de ordenada al origen vale {datoVariable1}, ¿cuál es el valor de "y" cuando x es {datoVariable3}?',datoVariable2*datoVariable3+datoVariable1],[f'Dada la función cuadrática {datoVariable1}x^2 + {datoVariable2}x - {datoVariable3}; encuentra la intersección de la parábola con el eje y', -datoVariable3],[f'Dada la función f(x) = {datoVariable1}x^2 - {datoVariable2}x - {datoVariable3}; evalúa para f(2)', datoVariable1*2**2 - datoVariable2*2 - datoVariable3]]
        
        ubicacion = 'Pueblo de Arcadia'
        typeProblem = 'funciones'

        enemigosNivel = [['aldeano enojado','un','El'],['ladrón','un','El'],['carterista','un','El']]
        ubicacionSiguiente = 'Monte de la Muerte'
        
    elif level == 4:
        datoVariable1 = randint(1,100)
        datoVariable2 = randint(1,100)
        datoVariable3 = randint(1,10)
        
        preguntasNivel = [[f'Javier tenía un promedio de {datoVariable1} en sus primeros {datoVariable3} exámenes. En el examen número {datoVariable3+1} sacó {datoVariable2}. ¿Cuál será el promedio de calificación en los {datoVariable3+1} exámenes?',(datoVariable1*datoVariable3+datoVariable2)/(datoVariable3+1)],[f'Si la media de calificaciones de 2 alumnos es de {datoVariable1} y un alumno sacó {datoVariable2}. ¿Cuánto debió de haber sacado otro alumno?',datoVariable1*2-datoVariable2],[f'La media de calificaciones de {datoVariable3} alumnos es de {datoVariable1}. Cuando se elimina un alumno el promedio cambia a {datoVariable2}. ¿Cuál era la calificación que tenía el alumno eliminado?',datoVariable1*datoVariable3 - datoVariable2*(datoVariable3-1)],[f'Dado los datos de tiempos recorridos por una persona en su trayecto al supermercado (en minutos): {datoVariable1}, {datoVariable1+100}, {datoVariable2}, {datoVariable3} y {datoVariable3+20}. Obtén la mediana de estos datos.',median([datoVariable1, datoVariable1+100, datoVariable2, datoVariable3, datoVariable3+20])]]
        typeProblem = 'estadística'
        ubicacion = 'Monte de la Muerte'

        enemigosNivel = [['cabra','una','La'],['puma','un','El'],['águila','un','El']]
        ubicacionSiguiente = 'Castillo del Shire'
    elif level == 5:
        datoVariable1 = randint(1,20)
        datoVariable2 = randint(20,100)
        datoVariable3 = randint(1,50)
        
        preguntasNivel = [[f'¿Cuál es la probabilidad (%) que te salga el número {datoVariable1}, entre los números 0 y {datoVariable2}?', datoVariable1/datoVariable2*100],[f'Te estás comiendo unos chocolates freskas (Cuenta con color verde, amarillo y rosa). ¿Cuál es la probabilidad (%) que el interior del chocolate no sea de color verde o amarillo?',1/3*100],[f'En un salón hay un total de alumnos de {datoVariable2} y de esos {datoVariable1} son hombres. ¿Qué porcentaje (%) del salón son mujeres?',100 - datoVariable1/datoVariable2*100 ],[f'En un juego de naipes ingleses (trébol, diamantes, corazones y flechas), ¿Cuál es la probabilidad (%) que te salga una carta de diamantes?',1/4*100],[f'Al lanzar una moneda al aire, ¿Qué probabilidad (%) hay que está caiga en cruz?',1/2*100]]
        ubicacion = 'Castillo del Shire'
        typeProblem = 'probabilidad'

        enemigosNivel = [['espía','un','El'],['guardia','un','El'],['rey malvado','un','El']]
        ubicacionSiguiente = 'Domo de Güsenville' #Ubicación donde celebra la victoria
    enemies = escoge_enemigos(enemigosNivel)
    if first: #Variable de primera vez. Esto es para ver si imprimer la sig. leyenda
        print(f'\nNivel {level}:\n¡Prepárate para responder preguntas de {typeProblem}!\n')
        sleep(2)
        print(f'Llegas al {ubicacion} en busca de pistas de dónde está el rey.\n')
                        
    sleep(3) #Pausas de segundos
    print(f'¡CUIDADO, {enemies[1]} {enemies[0]} bloquea tu paso!, responde correctamente a la pregunta para derrotar a tu enemigo.\n')
    sleep(2)
    print(f'Pregunta {question}:')
                       
    #Imprime una pregunta de forma aleatoria
    indiceAleatorio = randint(0,len(preguntasNivel)-1) 
    print(preguntasNivel[indiceAleatorio][0]) #Solo imprime el indice en posición cero, para solo imprimir la pregunta y no la respuesta
    
    respuesta = -10000000
    while respuesta != round(preguntasNivel[indiceAleatorio][-1],2): #Redondea la respuesta a 2 decimales
        if lives != 0: 
            
            respuesta = confirma_dataType('Ingresa tu respuesta (redondea tu respuesta a 2 decimales de ser necesario):\n','float') # Se llama la función para evaluar si el dato ingresado sea un valor int o float.
            sleep(1)
            if respuesta == round(preguntasNivel[indiceAleatorio][-1],2):
                corrects += 1
                question += 1 
                print(f'\nDerrotaste con éxito a {enemies[1]} {enemies[0]}\nContinúa buscando por el {ubicacion} hasta encontrar una pista.\n')
                
            else:
                lives -= 1
                
                print(f'\n{enemies[2]} {enemies[0]} te ha hecho daño. Has perdido una vida (tienes {lives} vidas restantes)\nIntenta de nuevo:\n')
                sleep(1)
                print(preguntasNivel[indiceAleatorio][0])
            
            first = False #Esto es para validar que ya no es tu primera vez en el juego y así ya no se imprime la leyenda de que llegaste a un lugar
        
        else:
            break #Si vidas no es igual a 0, salte del juego
        
    
    life = [corrects,lives,question,first,enemies,ubicacionSiguiente]  #Se guarda una matriz con los datos que queremos que devuelva la matriz     
    return life
    
    
    
def escoge_enemigos(matrix_enemies): #Escoge un enemigo aleatorio dada una matriz
    random_enemie = randint(0,len(matrix_enemies)-1)
    return matrix_enemies[random_enemie]
    
def confirma_dataType(pregunta,dataType): #Comprueba que el dato ingresado sea str() o int() o float()
    myInput = input(pregunta).strip() #Recibe como parámetro la pregunta 
    if dataType == 'int': 
        while not myInput.isnumeric():
            print('\nIngresa un valor numérico entero válido')
            myInput = input(pregunta).strip()
        return int(myInput)
    elif dataType == 'str': #Si el valor ingresado es string, corre este pequeño programa
        while myInput.isnumeric() or myInput == '': #Método isnumeric devuelve un valor booleano
            print('\nIngresa un valor de texto válido')
            myInput = input(pregunta).strip()
        return myInput.lower().title()
    else:
        while True:
            try:
                float(myInput) 
            except:
                print('\nIngresa un valor con decimal válido')
                myInput = input(pregunta).strip()
                continue
            break
        return float(myInput)
    
    

#######PROGRAMA PRINCIPAL#######
separador = '<--------------------------------------------------------------------------------------------------------------->'
print("Bienvenido a Güsenville, tierra de aventuras y reinos.")
sleep(2.5)
print("Este reino es un lugar complicado, en donde reina el caos.\nHace unos meses capturaron a los reyes de la región Small Town, y es tu deber salvarlos.")
sleep(6)
print("\nPara esto necesitas resolver varios problemas matemáticos como los que encontrarás en tu prueba PISA,\npara así derrotar a los oponentes que encontrarás en esta aventura\n")
sleep(3)
print(separador)
nombre = confirma_dataType("\nVamos a generar tu perfil de jugador.\n(Tu nombre y edad guardarán el registro de cómo te fue en el juego esta ocasión)\n\n\tIngresa tu nombre: ",'str')
edad = confirma_dataType("\tIngresa tu edad: ",'int')

datosDeJugadores = crea_rutaDeCarpetas()
sleep(0.7)
print(f"""
{nombre}, unos espías del reino del Shire acaban de secuestrar a tu rey supremo Legolas. 
Tu deber es entrar en el castillo principal del Shire y rescatar a Legolas. Pero no será tán fácil, 
tu primera misión es cruzar el pantano misterioso, lugar de arañas gigantes y ranas carnívoras.
""")
sleep(6)
dec = '0'
while dec != '4':
    dec = input("\t\tMENÚ PRINCIPAL:\n  ---------------------------------------------\n\t1. Comenzar el juego\n\t2. Ver el registro de usuarios\n\t3. Borrar datos guardados\n\t4. Salir\n\nIngresa el número correspondiente: ")
    if dec == '1':
        print("\nInicia el juego\n")
        reglas = ['1. Tienes 3 vidas al inicio del juego, por cada pregunta mal que tengas será una vida menos','2. Hay 5 niveles que debes superar para pasar el juego','3. Para superar el nivel debes responder correctamente a 3 preguntas','4. Responde solo valores numéricos ya sean enteros o decimales, no escribas unidades']
        print(separador)
        print('\t\t\t\t\tReglas\n')
        for rule in reglas:
            print(rule)
            sleep(3.5)
        print('\n',separador)
        rango = ['Rookie','Amateur','Semiprofesional','Profesional','Campeón','Leyenda']
        vidas = 3
        nivel = 1
        correctas = 0
        pregunta = 1
        firstTime = True #Indica si es la primera vez que se entra a la variable, para ver si muestra la leyenda de intro al programa
        while True: #Siempre va a entrar a este bucle infinito y solo se puede salir con un break
            if vidas > 0:
                if nivel != 6:
                    if correctas != 3:
                        matriz_DeDatos = imprime_pregunta(nivel,firstTime,correctas,vidas,pregunta)
                        correctas = matriz_DeDatos[0] 
                        vidas = matriz_DeDatos[1]
                        pregunta = matriz_DeDatos[2]
                        firstTime = matriz_DeDatos[3]
                        enemigo = matriz_DeDatos[4]
                        nextLocation = matriz_DeDatos[5]
                        
                    else: #Avanzar de nivel
                        correctas = 0
                        nivel += 1
                        pregunta = 1
                        firstTime = True #El firstTime se vuelve, para que le muestre la leyenda del lugar nuevo
                        if nivel != 6:
                            print(f'\n¡FELICIDADES! Avanzas al nivel {nivel}\n')
                            print(f'{enemigo[2].title()} {enemigo[0]} reveló que al rey se lo llevaron por el {nextLocation}.\nSerá mejor que investigues por ahí')
                        print(f'\n{separador}\n')
                        sleep(2)
                        
                
                else: #NIVEL = 6; Superaste el juego
                    

                    datosPersonales = [nombre,str(edad),str(vidas),rango[nivel-1]] #Lista creada del usuario que acaba de terminar el juego
                    datosDeJugadores.append(datosPersonales) #datosDeJugadores es la matriz con los datos históricos y se le agrega la información del nuevo usuario
                    guarda_datos(datosDeJugadores) #Esto es para guardar en el archivo la nueva matriz
                    print('\n\t\t\t\t\tSUPERASTE EL JUEGO\n')
                    print(separador)
                    sleep(2)
                    print(f'\nVidas Restantes:\t{vidas}\n')
                    print(separador)
                    sleep(2.5)
                    print(f'''
Has encontrado al Rey Legolas, lamentablemente se encuentra en un estado reprobable,
necesita atención médica urgente. Llévalo al Domo de Güsenville para curarlo.

Muchas felicidades {nombre}, con tan solo {edad} años, y tu gran conocimiento de matemáticas salvaste al rey Legolas
y lo trajiste de vuelta con su gente.

Alcanzaste el rango de {rango[nivel-1]}

Si quieres seguir practicando a partir de algún nivel en especial, ingresa el número del nivel:
                                FREE PLAY:
                                
                            1. Aritmética
                            2. Geometría
                            3. Funciones
                            4. Estadística
                            5. Probabilidad
                            6. SALIR''')
                    nivel = '0'
                    while nivel not in '123456': #Como aquí nivel es 0, no se encuentra en ese string y por ende entra al ciclo while
                        
                        nivel = str(confirma_dataType('Ingresa un número que esté en el menú: ','int'))
                    if nivel == '6': #Se pone un break y se sale del ciclo while de la opción 1 del menú
                        print()
                        sleep(2)
                        break
                        
                    else: #Se va al nivel seleccionado
                        nivel = int(nivel) 
                        vidas = 3
                        continue
                    
                    
            else: #Si tiene menos de 3 vidas, pierdes
                print('\n\t\tFIN DEL JUEGO\n\t  Perdiste todas tus vidas\n')
                print(f'Alcanzaste el rango de {rango[nivel-1]}\n')
                print(separador,'\n')

                datosPersonales = [nombre,str(edad),str(vidas),rango[nivel-1]] #Esto es lo mismo que se hace cuando el usuario termina el juego en nivel 6
                datosDeJugadores.append(datosPersonales)
                
                guarda_datos(datosDeJugadores)
                sleep(2)
                break
                         
    elif dec == '2':  #Registro de campeones
        print("\nRegistro de usuarios:\n")
        sleep(1)
        datosDeJugadores = crea_rutaDeCarpetas()
        imprime_tabla(datosDeJugadores)
        sleep(2)
        print(separador,'\n')
    
    elif dec == '3': #Se borran los datos del archivo
        remove(f'{getcwd()}/gusenville/jugadores.csv') #Con el método "remove"
        datosDeJugadores = crea_rutaDeCarpetas()
        print('\nDatos borrados\n')
        sleep(1)
    elif dec == '4': #Se sale del menú y termina el programa
        print(f'Vuelve pronto {nombre}') 
    else: 
        print("\nIngresa una opción válida\n")


