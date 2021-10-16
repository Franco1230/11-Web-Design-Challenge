import pandas as pd

# Read CSV data
cities = pd.read_csv("Resources/cities.csv")
cities_df = pd.DataFrame(cities)
cities_df = cities.rename(columns = {"City_ID": "City ID",
                                     "Humidity": "Humidity %",
                                     "Lat": "Latitude",
                                     "Lng": "Longitude",
                                     "Max Temp": "Max Temp(F)",
                                     "Wind Speed": "Wind Speed(MPH)"})
cities_df.to_html("Resources/weather_data.html", index = False)                                     