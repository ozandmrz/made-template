# Project Plan

## Title

Project for Analyzing Public Transportation and Traffic Linked to Weather Conditions in Istanbul.

## Main Question

1. How do weather variations differ in the relationship between traffic density and public transportation usage in Istanbul?


## Description

Istanbul, with its 16 million residents, faces major transportation challenges due to its dense population, especially during peak hours. The city, separated by the Bosphorus, depends on a limited range of transportation options, including three bridges, one underwater tunnel, a subway system, and sea transport. However, when there's a sudden high demand for a specific option, like everyone trying to use their own cars to cross the bridges, it can lead to transportation problems.

The use of these options can vary, often influenced by the weather. For instance, if bad weather prevents sea transportation, people naturally turn to alternative options, causing issues in those options.

This project's main goal is to study how weather conditions affect the connection between traffic congestion on the roads and the use of public transportation. By examining these interactions, the project aims to predict which resources will see increased demand. For example, if there's a surge in public transportation usage, additional services can be added strategically.

## Datasources


### Datasource1: IMM Open Data Portal
* Metadata URL: https://data.ibb.gov.tr/en/
* Data URL: https://data.ibb.gov.tr/en/dataset/hourly-traffic-density-data-set
* Data Type: CSV

This dataset contains hourly traffic density data for Istanbul, providing information on the number of vehicles at specific locations within each one-hour time interval.

### Datasource2: IMM Open Data Portal
* Metadata URL: https://data.ibb.gov.tr/en/
* Data URL: https://data.ibb.gov.tr/en/dataset/hourly-public-transport-data-set
* Data Type: CSV

This dataset contains hourly public transportation usage data for Istanbul, recording the number of passengers traveling on each mode of public transportation during each one-hour time interval.

### Datasource3: Open-Meteo
* Metadata URL: https://open-meteo.com
* Data URL: https://archive-api.open-meteo.com/v1/archive?latitude=41.01&longitude=28.95&start_date=2022-10-01&end_date=2023-09-30&hourly=temperature_2m,relativehumidity_2m,dewpoint_2m,apparent_temperature,precipitation,rain,snowfall,snow_depth,windspeed_10m,windspeed_100m&timezone=Europe%2FMoscow&format=csv
* Data Type: CSV

This dataset contains hourly weather data for Istanbul, including various weather information such as temperature, rainfall, and other weather conditions within each one-hour time interval.


## Work Packages

1. Data Discovery and Preparation [#1](https://github.com/ozandmrz/made-template/issues/1)
2. Exploratory Data Analysis [#2](https://github.com/ozandmrz/made-template/issues/2)
3. Development of an Automated Data Pipeline [#3](https://github.com/ozandmrz/made-template/issues/3)
4. Implementation of Automated Tests [#4](https://github.com/ozandmrz/made-template/issues/4)
5. Compilation of the Final Report [#5](https://github.com/ozandmrz/made-template/issues/5)
6. Repository Organization and Presentation [#6](https://github.com/ozandmrz/made-template/issues/6)
