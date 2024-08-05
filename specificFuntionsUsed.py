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
# sample_script.py
import os
import sys
from collections import defaultdict, deque
import numpy as np
import pandas as pd
from typing import List, Tuple, Dict, Union, Callable, Awaitable, Set, Overload

# Alias import
import matplotlib.pyplot as plt

# Define a function using Union
def calculate_area(shape: Union[str, Tuple[int, int]]) -> float:
    if isinstance(shape, str):
        if shape == 'circle':
            return 3.1415 * 5 * 5
    elif isinstance(shape, tuple):
        return shape[0] * shape[1]
    return 0.0

# Define a callable function
def execute_callable(func: Callable[[int, int], int], a: int, b: int, func: Awaitable[None], func: Callable[[int, int], int]) -> int:
    return func(a, b)

# Define an awaitable function
async def async_function() -> Awaitable[None]:
    print("This is an async function")
    await asyncio.sleep(1)

# Use Overload for function definitions
@Overload
def overloaded_function(x: int) -> int:
    return x * 2

@Overload
def overloaded_function(x: str) -> str:
    return x * 2

# Use Set type
def process_numbers(numbers: Set[int]) -> int:
    return sum(numbers)

class DataProcessor:
    def __init__(self, numbers: List[int], labels: Tuple[str, str]):
        self.numbers = numbers
        self.labels = labels

    def compute_statistics(self) -> Tuple[float, float]:
        mean = np.mean(self.numbers)
        std_dev = np.std(self.numbers)
        return mean, std_dev

    def to_dataframe(self) -> pd.DataFrame:
        return pd.DataFrame({
            "numbers": self.numbers,
            "label1": [self.labels[0]] * len(self.numbers),
            "label2": [self.labels[1]] * len(self.numbers)
        })

def process_data(numbers: List[int], labels: Tuple[str, str], func: Callable[[int, int], int]) -> pd.DataFrame:
    processor = DataProcessor(numbers, labels)
    stats = processor.compute_statistics()
    df = processor.to_dataframe()
    
    # Use a dictionary to map statistics
    stats_dict: Dict[str, float] = {
        "mean": stats[0],
        "std_dev": stats[1]
    }

    print("Statistics:", stats_dict)
    
    # Use numpy operations
    array = np.array(numbers)
    reshaped_array = array.reshape(-1, 1)  # Detect this reshape call
    print("Reshaped Array:\n", reshaped_array)
    
    return df

# Alias usage
plt.plot([1, 2, 3], [4, 5, 6])
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Sample Plot")
plt.show()

# Function call examples
print(calculate_area("circle"))
print(calculate_area((4, 5)))
print(execute_callable(lambda x, y: x + y, 5, 10))
print(process_numbers({1, 2, 3, 4}))

# Ensure asyncio is imported for Awaitable to be valid
import asyncio

# Run async function
asyncio.run(async_function())
