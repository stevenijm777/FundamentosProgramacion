import numpy as np

def l_compradores(categorias):
    compradores = []
    for categoria in categorias:
        f = open(categoria + '.txt', 'r')
        f.readline()
        for linea in f:
            datos = linea.strip().split(',')
            comprador = datos[0]
            if comprador not in compradores:
                compradores.append(comprador)
    return compradores

def calculaTotales(categoria): # 'Flores'
    f = open(categoria+'.txt', 'r')
    f.readline()
    totales = {}
    for linea in f: # [Ecuador,Alemania,Narcisos,29103,4523.18,10-08-2020]
        Comprador,Vendedor,Producto,Unidadesvendidas,Ventas,Fecha = linea.strip().split(',')
        if (Comprador,Vendedor,Producto) not in totales:
            totales[(Comprador,Vendedor,Producto)] = float(Ventas)
        else:
            totales[(Comprador,Vendedor,Producto)] += float(Ventas)
    return totales

def consolidado(nomArchivo, categorias): # datos.csv [Flores,Maderas,frutas]
    f = open(nomArchivo, 'w')
    dicCategorias = {}
    for categoria in categorias:
        totales = calculaTotales(categoria)
        productos = []
        for (comprador,vendedor,producto),ventas in totales.items():
            productos.append(producto)
            linea = comprador+','+vendedor+','+categoria+','+producto+','+str(ventas)+'\n'
            f.write(linea)
        dicCategorias[categoria] = productos
    f.close()
    for categoria in categorias:
        dicCategorias[categoria].sort()
    return dicCategorias

def l_productos(dicCategorias,categorias):
    productos = []
    for categoria in categorias: # Maderas
        productos.extend(dicCategorias[categoria])
    return productos

def crearDicc(nomArchivo): # Datos.csv
    dicc = {}
    f = open(nomArchivo, 'r')
    for linea in f: # Ecuador,Alemania,Flores,Narcisos,4523.18
        comprador,vendedor,categoria,producto,ventas = linea.strip().split(',')
        ventas = float(ventas)
        if categoria not in dicc:
            dicc[categoria] = {(comprador,producto): ventas}
        else:
            if (comprador, producto) not in dicc[categoria]:
                dicc[categoria][(comprador, producto)] = ventas
            else:
                dicc[categoria][(comprador, producto)] += ventas
    return dicc

def crearMatriz(nomArchivo, dicCategorias, compradores, categorias):
    # datos.csv, ,
    productos = l_productos(dicCategorias,categorias)
    fils = len(compradores)
    cols = len(productos)
    M = np.zeros((fils, cols))
    dicc = crearDicc(nomArchivo)
    for categoria in categorias: # Maderas
        for (comprador, producto), ventas in dicc[categoria].items():
            ind_fila = compradores.index(comprador)
            ind_col = productos.index(producto)
            M[ind_fila, ind_col] = ventas
    return M, productos



categorias = ['Maderas', 'Frutas', 'Flores']
nomArchivo = 'Datos.csv'
dicCategorias= consolidado(nomArchivo, categorias)
compradores = l_compradores(categorias)
M, productos = crearMatriz(nomArchivo, dicCategorias, compradores, categorias)

# iterar la matriz por fila
filas = M.shape[0] # 10
total_pais = np.zeros(filas) # [0 0 0 0 0 0 0 0 ... ]
for i in range(filas): # [0,1 ,2...9]
    fila  = M[i, :]
    suma = fila.sum()
    total_pais[i] = suma
# cual es el mayor
ind = np.argmax(total_pais)
mayor_pais = compradores[ind]
print('el pais con mas ventas en total es {}'.format(mayor_pais))

def categoria_producto(dicCategorias, producto):
    for categoria,l_productos in dicCategorias.items():
        if producto in l_productos:
            return categoria
# iterar la matriz por columna
colus = M.shape[1]
v_prds_total = np.zeros(colus)
for j in range(colus):
    colu = M[:,j]
    total = colu.sum()
    v_prds_total[j] = total
ind_min = np.argmin(v_prds_total)
producto_menor = productos[ind_min]
cate_prod = categoria_producto(dicCategorias, producto_menor)
print(producto_menor)
print(cate_prod)
# top en listas
l_tuplas = []
for i in range(len(total_pais)):
    pais = compradores[i]
    ventas_pais = total_pais[i]
    tupla = (ventas_pais, pais)
    l_tuplas.append(tupla)
l_tuplas.sort(reverse = True)
top5 = l_tuplas[:5]
top5

# top con numpy
top5_pais = total_pais.argsort()[::-1][:5]
top5_pais
v_compradores = np.array(compradores)
v_compradores[top5_pais]
nombre_producto = input('Ingrese el nombre un producto ')
ind_col = productos.index(nombre_producto)
v_producto = M[:,ind_col]
v_producto
v_inds = v_producto.argsort()[::-1]
v_compradores[v_inds]
# 5.
pais = input('Ingrese un pais ')
# iterar una matriz por bloque
ini_col = 0
for categoria in categorias:
    fin_col = ini_col + len(dicCategorias[categoria])
    m_categoria = M[:,ini_col: fin_col]
    print(categoria)
    print(m_categoria)
    ini_col = fin_col
ind_pais = compradores.index(pais)
ini_col = 0
for categoria in categorias:
    fin_col = ini_col + len(dicCategorias[categoria])
    prods_cate = np.array(productos[ini_col: fin_col])
    m_categoria = M[ind_pais,ini_col: fin_col]
    condicion = m_categoria == 0
    print(categoria)
    print(prods_cate[condicion])
    ini_col = fin_col
# iterar una matriz por bloque
ini_col = 0
cate_T = []
for categoria in categorias:
    fin_col = ini_col + len(dicCategorias[categoria])
    m_categoria = M[:,ini_col: fin_col]
    suma = m_categoria.sum()
    cate_T.append(suma)
    ini_col = fin_col
print(cate_T)
print(categorias)
v_cate_T = np.array(cate_T)
v_categorias = np.array(categorias)
cate_mayor = v_categorias[np.argmin(cate_T)]
cate_mayor
#7
def matriz_Categoria(M,dicCategorias,categorias, nomcategoria):
    # iterar una matriz por bloque
    ini_col = 0
    for categoria in categorias:
        fin_col = ini_col + len(dicCategorias[categoria])
        if categoria == nomcategoria:
            m_categoria = M[:,ini_col: fin_col]
            return m_categoria
        ini_col = fin_col
m_Flores = matriz_Categoria(M,dicCategorias,categorias, 'Flores')
m_Flores
max_Flores = m_Flores.max(axis = 1)
m_Frutas = matriz_Categoria(M,dicCategorias,categorias, 'Frutas')
m_Frutas
m_condicion = m_Frutas > max_Flores
v_prods_frutas = np.array(dicCategorias['Frutas'])
for i in range(len(compradores)):
    fila = m_condicion[i,:]#[False, False, False, False, False, False, False, False, False, False]
    v_prods_frutas[fila]
    print(compradores[i])
    if len(v_prods_frutas[fila])==0:
        print('no hay')
    else:
        print(v_prods_frutas[fila])