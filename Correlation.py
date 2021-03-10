import plotly.express as px
import csv
import numpy as np

def get_data(path):
  coffee = []
  sleep = []

  with open(path) as f:
    reader = csv.DictReader(f)
    for row in reader:
      coffee.append(float(row['Coffee Amount']))
      sleep.append(float(row['Sleep Received']))

  return {'x': coffee, 'y': sleep}

def find_correlation(source):
  correlation = np.corrcoef(source['x'], source['y'])
  print('Correlation between Amount of Coffee consumed and Sleep Received:',correlation[0, 1])

def figure(path):
  with open(path) as f:
    df = csv.DictReader(f)
    fig = px.scatter(df, x = 'Coffee Amount', y = 'Sleep Received')

  fig.show()

def main():
  path = './Cups_of_Coffee_vs_Sleep.csv'
  source = get_data(path)
  find_correlation(source)
  figure(path)

main()