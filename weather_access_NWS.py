
# Import the required libraries
import requests
import geopy
import tkinter as tk
import pandas as pd

# Specifying location coordinates in decimal degrees in the interface

lat = float(input("Latitude: "))
lat_dir = input("N or S? ")
lon = float(input("Longitude: "))
lon_dir = input("E or W? ")

if lat_dir == "N":
    lat = lat
else:
    lat = -lat

if lon_dir == "E":
    lon = lon
else:
    lon = -lon

from geopy.geocoders import Nominatim
locator = Nominatim(user_agent = "MyGeocoderApp v1.0")
location  = locator.reverse((lat, lon))
print("Your location is", location.address)

# Defining API endpoint and creating a unique URL that helps to identify our application.

api_key = "https://api.weather.gov"                                   # This is the base URL for the National Weather Service API. 

headers = {
    "User-Agent": "myweatherapp.com, contact@myweatherapp.com"
    }                                                                            # User agent is required for identifying our application. 

url_metadata = f"{api_key}/points/{lat},{lon}"                                   # This is our unique URL created using f-string. 

# Making an HTTP get request to the constructed URL and storing the response in 'response' variable.

response = requests.get(url_metadata, headers = headers)

# We need to check the response status to ensure that the request was successful. 

if response.status_code == 200:
    loc_metadata = response.json()
    url_forecast = loc_metadata["properties"]["forecast"]

    forecast_response = requests.get(url_forecast, headers = headers)

    # We need to check the response status again. 

    if forecast_response.status_code ==200:
        forecast_data = forecast_response.json()
        periods = forecast_data["properties"]["forecast"]

        selected_parameters = [
        ("Start Time", "startTime"),
        ("End Time", "endTime"),
        ("Temperature", "temperature"),
        ("Relative Humidity", "relativeHumidity"),
        ("Wind Speed", "windSpeed"),
        ("Cloud Cover", "clouds")
        ]

        df = pd.DataFrame({param: [period.get(param, None) for period in periods] for param in selected_parameters})

        print("Weather Forecast Data (Selected Parameters):")

        print(df.to_string(index=False))

    else:

        print(f"Error. Status code: {forecast_response.status_code}")

else:

    print(f"Error. Status code: {response.status_code}")


    

# Using tkinter to create an interface
#top = tk.Tk()
#top.mainloop()

#from tkinter as tk import messagebox

#answer = message.askyesno("Question","Is this location correct?")