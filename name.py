import pandas as pd
import plotly.express as px

df = pd.read_csv('line_chart.csv')

graph = px.line(df, x = 'Per capita income', y = 'Year', color = 'Country')

graph.show()
