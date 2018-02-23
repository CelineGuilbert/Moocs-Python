# Downsample to 6 hour data and aggregate by mean: df1
df1 = df['Temperature'].resample('6h').mean()
# Downsample to daily data and count the number of data points: df2
df2 = df['Temperature'].resample('D').count()



# Extract temperature data for August: august
august = df['Temperature'].loc['2010-8']


# Extract temperature data for August: august
august = df['Temperature'].loc['2010-8']

# Downsample to obtain only the daily highest temperatures in August: august_highs
august_highs = august.resample('D').max()
# Extract temperature data for February: february
february = df['Temperature'].loc['2010-2']
# Downsample to obtain the daily lowest temperatures in February: february_lows
february_lows = february.resample('D').min()


# Extract data from 2010-Aug-01 to 2010-Aug-15: unsmoothed
unsmoothed = df['Temperature']['2010-Aug-01':'2010-Aug-15']
# Apply a rolling mean with a 24 hour window: smoothed
smoothed = unsmoothed.rolling('24h')
# Create a new DataFrame with columns smoothed and unsmoothed: august
august = pd.DataFrame({'smoothed':unsmoothed, 'unsmoothed':smoothed})
# Plot both smoothed and unsmoothed data using august.plot().
august.plot()
plt.show()
