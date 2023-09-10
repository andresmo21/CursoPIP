# python app/piechart.py
import utils
import read_csv
import charts

data=read_csv.read_csv('./app/data.csv')
countries=list(map(lambda item: item['Country/Territory'],data))
percentage=list(map(lambda item: item['World Population Percentage'],data))

charts.generate_pie_chart(countries,percentage)
