import pandas as pd
from geopy import distance
import argparse
from math import cos, asin, sqrt

parser = argparse.ArgumentParser(description='Geography processer')
parser.add_argument('-f', '--func',
                    help='Name of the function to use:\n"get_cities" to get requiered cities with coordinates for subtask 1\n'
                         '"get_distance" for subtask2\n"get_nearest" for optional task. Run within directory with source file.',
                    required=True)
parser.add_argument('-p', '--parameters',
                    help='Parameters for selected function:\nFor "get_cities" - country in iso2 encoding (us, au, ca etc.).\n'
                         'For "get_distance" - countr_a, city_a, country_b, city_b where country_a & country_b = country in iso2 encoding,'
                         ' city_a, city_b = city coded name from column "City" from source file.\n'
                         'For "get_nearest" - latitude, longitude, number_of_nearest_cities.', nargs='+', required=True)

args = parser.parse_args()
print('Reading source file...')
df = pd.read_csv('worldcitiespop.txt.gz', compression='gzip', encoding='ANSI', low_memory=False)
country_set = set(df.Country.values)


def get_cities_of_country(country_iso2_code):
    print("Finding edge cities...")
    country_iso2_code = country_iso2_code.lower()
    assert country_iso2_code in country_set, print('Code was not found, please use iso2 codes, please refer to'
                                                   ' https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Current_codes for iso codes')
    df_c = df[df.Country == country_iso2_code]
    # We assume that northernmost city - is city with biggest Latitude and southernmost is the opposite - with the least Latitude
    # The same goes for easternmost and westernmost but with Longitude as measure
    north = df_c.loc[df_c.Latitude.idxmax()]
    south = df_c.loc[df_c.Latitude.idxmin()]
    east = df_c.loc[df_c.Longitude.idxmax()]
    west = df_c.loc[df_c.Longitude.idxmin()]
    cities_l = [[c['AccentCity'], c['Latitude'], c['Longitude']] for c in [north, south, west, east]]
    print('Listing of cities from task')
    for part, city in zip((c + 'ernmost' for c in ['North', 'South', 'East', 'West']), cities_l):
        print(part + ' city:\n\tCity name - ' + city[0] + ':\n\tLatitude - ' + str(city[1]) + '\n\tLongitude - ' + str(city[2]))


def get_distance_between_cities(country_a, city_a, country_b, city_b):
    print('Calculating distance...')
    coord_a = df[(df.Country == country_a) & (df.City == city_a)][['Latitude', 'Longitude']].values[0]
    coord_b = df[(df.Country == country_b) & (df.City == city_b)][['Latitude', 'Longitude']].values[0]
    print('Distance between ' + ':'.join([country_a, city_a]) + ' and ' + ':'.join([country_b, city_b]) + ' is {:.2f} kilometers'.format(
        distance.distance(coord_a, coord_b).km))


# Stole this from stack overflow https://stackoverflow.com/questions/41336756/find-the-closest-latitude-and-longitude
def _distance(lat1, lon1, lat2, lon2):
    p = 0.017453292519943295
    a = 0.5 - cos((lat2 - lat1) * p) / 2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 12742 * asin(sqrt(a))


def get_nearest_cities(lat, long, n_cities):
    print('Finding nearest...')
    # args parsed as string, so casting is required
    lat, long, n_cities = float(lat), float(long), int(n_cities)
    used_values = [(x, v, city, country) for x, v, city, country in df[['Latitude', 'Longitude', 'AccentCity', 'Country']].values]
    closest_l = sorted(used_values, key=lambda p: _distance(lat, long, p[0], p[1]))[:n_cities]
    print('Closest {:n} city(ies) for given coordinates Latitude - {:.4f}, Longitude - {:.4f} is/are:'.format(n_cities, lat, long))
    for city in closest_l:
        print('Country - {:s}\nCity - {:s}\nLatitude - {:.4f}\nLongitude - {:.4f}'.format(city[3], city[2], city[0], city[1]))


func = get_cities_of_country if args.func == 'get_cities' else \
    get_distance_between_cities if args.func == 'get_distance' else \
    get_nearest_cities if args.func == 'get_nearest' else None
assert func is not None, print('Wrong func name use "get_cities", "get_distance" or "get_nearest"')
func(*args.parameters)
