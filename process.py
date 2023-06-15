import functions
from utm import from_latlon, to_latlon

if __name__ == '__main__':
    pass

def latlon_to_utm(df):
    lat_col_num = functions.select_column("Latitude", len(df.columns)-1)
    lon_col_num = functions.select_column("Longitude", len(df.columns)-1)
    northings = []
    eastings = []
    zones = []

    for i in range(len(df)):
        try:
            east, nor, zone_num, zone_let = from_latlon(float(df.loc[i, lat_col_num]), 
                                                        float(df.loc[i, lon_col_num]))
        except:
            nor, east, zone_num, zone_let = ("","","","")
        northings.append(nor)
        eastings.append(east)
        zones.append(f'{zone_num}{zone_let}')
    
    df["Easting"] = eastings
    df["Northing"] = northings
    df["Zone"] = zones

    return df

def utm_to_latlon(df):
    nor_col_num = functions.select_column("Northing", len(df.columns)-1)
    east_col_num = functions.select_column("Easting", len(df.columns)-1)
    lats = []
    longs = []

    for i in range(len(df)):
        try:
            lat, long = to_latlon(float(df.loc[i, east_col_num]), 
                            float(df.loc[i, nor_col_num]),
                            zone_number=17,
                            zone_letter='T'
                        )
        except Exception as e:
            print(e)
            lat, long = ("","")

        lats.append(lat)
        longs.append(long)
    
    df["Latitude"] = lats
    df["Longitude"] = longs

    return df