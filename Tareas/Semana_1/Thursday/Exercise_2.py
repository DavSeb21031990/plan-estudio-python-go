import random

lat = random.uniform(-90.0, 90.0)
lon = random.uniform(-180.0, 180.0)

coords = (lat, lon)
coords[0] = 0
print(f"Latitude: {coords[0]}, Longitude: {coords[1]}")
