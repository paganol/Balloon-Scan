# Balloon Scan
Scan of a spinning balloon

## Installation

```
git clone https://github.com/paganol/Balloon-Scan.git
cd Balloon-Scan
pip install -e .
```

## Usage

```python

from balloon_scan import scan_sky 
import numpy as np
import matplotlib.pyplot as plt
import healpy as hp

# Kiruna
latitude = 67.8558  # deg
longitude = 20.225  # deg
# 36 hrs

elevation = 50.0  # deg

mission_time_hrs = 36 # hrs
spin = 1.0  # rmp

sampling_rate = 50.0  # Hz

period_of_revolution_days = np.inf  # days, with np.inf the balloon stays over the launch site

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

nside = 256
npix = hp.nside2npix(nside)
pix = hp.vec2pix(nside, vecx, vecy, vecz)

h = np.zeros(npix)
pixel_occurrences = np.bincount(pix)
h[0 : len(pixel_occurrences)] = pixel_occurrences
```
![hits](https://user-images.githubusercontent.com/5398538/135595088-062b2999-b832-4d93-ace8-6eecc9c6c629.png)

Parameters:

    - ``mission_len_hrs``: mission duration in hrs

    - ``sampling_hz``: sampling rate in hz

    - ``spin_rpm``: Number of rotations around the spin axis per minute

    - ``rev_per_day``: Number of revolutions per day

    - ``lat_deg``: Geographical latitude in deg

    - ``lon_deg``: Geographical longitude in deg

    - ``ele_deg``: Starting elevation in deg

    - ``variable_elevation``: list of (float, int) (Elevation change in deg, number of steps)
