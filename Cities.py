import pandas as pd
from geopy import distance
import argparse

parser = argparse.ArgumentParser(description='Geography processer')
parser.add_argument('-f', '--func',
                    help='Name of the function to use, "get_cities" to get requiered cities with coordinates for subtask 1,'
                         ' "get_distance" for subtask2, run within directory with source file', required=True)
parser.add_argument('-p', '--parameters',
                    help='Parameters for selected function, for "get_cities" - country in iso2 encoding (us, au, ca etc.)'
                         ' for "get_distance" - countr_a, city_a, country_b, city_b where country_a & country_b = country in iso2 encoding,'
                         ' city_a, city_b = city coded name from column "City" from source file', nargs='+', required=True)

args = parser.parse_args()
print('Reading source file')
df = pd.read_csv('worldcitiespop.txt.gz', compression='gzip', encoding='ANSI', low_memory=False)
contry_set = set(df.Country.values)


def get_cities_of_country(country_iso2_code):
    country_iso2_code = country_iso2_code.lower()
    assert country_iso2_code in contry_set, print('Code was not found, please use iso2 codes, please refer to'
                                                  ' https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Current_codes for list of iso codes')
    df_c = df[df.Country == country_iso2_code]
    # We assume that northernmost city - is city with biggest Latitude and southernmost is the opposite - with the least Latitude
    # The same goes for easternmost and westernmost but with Longitude as measure
    north = df_c.loc[df_c.Latitude.idxmax()]
    south = df_c.loc[df_c.Latitude.idxmin()]
    east = df_c.loc[df_c.Longitude.idxmax()]
    west = df_c.loc[df_c.Longitude.idxmin()]
    # return list of cities, order as in the task
    cities_l = [[c['AccentCity'], c['Latitude'], c['Longitude']] for c in [north, south, west, east]]
    print('Listing of cities from task')
    for part, city in zip((c + 'ernmost' for c in ['North', 'South', 'East', 'West']), cities_l):
        print(part + ' city:\n\tCity name - ' + city[0] + ':\n\tLatitude - ' + str(city[1]) + '\n\tLongitude - ' + str(city[2]))


def get_distance_between_cities(country_a, city_a, country_b, city_b):
    coord_a = df[(df.Country == country_a) & (df.City == city_a)][['Latitude', 'Longitude']].values[0]
    coord_b = df[(df.Country == country_b) & (df.City == city_b)][['Latitude', 'Longitude']].values[0]
    print('Distance between ' + ':'.join([country_a, city_a]) + ' and ' + ':'.join([country_b, city_b]) + ' is {:.2f} kilometers'.format(
        distance.distance(coord_a, coord_b).km))


func = get_cities_of_country if args.func == 'get_cities' else get_distance_between_cities if args.func == 'get_distance' else None
assert func is not None, print('Wrong func name use "get_cities" or "get_distance"')
func(*args.parameters)
