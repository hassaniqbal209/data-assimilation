import numpy as np
import dapy.filters as filters
import dapy.utils.pou as pou
import dapy.ot as ot
from dapy.models import SpatialIncompressibleFluidModel
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#matplotlib inline
plt.style.use('seaborn-white')
plt.rcParams['figure.dpi'] = 100
plt.rcParams['animation.html'] = 'html5'