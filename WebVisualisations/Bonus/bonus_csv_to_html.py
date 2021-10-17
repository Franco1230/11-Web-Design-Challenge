import pandas as pd

# Read CSV data
cities = pd.read_csv("Resources/cities_weather.csv")
cities_df = pd.DataFrame(cities)
cities_df = cities.rename(columns = {"City_ID": "City ID",
                                     "Humidity": "Humidity %",
                                     "Lat": "Latitude",
                                     "Lng": "Longitude",
                                     "Max Temp": "Max Temp(F)",
                                     "Wind Speed": "Wind Speed(MPH)"})

cities_df = cities_df.iloc[:, [0, 7, 1, 2, 3, 4, 5, 6, 8]]
cities_df.to_html("Resources/data.html", index = False)                                     