import matplotlib.pyplot as plt

categorias = ["tik tok","X","Facebook","Instagram","WhatsApp","YouTube"]
porcentajes = [20,20,10,10,20,20]

plt.pie(
    porcentajes,
    labels=categorias,
    autopct="%1.1f%%",
    startangle=90,
    shadow=True
)

plt.title("Distribucion  de estudiantes universitarios de usos de las redes sociales")
plt.show()