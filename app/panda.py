import utils as utils
import read_csv 
import charts
import pandas as pd

def run():
    #Con Pandas
    df = pd.read_csv('./data.csv') #df = data frames
    df = df[df['Continent'] == 'South America']
    
    contries = df['Country/Territory'].values
    percentages = df['World Population Percentage'].values


    data = read_csv.read_csv('./data.csv')
    Country = input('Digite el país => ')
    result = utils.population_by_country(data, Country)
    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(Country['Country/Territory'], labels, values)
        # print(result)
        pais, porcentaje = utils.world_percentage(data)
        charts.generate_pie_chart(pais, porcentaje)


if __name__ == '__main__':
    run()