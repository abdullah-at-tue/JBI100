import pandas as pd

# dtype=[
#     int,int,str,int,str,str,str,str,int,int,int,str,int,int,int,int,str,str,str,str,int,float,datetime,int,int,int,int,str,str,int,datetime,str,int
# ]
df = pd.read_csv(__path__[0] + "/dataset.csv", low_memory=False).set_index('id')
df_us_zips = pd.read_csv(__path__[0] + "/uszips.csv").set_index('zip')

# len(df_us_zips) # 33784
# len(df['zip_code'].unique()) # 17101
# len(df['id'].unique()) # 889447
# len(df) # 889447

if 'lat' not in df or 'lng' not in df:
    for i, (index, row)  in enumerate(df.iterrows(), start=1):
        print(f"[PRE-ANALYSE] LOADING LAT AND LNG; Progress: {round(i/889447*100, 2)}%")

        zip_code: int = int(row['zip_code'])
        if zip_code in df_us_zips.index:
            df.loc[index, 'lat'] = df_us_zips.loc[zip_code]['lat']
            df.loc[index, 'lng'] = df_us_zips.loc[zip_code]['lng']
        else:
            df.loc[index, 'lat'] = None
            df.loc[index, 'lng'] = None

    df.to_csv(__path__[0] + "/dataset.csv")

if 'incident_datetime' not in df:
    print("[PRE-ANALYSE] COMPUTING INCIDENT DATETIME;")

    df['incident_datetime'] = pd.to_datetime(df['date_of_incident'] + ' ' + df['time_of_incident'])
    df['incident_datetime'] = df['incident_datetime'].astype('datetime64[ns]')

    df.to_csv(__path__[0] + "/dataset.csv")

df['date_of_incident'] = df['date_of_incident'].astype('datetime64[ns]')
