import matplotlib.pyplot as plt

# Datos
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y1 = [0, 5, 6, 2, 4, 6, 7, 8, 9, 3, 7]


plt.plot(x, y1, label="Horas dormidas", marker="o")
plt.xlabel("Personas")
plt.ylabel("Horas")
plt.title("Horas dormidas por persona")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
