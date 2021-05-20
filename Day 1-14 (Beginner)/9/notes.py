# dictionaries -> data structure with keys and values

programming_dictionary = {
    "Bug": "An error that prevents the program from running as expected",
    "Function": "A piece of code that you can call over and over again"
}
print(programming_dictionary)
programming_dictionary['Loop'] = 'Action of doing something repeatedly'
print(programming_dictionary)
# we can wipe out the dictionary by redefining them as an empty dictionary

# nesting lists in a dictionary
travel_log1 = {
    'France': ['Paris','Lille','Dijon'],
    "Germany": ['Berlin', 'Hamburg', 'Stuttgart']
}

# nesting a dictionary in a dictionary
travel_log2 = {
    'France':{
        'cities_visited':['Paris','Lille','Dijon'],
        'total_visited':100
    },
    'Germany':{
        'cities_visited':['Berlin','Hamburg','Stuttgart'],
        'total_visited':14
    }
}
# nesting dictionary in a list
travel_log3 = [
    {
        'country':'France',
        'cities_visited':['Paris','Lille','Dijon'],
        'total_visited':100
    },
    {
        'country':'Germany',
        'cities_visited':['Berlin','Hamburg','Stuttgart'],
        'total_visited':14
    }
]
print(travel_log3)