class FlightData:
    '''Flight Data Structure'''
    def __init__(self, dep_airport, arr_airport, cityTo, countryTo, price, dep_time, arr_time, link):
        self.dep_airport = dep_airport
        self.arr_airport = arr_airport
        self.city_from = 'Jakarta'
        self.countryFrom = 'Indonesia'
        self.cityTo = cityTo
        self.countryTo = countryTo
        self.price = price
        self.dep_date = dep_time.split("T")[0]
        self.dep_time = dep_time.split("T")[1].split(".")[0]
        self.arr_date = arr_time.split("T")[0]
        self.arr_time = arr_time.split("T")[1].split(".")[0]
        self.link = link
        
