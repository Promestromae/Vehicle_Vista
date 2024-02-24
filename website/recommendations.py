def get_recommendations(user_id):
    user_preferences = get_user_preferences(user_id)
    recommended_cars = fetch_recommended_cars(user_preferences)
    return recommended_cars

def get_user_preferences(user_id):
    user_preferences = {
                        'preferred_make': 'Toyota',
                                'preferred_model': 'Camry',
                                        'max_price': 30000
                                            }
    return user_preferences

def fetch_recommended_cars(user_preferences):
    recommended_cars = [
                        {'make': 'Toyota', 'model': 'Camry', 'year': 2020, 'price': 25000},
                                {'make': 'Honda', 'model': 'Accord', 'year': 2019, 'price': 27000},
                                        {'make': 'Ford', 'model': 'Fusion', 'year': 2018, 'price': 22000}
                                            ]
    return recommended_cars

