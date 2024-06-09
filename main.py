import numpy as np
import scipy as sc
import matplotlib.pyplot as plt

# Th será el vector que contenga x e y
func = lambda th: np.sin(1/2 * th[0]**2 - 1/4 *th[1]**2 +3) * np.cos(2*th[0] +1 - np.e**th[1])

resolucion=100

# Generar un vector con secuencias de valores de x
_x= np.linspace(-2,2,resolucion)

# Generar un vector con secuencias de valores de y
_y = np.linspace(-2,2,resolucion)

#Para cada combinacion de x e y evaluar la funcion y obtener nuevos valores
_z = np.zeros((resolucion,resolucion))

for ix,x in enumerate(_x):
    for iy,y in enumerate(_y):
        _z[iy,ix] = func([x,y]) # iy numero de fila (eje y) e ix numero de columna (eje x)

# mostrar superficie donde cada color representa diferentes puntos de altura en la funcion de coste

plt.contourf(_x,_y,_z,100)
plt.colorbar()

# Vector basado en 2 numeros aleatorios generado en un rango (-2,2)
theta =np.random.rand(2)*4 -2

h=0.001
lr = 0.001 # ratio de aprendizaje

plt.plot(theta[0],theta[1],"o",c="white")

gradiente = np.zeros(2)

# Método iterativo, lo ejecutamos 1000 veces (Convergencia fijada 10000 iteraciones)
for _ in range(1000):
    # Calculamos las derivadas parciales para evaluar la pendiente de cada variable

    gradiente = sc.optimize.approx_fprime(theta, func, h)

    theta = theta - lr*gradiente
    print(func(theta))

    # Mostramos los puntos cada 100 iteraciones para ver como se desplaza la optimizacion
    # El desplazamiento dependerá del ratio de aprendizaje y el numero de iteraciones
    if(_ % 100==0):
        plt.plot(theta[0], theta[1], "o", c="red")

# Mostramos el punto final tras la optimizacion
plt.plot(theta[0],theta[1],"o",c="green")
plt.show()

