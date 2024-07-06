import os  # Whole Module Import
from os import path  # Specific Import
from os import *  # Wildcard Import
import numpy as np  # Alias Import
import sys  # Conditional Import (used in the try-except block)
from . import sibling_module  # Relative Import
from .. import parent_module  # Relative Import Upwards

try:
    import cPickle as pickle  # Conditional Import
except ImportError:
    import pickle


# Import styles breakdown:
# Whole Module:
#   - os: 1 times
#   - sys: 1 times
#   - pickle: 1 times
# Specific Import:
#   - os.path: 1 times
#   - os.remove: 1 times
# Wildcard Import:
#   - os: 1 times
# Alias Import:
#   - numpy: 1 times
#   - pandas: 1 times
#   - matplotlib.pyplot: 1 times
#   - cPickle: 1 times
#   - Tkinter: 1 times
#   - tkinter: 1 times
# Conditional Import:
#   - cPickle: 1 times
# Relative Import:
#   - .: 1 times
# Relative Import Upwards:
#   - None: 1 times
