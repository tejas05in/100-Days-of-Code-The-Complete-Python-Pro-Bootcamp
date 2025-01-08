# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again."
# }


# # Add a new item to the dictionary
# programming_dictionary["Loop"] = "The action of doing something over and over again."


# wipe the dictionary
# programming_dictionary = {}

# edit an item in the dictionary
# print(programming_dictionary["Bug"])
# programming_dictionary["Bug"] = "A moth in your computer."
# print(programming_dictionary["Bug"])

# loop through a dictionary
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])

# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nesting a list in a dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

# Nesting a dictionary in a dictionary
travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    }
}

# Nesting a dictionary in a list
travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    }
]