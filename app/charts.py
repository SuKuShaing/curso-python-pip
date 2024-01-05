import matplotlib.pyplot as plt


def generate_bar_chart(name, labels, values):
    fig, ax = plt.subplots() # La librería se usa así
    ax.bar(labels, values) # se le pasan los valores y etiquetas
    # plt.show() # con este comando se muestra el gráfico en pantalla
    plt.savefig(f'./imgs/{name}.png')
    plt.close()

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels) # aquí se le especifica que las etiquetas, son las etiquetas, enserio
    ax.axis('equal') # aquí para que el gráfico este centrado
    # plt.show()
    plt.savefig('./imgs/pie.png')
    plt.close()



if __name__ == '__main__':
    labels = ['a', 'b', 'c', 'd', 'e']
    values = [150, 200, 130, 80, 115, ]
    generate_bar_chart(labels, values) # si se piden generar 2 gráficas, al cerra una, se abre la otra
    generate_pie_chart(labels, values)