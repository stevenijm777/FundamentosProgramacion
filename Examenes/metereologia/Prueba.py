
# Tema 3
def cargar_datos(ciudad, lst_tweets):
    l_tem_Max = []
    l_tem_Min = []
    l_fechas = []
    for tweet in lst_tweets:
        datos = tweet.split(" ")
        if ciudad in datos:
            for i in range(len(datos)): # 10
                palabra = datos[i] # tempMin
                if palabra == "DIA": # F
                    fecha = datos[i+1]
                    l_fechas.append(fecha)
                elif palabra == "TEMP_MIN":
                    tem_min = datos[i+1]
                    l_tem_Min.append(float(tem_min))
                elif palabra == "TEMP_MAX":
                    tem_max = datos[i+1]
                    l_tem_Max.append(float(tem_max))
    return l_tem_Min, l_tem_Max, l_fechas


# Programa
#2.1
lst_tweets = ["El DIA 2021-05-17 en la CIUDAD Octavalo se regiistro una TEMP_MIN 18.3 grados centigrados y una TEMP_MAX 27.7 grados centigrados"]
ciudad = "Octavalo"
l_tem_Min, l_tem_Max, l_fechas = cargar_datos(ciudad, lst_tweets)
#2.2
print(l_tem_Max)
print(l_tem_Min)
print(l_fechas)
l_proms = []
for i in range(len(l_fechas)):
    tem_max = l_tem_Max[i]
    tem_min = l_tem_Min[i]
    promedio = (tem_min + tem_max) / 2
    l_proms.append(promedio)


#2.3
mes = int(input("Ingrese un número de mes: ")) # 15
while not(mes>=1 and mes<=12): #F
    mes = int(input("Ingrese un número de mes: ")) # 5
l_mes_proms = []
for i in range(len(l_fechas)): # 0
    fecha = l_fechas[i] # 2021-05-17
    aaaa,mm,dd = fecha.split("-") # "2021", "05", "17"
    if mm[0] == "0":
        mm = int(mm[-1])
    else:
        mm = int(mm)
    if mm == mes:
        tem_prom = l_proms[i]
        l_mes_proms.append(tem_prom)
# Sacar el maximo de la lista
maxi_prom = max(l_mes_proms)
print("La mayor temperatura promedio: ", maxi_prom)





