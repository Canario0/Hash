
f= open('busy_day.in', 'r')

# Leemos el tamaño del mapa el número de drones los turnos máximos y el peso máximo.
x,y,numDrones,turnos,pesoMax=[int(i) for i in f.readline().split()]
# Leemos el número de productos.
numProductos = int(f.readline())
# Asignamos a cada producto el peso correspodiente
productos= [int(i) for i in f.readline().split()]

# Leemos el número de almacenes
numAlmacenes = int(f.readline())
# Generamos una lista de almacenes
almacenes = [[] for _ in range(numAlmacenes)]

# Guardamos las coordenadas y la cantidad de existencias de cada producto
for i in range(numAlmacenes):
    coordenadas=[int(i) for i in f.readline().split()]
    cantidad= [int(i) for i in f.readline().split()]
    almacenes[i] =[coordenadas, cantidad] 

# Ponemos los drones en su hubicación inicial
drones = [almacenes[0][0] for _ in range(numDrones)]

# Procesamos el número de clientes y su información
numClientes = int(f.readline())
clientes = [[] for _ in range(numClientes)]
# Generamos un sert de coordenadas de los clientes
corrdenadasTotales= set()
for i in range(numClientes):
    coordenadas=[int(i) for i in f.readline().split()]
    corrdenadasTotales.add(tuple(coordenadas))
    cantidad = int(f.readline())
    tipoProductos = [int(i) for i in f.readline().split()]
    clientes[i] =[coordenadas, cantidad, tipoProductos] 

'''
Imprimir el mapa por motivos de logistica
mapa = [[ 0 for _ in range(y) ]for _ in range(x)]
for c in almacenes:
    mapa[c[0][0]][c[0][1]] =9 

for c in clientes:
    mapa[c[0][0]][c[0][1]] +=1 

for i in mapa:
    print(*[j if j != 0 else " " for j in i ], sep=" ", end='\n')
'''
#print(*[i for i in corrdenadasTotales], sep='\n')
#print(x,y,numDrones,turnos,pesoMax, numProductos, len(corrdenadasTotales))
f.close() 