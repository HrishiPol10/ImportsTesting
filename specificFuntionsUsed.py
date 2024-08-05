# import os
# import sys
# from collections import defaultdict, deque
# import numpy as np
# import pandas as pd
# import seaborn as sns  # Alias Import (Third-party)
# import matplotlib as mpl  # Alias Import (Third-party)

# from . import sibling_module  # Relative Import
# from . import another_sibling_module  # Relative Import

# def example_function():
#     # Single call
#     sys.exit(0)
    
#     # Single call with attribute
#     path = os.path('a', 'b')
    
#     # Double call
#     full_path = os.path.join('a', 'b')
    
#     # Triple call
#     root, ext = os.path.splitext(os.path.basename(full_path))
    
#     # Function from numpy
#     array = np.array([1, 2, 3])
    
#     # Function from collections
#     d = defaultdict(list)
#     d['key'].append('value')
    
#     # Function from collections with alias
#     q = deque([1, 2, 3])
#     q.appendleft(0)
    
#     # Function from pandas
#     df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    
#     # Another function from numpy
#     mean = np.mean(array)
    
#     # Another function from os.path
#     is_dir = os.path.isdir(full_path)


#      # Triple call
#     root, ext = os.path.splitext(os.path.basename(full_path))
    
#     # Function from numpy
#     array = np.array([1, 2, 3])
    
#     # Function from collections
#     d = defaultdict(list)
#     d['key'].append('value')
    
#     # Function from collections with alias
#     q = deque([1, 2, 3])
#     q.appendleft(0)
    
#     # Function from pandas
#     df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    
#     # Another function from numpy
#     mean = np.mean(array)
    
#     # Another function from os.path
#     is_dir = os.path.isdir(full_path)

#     return {
#         "sys_exit": sys.exit,
#         "path": path,
#         "full_path": full_path,
#         "root": root,
#         "ext": ext,
#         "array": array,
#         "defaultdict": d,
#         "deque": q,
#         "dataframe": df,
#         "mean": mean,
#         "is_dir": is_dir
#     }


# sample_script.py

import os
import sys
from collections import defaultdict, deque
import numpy as np
import pandas as pd
from typing import List, Tuple

# Alias import
import matplotlib.pyplot as plt

class MyClass:
    def __init__(self, data: List[int]):
        self.data = data

    def compute_average(self) -> float:
        return np.mean(self.data)

    def create_dataframe(self) -> pd.DataFrame:
        return pd.DataFrame({"data": self.data})

def example_function():
    # Using os functions
    files = os.listdir('.')
    path = os.path.join('a', 'b')

    # Using collections
    d = defaultdict(list)
    q = deque([1, 2, 3])
    
    # Using numpy
    array = np.array([1, 2, 3])
    reshaped = array.reshape((3, 1))
    average = np.mean(array)

    # Using pandas
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

    return df

# Alias usage
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()
