# Exercise 2: Travel Log

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
  },
]

def add_new_country(country, visits, cities):
    travel_log.append({
        "country":country,
        "visits":visits,
        "cities":cities
    })
    print(f"You've visited {country} {visits} time(s)")
    if len(cities)<=1:
      print("You've been to "+ "".join(cities))
    elif len(cities)==2:
      print("You've been to "+", ".join(cities[0:len(cities)-1])+" and "+cities[len(cities)-1])
    else:
      print("You've been to "+", ".join(cities[0:len(cities)-1])+", and "+cities[len(cities)-1])

add_new_country("Russia", 2, ["Moscow", "Petersburg"])
print(travel_log)
