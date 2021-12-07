
__author__ = 'Rohan Shah'
__lastEditor__ = 'Rohan Shah'
__date__ = "December 7, 2021"

#ATCS Data Science Project - analyzing the evolution of crime in San Francisco (2018-Present)

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
sns.set_theme()

#reading the csv's
sfcrime = pd.read_csv("Police_Department_Incident_Reports__2018_to_Present.csv")
sfneigh = pd.read_csv("sfpd_districts.csv")

#dropping columns in the dataset that are not needed / have null values
sfcrime.drop('Incident Time', axis=1, inplace=True)
sfcrime.drop('Report Datetime', axis=1, inplace=True)
sfcrime.drop('CAD Number', axis=1, inplace=True)
sfcrime.drop('Filed Online', axis=1, inplace=True)
sfcrime.drop('Incident Code', axis=1, inplace=True)
sfcrime.drop('Intersection', axis=1, inplace=True)
sfcrime.drop('Supervisor District', axis=1, inplace=True)
sfcrime.drop('Neighborhoods', axis=1, inplace=True)
sfcrime.head()

#plotting a  histogram (2018-2021) of the total number of crimes reported each year
sns.histplot(data=sfcrime, x="Incident Year", element="bars", palette="pastel", legend=False)
plt.xticks([2018, 2019, 2020, 2021])
plt.title("Incidents by Year")
plt.show()

#creating pie chart of disribution of types of crime from 2018-present
#allIncidentsListed = list(sfcrime['Incident Category'].unique())
#countOfAllIncidentsListed = list(sfcrime['Incident Category'].value_counts())
#topIncidents = allIncidentsListed[:10]
#topIncidentsCount = countOfAllIncidentsListed[:10]
#plt.pie(topIncidentsCount, labels=topIncidents, autopct='%1.1f%%', textprops={'fontsize': 10})
#plt.show()

#breaking up the dataset into four different tables by year (2019 and 2020)
sfcrime2019 = sfcrime[sfcrime['Incident Year'] == int(2019)]
sfcrime2020 = sfcrime[(sfcrime['Incident Year'] == int(2020))]

#examining larceny theft 2019 - plotting longitude vs. latitude of all larceny thefts
larTheft2019 = sfcrime2019[(sfcrime2019['Incident Category'] == 'Larceny Theft')]
sns.scatterplot(data=larTheft2019, x="Longitude", y="Latitude", palette='pastel', alpha=.05, linewidth=0)
plt.title("Larceny Theft Mapped in 2019")
plt.show()

#examining larceny theft 2020 - plotting longitude vs. latitude of all larceny thefts
larTheft2020 = sfcrime2020[(sfcrime2020['Incident Category'] == 'Larceny Theft')]
sns.scatterplot(data=larTheft2020, x="Longitude", y="Latitude", palette='pastel', alpha=.05, linewidth=0)
plt.title("Larceny Theft Mapped in 2020")
plt.show()

#converting all values in df to strings in order to plot
sfcrime2019 = sfcrime2019.astype(str)
sfcrime2020 = sfcrime2020.astype(str)

#creating a new dataset with three specific incident categories - larceny theft, burglary, and robbery
impCrimes = sfcrime[(sfcrime['Incident Category'] == 'Burglary') | (sfcrime['Incident Category'] == 'Larceny Theft') | (sfcrime['Incident Category'] == 'Robbery')]

#plotting a stacked histogram (2018-2021) of the total number of "main" crimes seen
sns.histplot(data=impCrimes, x="Incident Year", hue = impCrimes['Incident Category'], element="bars", legend=True, palette="pastel", multiple = "stack", kde=False)
plt.xticks([2018, 2019, 2020, 2021])
plt.title("Incidents by Year")
plt.show()

larCrimes = sfcrime[(sfcrime['Incident Category'] == 'Larceny Theft')]

#plotting each neighborhood by larceny theft crimes in 2019
sns.histplot(data=larTheft2019, x="Analysis Neighborhood", element="bars", palette="pastel", legend=False)
plt.title("Larceny Theft by Neighborhoods in 2019")
plt.xticks(rotation=90, size=3)
plt.show()

#plotting each neighborhood by larceny theft crimes in 2020
sns.histplot(data=larTheft2020, x="Analysis Neighborhood", element="bars", palette="pastel", legend=False)
plt.title("Larceny Theft by Neighborhoods in 2020")
plt.xticks(rotation=90, size=3)
plt.show()

#creating pie chart of distribution of types of crime in 2019
#creating a list of all incidents that happened in 2019
allIncidentsListed2019 = list(sfcrime2019['Incident Category'].unique())
#counting the # of times each incident type occurred and putting into a list
countOfAllIncidentsListed2019 = list(sfcrime2019['Incident Category'].value_counts())
#taking only the first (biggest) 10 of the incidents that occurred
topIncidents2019 = allIncidentsListed2019[:10]
topIncidentsCount2019 = countOfAllIncidentsListed2019[:10]
plt.pie(topIncidentsCount2019, labels=topIncidents2019, autopct='%1.1f%%', textprops={'fontsize': 8})
plt.title("Crimes in 2019")
plt.show()

#creating pie chart of distribution of types of crime in 2020
#creating a list of all incidents that happened in 2020
allIncidentsListed2020 = list(sfcrime2020['Incident Category'].unique())
#counting the # of times each incident type occurred and putting into a list
countOfAllIncidentsListed2020 = list(sfcrime2020['Incident Category'].value_counts())
#taking only the first (biggest) 10 of the incidents that occurred
topIncidents2020 = allIncidentsListed2020[:10]
topIncidentsCount2020 = countOfAllIncidentsListed2020[:10]
plt.pie(topIncidentsCount2020, labels=topIncidents2020, autopct='%1.1f%%', textprops={'fontsize': 8})
plt.title("Crimes in 2020")
plt.show()