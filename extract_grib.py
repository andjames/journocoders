import pygrib
import numpy as np
import pandas as pd

# Open the GRIB2 file
grbs = pygrib.open('sof-d.20250405.t00z.0p125.agricultural.europe.f000.grib2')
variable = 'soilw'
# Select your specific GRIB message (here: Wind at 100m above surface level)
grb = grbs.select(shortName=variable)[0]

# Extract data and lat/lon coordinates
data, lats, lons = grb.data()

# Flatten the data for CSV export
flat_data = {
    'latitude': lats.flatten(),
    'longitude': lons.flatten(),
    'var': data.flatten()
}

# Create DataFrame
df = pd.DataFrame(flat_data)

# Filter data where ssrd > 0.1
df_filtered = df[df['var'] > 0.1]

# Export filtered data to CSV
df_filtered.to_csv('soilw.csv', index=False)

print("Filtered data exported to soilw.csv successfully!")