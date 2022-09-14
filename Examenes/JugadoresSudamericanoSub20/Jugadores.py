# CCPG1001-Fundamentos de Programación - FIEC-ESPOL
# 3Eva_IIT2018_T2 Jugadores Sudamericano Sub-20

def actualizaDiccionario(nomArchivo,dic):
    paises  = list(dic.keys())
    archivo = open(nomArchivo,'r')
    encabezado = archivo.readline()
    linea   = archivo.readline()
    while not(linea==''):
        linea   = linea.strip('\n')
        partes  = linea.split(',')
        pais    = partes[0]
        jugador = partes[1]
        if not(pais in paises):
            dic[pais]={jugador:{'TA':int(partes[2]),
                                'TR':int(partes[3]),
                                'Goles':int(partes[4]),
                                'Minutos':int(partes[5]),
                                'KM':float(partes[6])
                                  }
                       }
        else:
            jugadores = list(dic[pais].keys())
            if not(jugador in jugadores):
                dic[pais][jugador] = {'TA':int(partes[2]),
                                      'TR':int(partes[3]),
                                      'Goles':int(partes[4]),
                                      'Minutos':int(partes[5]),
                                      'KM':float(partes[6])
                                      }
            else:
                dic[pais][jugador]['TA']    = dic[pais][jugador]['TA'] + int(partes[2])
                dic[pais][jugador]['TR']    = dic[pais][jugador]['TR'] + int(partes[3])
                dic[pais][jugador]['Goles'] = dic[pais][jugador]['Goles'] + int(partes[4])
                dic[pais][jugador]['Minutos'] = dic[pais][jugador]['Minutos'] + int(partes[5]),
                dic[pais][jugador]['KM']    = dic[pais][jugador]['KM'] + float(partes[5])
        linea = archivo.readline()
    archivo.close()
    return(dic)

def buenDeportista(jugador,dic):
    cumple = 0
    paises = list(dic.keys())
    for pais in paises:
        jugadores = list(dic[pais].keys())
        if jugador in jugadores:
            tarjetas = dic[pais][jugador]['TA'] + dic[pais][jugador]['TR']
            transcurrido = dic[pais][jugador]['Minutos']
            registro = tarjetas/transcurrido
            if registro<(2/270):
                cumple=1
    return(cumple)

def jugadorAtleta(jugador,dic):
    cumple = 0
    paises = list(dic.keys())
    for pais in paises:
        jugadores = list(dic[pais].keys())
        total = 0
        for jugador in jugadores:
            total = total + dic[pais][jugador]['KM']
        promedio = total/len(jugadores)
        if jugador in jugadores:
            if dic[pais][jugador]['KM']>=promedio and dic[pais][jugador]['Goles']>=1:
                cumple = 1
    return(cumple)

def paisBuenasPraticas(pais,dic):
    cumple = 0
    paises = list(dic.keys())
    if pais in paises:
        jugadores = list(dic[pais].keys())
        k = len(jugadores)
        cuenta = 0
        for jugador in jugadores:
            cuenta = cuenta + buenDeportista(jugador, dic)
        if (k==cuenta):
            cumple = 1
    return(cumple)

# PROGRAMA -----------------------
# INGRESO
L = ['br-ur.csv'] #,'ec-vn.csv']

# PROCEDIMIENTO
dic = {}
n = len(L)
i = 0
while not(i>=n):
    nomArchivo = L[i]
    actualizaDiccionario(nomArchivo,dic)
    i = i + 1

paises = list(dic.keys())
resultados = []
jugadoresatletas = []
for pais in paises:
    jugadores = list(dic[pais].keys())
    k = len(jugadores)
    cuenta = 0
    goles = 0
    recorrido = 0
    
    for jugador in jugadores:
        cuenta = cuenta + jugadorAtleta(jugador,dic)
        goles = goles + dic[pais][jugador]['Goles']
        recorrido = recorrido + dic[pais][jugador]['KM']
        goleskm = goles/recorrido

        if jugadorAtleta(jugador,dic)==1:
            jugadoresatletas.append([jugador,pais])

    porcentaje = cuenta/k
    nominado = paisBuenasPraticas(pais,dic)
    resultados.append([pais,porcentaje,goleskm,nominado])

# SALIDA
print('pais,porcentaje,goleskm,nominado')
print(resultados)
print('jugadores atletas')
print(jugadoresatletas)