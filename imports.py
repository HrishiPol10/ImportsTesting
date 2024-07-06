import os
import sys

from os import path, remove

from os import *
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

try:
    import cPickle as pickle
except ImportError:
    import pickle
if sys.version_info[0] < 3:
    import Tkinter as tk
else:
    import tkinter as tk


from . import sibling_module

from .. import parent_module


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
