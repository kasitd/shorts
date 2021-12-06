from collections import Counter

import requests

CAR_DATA = 'https://bites-data.s3.us-east-2.amazonaws.com/cars.json'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(CAR_DATA).json()


# your turn:
def most_prolific_automaker(year):
    """Given year 'year' return the automaker that released
       the highest number of new car models"""
    moja_lista = []

    for dict in data:

        for keys, values in dict.items():

            if str(year) in str(dict.values()):

                moja_lista.append(dict["automaker"])

    return max(Counter(moja_lista), key=Counter(moja_lista).get)


def get_models(automaker, year):
    moja_lista = []
    for dict in data:
        if str(year) in str(dict.values()) and automaker in dict.values():
            moja_lista.append(dict["model"])

    return set(moja_lista)