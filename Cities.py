import pandas as pd
import os
import geopy as gp

df = pd.read_csv('worldcitiespop.txt.gz', compression='gzip', encoding='ANSI', low_memory=False)
# df_iso = pd.read_csv('iso_codes.csv')
contry_s = set(df.Country.values)


# iso_s = set([str(c).lower() for c in df_iso.Code.values])
# print(contry_s - iso_s)

def get_cities_of_country(country_iso2_code):
    country_iso2_code = 'us'
    country_iso2_code = country_iso2_code.lower()
    assert country_iso2_code in contry_s, print('Code was not found, please use iso2 codes, codes could be foun here -'
                                                ' https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Current_codes')
    df_c = df[df.Country == country_iso2_code]
    north = df_c.loc[df_c.Latitude.idxmax()]
    south = df_c.loc[df_c.Latitude.idxmin()]
    east = df_c.loc[df_c.Longitude.idxmax()]
    west = df_c.loc[df_c.Longitude.idxmin()]
    print(df_c)


get_cities_of_country('ua')
