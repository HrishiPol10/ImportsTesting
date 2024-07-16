import os
import sys
from collections import defaultdict, deque as c
import numpy as np
import pandas as pd
import seaborn as sns  # Alias Import (Third-party)
import matplotlib as mpl  # Alias Import (Third-party)

from . import sibling_module  # Relative Import
from . import another_sibling_module  # Relative Import

def example_function():
    # Single call
    sys.exit(0)
    
    # Single call with attribute
    path = os.path('a', 'b')
    
    # Double call
    full_path = os.path.join('a', 'b')
    
    # Triple call
    root, ext = os.path.splitext(os.path.basename(full_path))
    
    # Function from numpy
    array = np.array([1, 2, 3])
    
    # Function from collections
    d = defaultdict(list)
    d['key'].append('value')
    
    # Function from collections with alias
    q = deque([1, 2, 3])
    q.appendleft(0)
    
    # Function from pandas
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    
    # Another function from numpy
    mean = np.mean(array)
    
    # Another function from os.path
    is_dir = os.path.isdir(full_path)
    # Single call
    sys.exit(0)
    
    # Single call with attribute
    path = os.path('a', 'b')
    
    # Double call
    full_path = os.path.join('a', 'b')
    
    # Triple call
    root, ext = os.path.splitext(os.path.basename(full_path))
    
    # Function from numpy
    array = np.array([1, 2, 3])
    
    # Function from collections
    d = defaultdict(list)
    d['key'].append('value')
    
    # Function from collections with alias
    q = deque([1, 2, 3])
    q.appendleft(0)
    
    # Function from pandas
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    
    # Another function from numpy
    mean = np.mean(array)
    
    # Another function from os.path
    is_dir = os.path.isdir(full_path)
    # Single call
    sys.exit(0)
    
    # Single call with attribute
    path = os.path('a', 'b')
    
    # Double call
    full_path = os.path.join('a', 'b')
    
    # Triple call
    root, ext = os.path.splitext(os.path.basename(full_path))
    
    # Function from numpy
    array = np.array([1, 2, 3])
    
    # Function from collections
    d = defaultdict(list)
    d['key'].append('value')
    
    # Function from collections with alias
    q = deque([1, 2, 3])
    q.appendleft(0)
    
    # Function from pandas
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    
    # Another function from numpy
    mean = np.mean(array)
    
    # Another function from os.path
    is_dir = os.path.isdir(full_path)

    return {
        "sys_exit": sys.exit,
        "path": path,
        "full_path": full_path,
        "root": root,
        "ext": ext,
        "array": array,
        "defaultdict": d,
        "deque": q,
        "dataframe": df,
        "mean": mean,
        "is_dir": is_dir
    }
