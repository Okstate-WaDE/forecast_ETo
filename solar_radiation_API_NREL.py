# Import the required libraries
import requests
import geopy
import pandas as pd

# Specifying location coordinates in decimal degrees in the interface

lat = float(input("Latitude: "))
lat_dir = input("N or S? ").upper()
lon = float(input("Longitude: "))
lon_dir = input("E or W? ").upper()

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

api_key = 'VmnrNGk5WcKhhR4fh5xj0z7qM1Rh2lm2ntHacwmW'

def solar_radiation_data_nrel(api_key, lat, lon):
    base_url = f"https://developer.nrel.gov/api/solar/solar_resource/v1.json"

    # Specifing the parameters
    params = {
        'api_key': api_key,
        'lat': lat,
        'lon': lon,
    }

    # Making the get request
    response = requests.get(base_url, params=params)

    # We need to check the response status to ensure that the request was successful. 
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None


# Making a request to get solar radiation data
radiation_data = solar_radiation_data_nrel(api_key, lat, lon)

print(radiation_data)
