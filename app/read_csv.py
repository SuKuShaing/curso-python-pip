import csv

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',') # Entrega la dirección del objeto
        header = next(reader) # Con esta línea de código solo leemos la primera línea del archivo y se guarda como un array
        data = []
        for row in reader: # con esto podemos trabajar linea por linea del csv y está en "row" como un array
            iterable = zip(header, row) # se devuelve como la dirección del objeto zip, al pasarlo a lista, se ve un array con tuplas, donde une el el titulo guardado en header con el row correspondiente, así ('country', 'Chile')
            country_dict = {key: value for key, value in iterable} # Convierte cada Row en un diccionario donde la key es es el título y el valor es el que corresponde al país en esa columna, así {'Rank': '74', 'CCA3': 'ZWE', 'Country/Territory': 'Zimbabwe', 'Capital': 'Harare', 'Continent': 'Africa', '2022 Population': '16320537', '2020 Population': '15669666', '2015 Population': '14154937', '2010 Population': '12839771', '2000 Population': '11834676', '1990 Population': '10113893', '1980 Population': '7049926', '1970 Population': '5202918', 'Area (kmÂ²)': '390757', 'Density (per kmÂ²)': '41.7665', 'Growth Rate': '1.0204', 'World Population Percentage': '0.2'}
            # country_dict = dict(iterable) # De esta manera también se puede se podía convertir en diccionario pero el profesor escogió la versión de arriba
            data.append(country_dict) # Guarda cada uno de los diccionarios en un array uno por uno en cada iteración
        return data


if __name__ == '__main__':
    data = read_csv('./app/data.csv')
    # print(data)
    # print(data[0])
    print(list(filter(lambda item : item['Country/Territory'] == 'Argentina' ,data)))
