# python app/main.py
import utils
import read_csv
import charts

def run():
  data=read_csv.read_csv('./app/data.csv')
  countries=list(map(lambda item: item['Country/Territory'],data))
  percentage=list(map(lambda item: item['World Population Percentage'],data))
  charts.generate_pie_chart(countries,percentage)
  

def run():
  data=read_csv.read_csv('./data.csv')
  country=input('Type country =>')
  country1=country
  result=utils.population_by_country(data,country)

  if len(result)>0:
    country=result[0]
    labels,values=utils.get_population(country)
    charts.generate_bar_chart(country1,labels,values)
    charts.generate_pie_chart(country1,labels,values)

  print(result)

    
if __name__=='__main__':
  run()