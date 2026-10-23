# NumPy Practice

This folder contains my beginner-friendly NumPy practice programs as a BTech Artificial Intelligence and Machine Learning (AIML) student.

## 01. Array Creation and Multiplication

**File:** `01_array_creation.py`

### What I learned
- Importing NumPy using the alias `np`
- Creating a NumPy array with `np.array()`
- Multiplying every element of an array by a number
- Checking the type of a NumPy array

### Code example
```python
import numpy as np

array = np.array([1, 2, 3, 4, 5])
array = array * 3

print("Updated array:", array)
print("Data type:", type(array))
```

### Output
```text
Updated array: [ 3  6  9 12 15]
Data type: <class 'numpy.ndarray'>
```

### Key takeaway
NumPy performs element-wise operations on arrays. Multiplying an array by `3` multiplies each element by three.

## How to run
Install NumPy if needed:

```bash
python -m pip install numpy
```

Run the program from the repository root:

```bash
python numpy/01_array_creation.py
```

I'm building this folder step by step as I learn NumPy and other Python libraries for AIML.
