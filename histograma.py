import matplotlib.pyplot as plt

# Rangos personalizados
categorias = ["15 - 20 minutos", "30 - 45 minutos", "60 - 90 minutos", "120 - 180 minutos"]
frecuencias = [1, 4, 3, 2]  # Total 10 estudiantes

# Gráfico de barras
plt.bar(categorias, frecuencias, color='skyblue', edgecolor='black')
plt.xlabel('Duración de viaje hacia la universidad')
plt.ylabel('Número de estudiantes')
plt.title('Distribución de tiempos de viaje (10 estudiantes)')
plt.ylim(0, max(frecuencias) + 1)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()
