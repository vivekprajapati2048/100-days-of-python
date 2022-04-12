import pandas
data = pandas.read_csv("Squirrel_Data.csv")

# print(data["Primary Fur Color"].unique())

# get count of squirrels based on fur color
df_squirrel_counts = data["Primary Fur Color"].value_counts().rename_axis('Fur Color').reset_index(name='count')
df_squirrel_counts.to_csv("squirrel_counts.csv")


'''
import csv

with open("weather_data.csv") as data_file:
	data = csv.reader(data_file)
	temperature = []
	for row in data:
		if row[1] != 'temp':
			temperature.append(int(row[1]))
	print(temperature)
 '''