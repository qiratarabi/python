def hotel_cost(nights):
    return 140 * nights
def plane_cost(city):
    if city == "New York":
        return 850
    elif city == "Dubai":
        return 200
    elif city == "Los Angeles":
        return 700
    
    def rental_car_cost(days):
        return 30 * days
    
    def  trip_cost(city, days, nights):
        return hotel_cost(nights) + rental_car_cost(days) + plane_cost(city)
    
    print(trip_cost("Los Angeles", 5, 3))