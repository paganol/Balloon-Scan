import numpy as np

def scan_sky(
    mission_len_hrs,
    sampling_hz,
    spin_rpm,
    rev_per_day,
    lat_deg=67.8558,
    lon_deg=20.225,
    ele_deg=40.0,
    variable_elevation=(5.0, 10),
):
    """

    - ``mission_len_hrs``: mission duration in hrs

    - ``sampling_hz``: sampling rate in hz

    - ``spin_rpm``: Number of rotations around the spin axis per minute

    - ``rev_per_day``: Number of revolutions per day

    - ``lat_deg``: Geographical latitude in deg

    - ``lon_deg``: Geographical longitude in deg

    - ``ele_deg``: Starting elevation in deg

    - ``variable_elevation``: list of (float, int) (Elevation change in deg, number of steps)

    """

    dt = 1.0 / sampling_hz  # sec
    time = np.arange(0, mission_len_hrs * 3600, dt)

    cthspin = np.cos(2 * np.pi * spin_rpm / 60.0 * time)
    sthspin = np.sin(2 * np.pi * spin_rpm / 60.0 * time)

    lon_rad = np.deg2rad(lon_deg)

    cpaylon = np.cos(
        lon_rad + 2 * np.pi * (1 + rev_per_day) / 24.0 / 3600.0 * time
    )
    spaylon = np.sin(
        lon_rad + 2 * np.pi * (1 + rev_per_day) / 24.0 / 3600.0 * time
    )

    clat = np.cos(np.deg2rad(lat_deg))
    slat = np.sin(np.deg2rad(lat_deg))

    if variable_elevation[1] > 0:
        ntime = len(time)
        nstepperpos = int(ntime / variable_elevation[1])
        normang = int(((ntime - 1) / nstepperpos))
        ele_deg += (
            variable_elevation[0]
            * (np.arange(ntime) / nstepperpos).astype(int)
            / normang
        )

    cele = np.cos(np.deg2rad(ele_deg))
    sele = np.sin(np.deg2rad(ele_deg))

    cdelang = np.cos(
        2 * np.pi * spin_rpm / 60.0 * time
        - lon_rad
        - 2 * np.pi * (1 + rev_per_day) / 24.0 / 3600.0 * time
    )
    sdelang = np.sin(
        2 * np.pi * spin_rpm / 60.0 * time
        - lon_rad
        - 2 * np.pi * (1 + rev_per_day) / 24.0 / 3600.0 * time
    )

    x = (
        clat * sele * cpaylon
        + cele * slat * cthspin
        + cele * (-1 + slat) * sdelang * spaylon
    )
    y = (
        clat * sele * spaylon
        + cele * slat * sthspin
        + cele * (-1 + slat) * sdelang * cpaylon
    )
    z = slat * sele - cele * clat * cdelang

    return (x, y, z)
