from balloon_scan import scan_sky 
import numpy as np
import matplotlib.pyplot as plt
import healpy as hp


namefile = "pdf/hitmap_long_"

# Kiruna
latitude = 67.8558  # deg
longitude = 20.225  # deg
# 36 hrs or 45 hrs

# Longyearbyen
# latitude = 78.2232
# longitude = 15.6267
# 5 days

# Timmins
# latitude = 48.4758
# longitude = -81.3305
# 24 hrs

# Alice Springs
# latitude = -23.6980
# longitude = 133.8807
# 34 hrs
# https://stratocat.com.ar/news20170419-e.htm

elevation = 50.0  # deg

mission_time_hrs = 35 #24 * 5
spin = 1.0  # rmp

nside = 256
sampling_rate = 50.0  # Hz

period_of_revolution_days = np.inf  # days

revolutions_per_day = 1.0 / period_of_revolution_days

vecx, vecy, vecz = scan_sky(
    mission_time_hrs,
    sampling_rate,
    spin,
    revolutions_per_day,
    latitude,
    longitude,
    elevation,
    variable_elevation=(0, 0),
)

npix = hp.nside2npix(nside)
pix = hp.vec2pix(nside, vecx, vecy, vecz)

h = np.zeros(npix)
pixel_occurrences = np.bincount(pix)
h[0 : len(pixel_occurrences)] = pixel_occurrences

