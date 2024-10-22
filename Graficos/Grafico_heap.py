import matplotlib.pyplot as plt
import numpy as np

# Tamaños de los datasets (eje X)
tamanos = [100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 
           20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]

# Tiempos de ejecución (eje Y) - Datos simulados
tiempo_python = [0.0009999275207519531, 0.0015211105346679688, 0.0029981136322021484, 0.00750422477722168, 0.00973820686340332, 0.014154434204101562, 0.018670320510864258, 0.026712417602539062, 0.030509233474731445, 0.03276801109313965, 0.036606550216674805, 0.04436349868774414, 0.09656476974487305, 0.1406397819519043, 0.21467971801757812, 0.26863956451416016, 0.3308699131011963, 0.37888264656066895, 0.39630961418151855, 0.45076823234558105, 0.6155259609222412]
tiempo_java=[0.000077, 0.000261, 0.000280, 0.000412, 0.000559, 0.000659, 0.001027, 0.001126, 0.001150, 0.001276, 0.001303, 0.002293, 0.003205, 0.005782, 0.006812, 0.009875, 0.010013, 0.011761, 0.015482, 0.020360, 0.022966]
tiempo_cpp=[0, 0, 0, 0, 0.001, 0.001002, 0.002006, 0.002, 0.002525, 0.003999, 0.003001, 0.002997, 0.010118, 0.012505, 0.016087, 0.024034, 0.02662, 0.030309, 0.039628, 0.04844, 0.046644]



# Crear la figura y la gráfica
plt.plot(tamanos, tiempo_python, label='Python', color='green')
plt.plot(tamanos, tiempo_cpp, label='C++', color='pink')
plt.plot(tamanos, tiempo_java, label='Java', color='orange')
# Configuración de la gráfica
plt.xlabel('Tamaño del Dataset')
plt.ylabel('Tiempo de ejecución (s)')
plt.title('Tiempo de ejecución de HeapSort en Python - C++ - Java')
plt.legend()

# Rotar las etiquetas del eje X para mejor visibilidad
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()