import os
import sys
from collections import defaultdict
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def example_function():
    np.array([1, 2, 3])
    pd.DataFrame({'A': [1, 2, 3]})
    plt.plot([1, 2, 3])
    os.path.join('a', 'b')
    defaultdict(list)


from math import sqrt, pi
from os.path import join, dirname
import json as js

def another_function():
    result = sqrt(16)
    path = join(dirname(__file__), 'file.txt')
    pi_value = pi
    data = js.loads('{"key": "value"}')
    return result, path, pi_value, data

from scipy.stats import norm
from time import sleep

def third_function():
    norm.pdf(0)
    sleep(1)
