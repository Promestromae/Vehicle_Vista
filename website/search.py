def search_cars(criteria):
    searched_cars = [
                        {'make': 'Toyota', 'model': 'Camry', 'year': 2020, 'price': 25000},
                                {'make': 'Honda', 'model': 'Accord', 'year': 2019, 'price': 27000},
                                        {'make': 'Ford', 'model': 'Fusion', 'year': 2018, 'price': 22000}
                                            ]
            
    filtered_cars = []
    for car in searched_cars:
        if 'make' in criteria and car['make'] == criteria['make']:
            filtered_cars.append(car)
            
    return filtered_cars

