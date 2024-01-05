def get_population(country_dict): #llega como una string y hay que pasarlo a número
    population_dict = {
        '2022': int(country_dict['2022 Population']),
        '2020': int(country_dict['2020 Population']),
        '2015': int(country_dict['2015 Population']),
        '2010': int(country_dict['2010 Population']),
        '2000': int(country_dict['2000 Population']),
        '1990': int(country_dict['1990 Population']),
        '1980': int(country_dict['1980 Population']),
        '1970': int(country_dict['1970 Population'])
    }
    labels = population_dict.keys()
    values = population_dict.values()
    return labels, values # Debiese devolver un array

def population_by_country(data, country):
    result = list(filter(lambda item: item['Country/Territory'] == country, data))
    return result

#Recibimos la data con un array con diccionario, cada dict es la info de un país y devolvemos dos array con los países y sus porcentajes
def world_percentage(data):
    country = []
    percentage = []
    for pais in data:
        country.append(pais['Country/Territory'])
        percentage.append(float(pais['World Population Percentage']))
    return country, percentage
