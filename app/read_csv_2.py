# python app/read_csv_2.py
import csv

def read_csv(path):
  with open(path,'r') as csvfile:
    reader=csv.reader(csvfile, delimiter=',')
    header=next(reader)
    poblacion=['2022 Population','2020 Population','2015 Population','2010 Population','2000   Population','1990 Population','1980 Population','1970 Population']

    data=[]
    population_data=[]
    for row in reader:
      iterable=zip(header,row)
      country_dict={key:value for key,value in iterable if key in poblacion}
      population_data.append(country_dict)
    return data
    

if __name__=='__main__':
  data=read_csv('./app/data.csv')

print(population_data)

  