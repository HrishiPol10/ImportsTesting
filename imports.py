# import os  # Whole Module Import
# import sys  # Whole Module Import

# from os import path  # Specific Import
# from os import *  # Wildcard Import
# import numpy as np  # Alias Import

# try:
#     import cPickle as pickle  
# except ImportError:
#     import pickle

# from . import sibling_module  # Relative Import
# from .. import parent_module  # Relative Import Upwards


import os  # Whole Module Import
import sys  # Whole Module Import
import numpy  # Whole Module Import
import pandas  # Whole Module Import
import matplotlib

from os import path, remove  # Specific Import
from os import sep, environ  # Specific Import
from numpy import array  # Specific Import (Third-party)
from pandas import DataFrame  # Specific Import (Third-party)
from matplotlib import pyplot as plt  # Specific Import (Third-party)
from matplotlib import figure as Figure  # Specific Import (Third-party)

from os import *  # Wildcard Import
from sys import *  # Wildcard Import

import numpy as np  # Alias Import (Third-party)
import pandas as pd  # Alias Import (Third-party)
import matplotlib.pyplot as plt # Alias Import (Third-party)
import matplotlib.pyplot as plt # Alias Import (Third-party)
import seaborn as sns  # Alias Import (Third-party)
import matplotlib as mpl  # Alias Import (Third-party)

from . import sibling_module  # Relative Import
from . import another_sibling_module  # Relative Import

from .. import parent_module  # Relative Import Upwards
from .. import another_parent_module  # Relative Import Upwards

