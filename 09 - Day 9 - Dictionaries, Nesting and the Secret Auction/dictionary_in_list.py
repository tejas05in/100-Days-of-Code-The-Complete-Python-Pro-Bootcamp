# coding exercise 9.2: Dictionary in List
travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
        
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]        
    }
]

# TODO: Write a function that will allow new countries
# to be added to the travel_log. The function should take
# in the dictionary with the country, number of visits and
# list of cities visited and add it to the travel_log.
def add_new_country(country:str, visits:int, cities:list) -> None:
    new_details = {}
    new_details["country"] = country
    new_details["visits"] = visits
    new_details["cities"] = cities
    travel_log.append(new_details)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)