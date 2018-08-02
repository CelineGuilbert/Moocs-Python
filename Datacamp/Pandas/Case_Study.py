'''
DATA CLEANING 

1) VARIABLES NUMERIQUES
'''Conversion en numérique avec gestion des erreurs, remplacer par Nan

df_clean['wind_speed'] = pd.to_numeric(df_clean['wind_speed'], errors='coerce')


2) DATE USES CASES

Formater un string
Transforme une chaine '58', '758' en '0058', '0758
'''

lambda x:'{:0>4}'.format(x)

'''
Créer une date
'''
date_times = pd.to_datetime(date_string, format='%Y%m%d%H%M')

# ici la date est l'index du DF
print(df_clean.loc['2011-06-20 08:00:00':'2011-06-20 09:00:00', 'dry_bulb_faren'])

# Calcul over a date-index
print(df_clean.loc["2011-Apr":"2011-Jun", 'dry_bulb_faren'].median())



''' resample
#When we have many values for a day : 
# Downsample df_clean by day and aggregate by mean: daily_mean_2011
daily_mean_2011 = df_clean.resample('D').mean()

# Extract the dry_bulb_faren column from daily_mean_2011 using .values: daily_temp_2011 // Retourne un array
daily_temp_2011 =  daily_mean_2011['dry_bulb_faren'].values

# Downsample df_climate by day and aggregate by mean: daily_climate
daily_climate = df_climate.resample('D').mean()

# Extract the Temperature column from daily_climate using .reset_index(): daily_temp_climate // Retourne une Serie
daily_temp_climate = daily_climate.reset_index()['Temperature']

# LOC 
overcast = df_clean.loc[df_clean['sky_condition'].str.contains('OVC')]
'''
0    49.337500
1    49.795833
2    49.900000
Name: Temperature, dtype: float64

# Compute the difference between the two arrays and print the mean difference
difference = daily_temp_2011 - daily_temp_climate
print(difference.mean())
