import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from astropy.io import fits
from scipy.ndimage import gaussian_filter
from astropy.visualization import (MinMaxInterval, SqrtStretch, ImageNormalize)

# Load the FITS file
hdulist = fits.open("hst_mos_0093324_acs_wfc_f555w_drz.fits")

# List all extensions
# hdulist.info()

# Access a specific extension by its index or name
header = hdulist[1].header
data = hdulist[1].data

smoothed_data = gaussian_filter(data, sigma=3)
plt.imshow(data, origin='lower', cmap='gray')
plt.colorbar()
plt.show