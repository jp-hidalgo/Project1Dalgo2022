# 1 de Abril de 2022
# Universidad de los Andes
# Diseño y Análisis de Algoritmos
# Proyecto Final Entrega 1
# Miguel Sandoval , Tales Losada y Juan Pablo Hidalgo


#Función que calcula el esfuerzo mínimo al último cuarto del último piso
def menosEsfuerzo(torre):
    base = torre[0]
    filas = base[0]
    columnas = base[1]
    esfuerzos = torre[1]
    portales = torre[2]
    matriz = []
    inf = float('inf')
    for y in range(0, filas):
        matriz.append([])
    for y in range(0, filas):
        for x in range(0, columnas):
            if y == 0  and x == 0:
                matriz[y].append(0)
            else:
                matriz[y].append(inf)
                i = 0
                while i <len(portales):
                    portal = portales[i]
                    if portal[3] == x+1:
                        if portal[2] == y+1:
                            portales.remove(portal)
                            xPartida = portal[1]-1
                            yPartida = portal[0]-1
                            matriz[y][x] = min(matriz[y][x], matriz[yPartida][xPartida])
                        else:
                            i+=1
                    else:
                        i+=1 
                if x != 0:
                    esfAnterior = matriz[y][x-1]
                    matriz[y][x] = min(matriz[y][x], esfAnterior+esfuerzos[y])
        p = columnas - 2
        while p >= 0:
            matriz[y][p] = min(matriz[y][p+1]+esfuerzos[y],matriz[y][p])
            p-= 1
    return matriz[filas-1][columnas-1]

#Función que permite la interacción con el ususario
def interaccion():
    texto = []
    while True:
        linea = input()
        if linea:
            texto.append(linea)
        else:
            break
    casos = crearTorres(texto)
    totalCasos = len(casos)
    for i in range(0, totalCasos):
        esfuerzoFinal = menosEsfuerzo(casos[i])
        if esfuerzoFinal == float('inf'):
            print("NO EXISTE")
        else:
            print(esfuerzoFinal)

#Funición que transforma la entrada de texto en las diferentes torres a considerar
def crearTorres(texto):
    total = len(texto)
    for i in range(0, total):
        texto[i] = texto[i].split(" ")
        longitud = len(texto[i])
        for j in range(0, longitud):
            texto[i][j] = int(texto[i][j])
    numCasos = texto[0][0]
    casos = []
    for i in range(0, numCasos):
        casos.append([]) 
    lineaActual = 1
    for i in range(0,numCasos):
        casoActual = casos[i]
        base = []
        esfuerzos = []
        portales = []
        while lineaActual < total:
            if len(base) < 2:
                base.append(texto[lineaActual][0])
                base.append(texto[lineaActual][1])
                totalPortales = texto[lineaActual][2]
            elif len(esfuerzos) < base[0]:
                for j in range(0 , base[0]):
                    esfuerzos.append(texto[lineaActual][j])
            else:
                for  j in range(0, totalPortales):
                    portales.append(texto[lineaActual])
                    lineaActual += 1
                break
            lineaActual +=1
        casoActual.append(base)
        casoActual.append(esfuerzos)
        casoActual.append(portales)
    return casos

interaccion()
