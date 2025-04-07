import pygrib

# Open the GRIB file
ds = pygrib.open("sof-d.20250405.t00z.0p125.agricultural.europe.f000.grib2")

# Iterate through each grib_message in the dataset
# for grib_message in ds:
#     print("Keys in the grib_message:", grib_message)
#     print("=======================================")

for v in ds:
    print(v, "SHORT NAME:", v['shortName'], "Units:", v['units'], "Levels:", v['level'])
    #print(v, ds[v].attrs["long_name"], ds[v].attrs["units"])
    print("=======================================")
# Close the GRIB file
ds.close()


#sof-d.20230724.t12z.0p125.aviation.conus.f048.grib2