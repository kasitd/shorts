import json

cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""
    for key, value in cars.items():
        if key == 'Jeep':
            models = ', '.join(value)
            return models

def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    res = [[i for i in cars[x]] for x in cars.keys()]
    return list(list(zip(*res))[0])


def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    res = []
    ser = []

    for x in cars.keys():
        for i in cars[x]:
            if grep.lower() in i.lower():
                res.append(i)
    return sorted(res)




def sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    res = []
    ser = []
    klucz = []
    for x in cars.keys():
        for i in cars[x]:
            res.append(i)
        ser.append(sorted(res))
        res = []
    for k in cars.keys():
        klucz.append(k)

    cars_copy = dict(zip(klucz,ser))

    return cars_copy


