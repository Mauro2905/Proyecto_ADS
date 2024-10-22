import matplotlib.pyplot as plt
import numpy as np

# Tamaños de los datasets (eje X)
tamanos = [100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 
           20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]

# Tiempos de ejecución (eje Y) - Datos simulados
tiempo_python = [0.0, 0.0, 0.0009968280792236328, 0.00099945068359375, 0.0010001659393310547, 0.0010120868682861328, 0.0019905567169189453, 0.001999378204345703, 0.002008199691772461, 0.0020122528076171875, 0.002263307571411133, 0.0030002593994140625, 0.005997896194458008, 0.009644746780395508, 0.015906333923339844, 0.01705479621887207, 0.0235292911529541, 0.02422785758972168, 0.026690006256103516, 0.028156280517578125, 0.04175209999084473]
tiempo_java=[0.000037, 0.000116, 0.000141, 0.000151, 0.000193, 0.000233, 0.000254, 0.000379, 0.000390, 0.000616, 0.000887, 0.000915, 0.000919, 0.000978, 0.001150, 0.001418, 0.001442, 0.001601, 0.001790, 0.007509, 0.028649]
tiempo_cpp=[0, 0, 0.000998, 0.000999, 0, 0.001025, 0, 0, 0, 0, 0, 0, 0, 0, 0.001001, 0.001, 0.001001, 0.002034, 0.002999, 0.005506, 0.003]


# Crear la figura y la gráfica
plt.plot(tamanos, tiempo_python, label='Python', color='green')
plt.plot(tamanos, tiempo_cpp, label='C++', color='pink')
plt.plot(tamanos, tiempo_java, label='Java', color='orange')
# Configuración de la gráfica
plt.xlabel('Tamaño del Dataset')
plt.ylabel('Tiempo de ejecución (s)')
plt.title('Tiempo de ejecución de CountingSort en Python - C++ - Java')
plt.legend()

# Rotar las etiquetas del eje X para mejor visibilidad
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()