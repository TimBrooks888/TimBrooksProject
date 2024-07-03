# unit_converter.py
def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

km = 10
miles = 6.2
print(f"{km} km is {km_to_miles(km)} miles")
print(f"{miles} miles is {miles_to_km(miles)} km")
