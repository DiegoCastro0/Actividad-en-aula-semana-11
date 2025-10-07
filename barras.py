import matplotlib.pyplot as plt


tazas = [0, 1, 2, 3, 4, 5]
cantidad_personas = [2,4,2,1,1,0]

plt.bar(tazas, cantidad_personas, color='brown')
plt.xlabel('Tazas de café al día')
plt.ylabel('Cantidad de personas')
plt.title('Consumo diario de café')
plt.xticks(tazas)
plt.show()