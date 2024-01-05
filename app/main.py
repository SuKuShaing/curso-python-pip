import utils as utils
import read_csv 
import charts

def run():
    data = read_csv.read_csv('./data.csv')
    nameCountry = input('Digite el país => ')
    result = utils.population_by_country(data, nameCountry)
    # print(data)

    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(nameCountry, labels, values)
        # print(result)
        pais, porcentaje = utils.world_percentage(data)
        charts.generate_pie_chart(pais, porcentaje)


if __name__ == '__main__':
    run()