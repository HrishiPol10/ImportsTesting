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
