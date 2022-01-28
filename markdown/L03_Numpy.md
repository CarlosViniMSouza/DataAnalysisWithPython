# Numerical Computing with Python and Numpy

![img1](https://i.imgur.com/mg8O3kd.png)

### Part 6 of "Data Analysis with Python: Zero to Pandas"


This tutorial series is a beginner-friendly introduction to programming and data analysis using the Python programming language. These tutorials take a practical and coding-focused approach. The best way to learn the material is to execute the code and experiment with it yourself. Check out the full series here: 

1. [First Steps with Python and Jupyter](https://jovian.ai/aakashns/first-steps-with-python)
2. [A Quick Tour of Variables and Data Types](https://jovian.ai/aakashns/python-variables-and-data-types)
3. [Branching using Conditional Statements and Loops](https://jovian.ai/aakashns/python-branching-and-loops)
4. [Writing Reusable Code Using Functions](https://jovian.ai/aakashns/python-functions-and-scope)
5. [Reading from and Writing to Files](https://jovian.ai/aakashns/python-os-and-filesystem)
6. [Numerical Computing with Python and Numpy](https://jovian.ai/aakashns/python-numerical-computing-with-numpy)
7. [Analyzing Tabular Data using Pandas](https://jovian.ai/aakashns/python-pandas-data-analysis)
8. [Data Visualization using Matplotlib & Seaborn](https://jovian.ai/aakashns/python-matplotlib-data-visualization)
9. [Exploratory Data Analysis - A Case Study](https://jovian.ai/aakashns/python-eda-stackoverflow-survey)

This tutorial covers the following topics:

- Working with numerical data in Python
- Going from Python lists to Numpy arrays
- Multi-dimensional Numpy arrays and their benefits
- Array operations, broadcasting, indexing, and slicing
- Working with CSV data files using Numpy

## Working with numerical data

The "data" in *Data Analysis* typically refers to numerical data, e.g., stock prices, sales figures, sensor measurements, sports scores, database tables, etc. The [Numpy](https://numpy.org) library provides specialized data structures, functions, and other tools for numerical computing in Python. Let's work through an example to see why & how to use Numpy for working with numerical data.


> Suppose we want to use climate data like the temperature, rainfall, and humidity to determine if a region is well suited for growing apples. A simple approach for doing this would be to formulate the relationship between the annual yield of apples (tons per hectare) and the climatic conditions like the average temperature (in degrees Fahrenheit), rainfall (in  millimeters) & average relative humidity (in percentage) as a linear equation.
>
> `yield_of_apples = w1 * temperature + w2 * rainfall + w3 * humidity`

Based on some statical analysis of historical data, we might come up with reasonable values for the weights `w1`, `w2`, and `w3`. Here's an example set of values:

```python
w1, w2, w3 = 0.3, 0.2, 0.5
```

Given some climate data for a region, we can now predict the yield of apples. Here's some sample data:

<img src="https://i.imgur.com/TXPBiqv.png" style="width:360px;"></img>

To begin, we can define some variables to record climate data for a region.

```python
kanto_temp = 73
kanto_rainfall = 67
kanto_humidity = 43
```

We can now substitute these variables into the linear equation to predict the yield of apples.

```python
kanto_yield_apples = kanto_temp * w1 + kanto_rainfall * w2 + kanto_humidity * w3
kanto_yield_apples
```

```python
# To make it slightly easier to perform the above computation for multiple regions, 
# we can represent the climate data for each region as a vector, i.e., a list of numbers.

kanto = [73, 67, 43]
johto = [91, 88, 64]
hoenn = [87, 134, 58]
sinnoh = [102, 43, 37]
unova = [69, 96, 70]
```

The three numbers in each vector represent the temperature, rainfall, and humidity data, respectively. 

We can also represent the set of weights used in the formula as a vector.

```python
weights = [w1, w2, w3]
```

We can now write a function `crop_yield` to calcuate the yield of apples (or any other crop) given the climate data and the respective weights.

The three numbers in each vector represent the temperature, rainfall, and humidity data, respectively. 

We can also represent the set of weights used in the formula as a vector.

```python
weights = [w1, w2, w3]
```

We can now write a function `crop_yield` to calcuate the yield of apples (or any other crop) given the climate data and the respective weights.

```python
def crop_yield(region, weights):
    result = 0
    for x, w in zip(region, weights):
        result += x * w
    return result
```

## Going from Python lists to Numpy arrays


The calculation performed by the `crop_yield` (element-wise multiplication of two vectors and taking a sum of the results) is also called the dot product. Learn more about dot product here: https://www.khanacademy.org/math/linear-algebra/vectors-and-spaces/dot-cross-products/v/vector-dot-product-and-vector-length

The Numpy library provides a built-in function to compute the dot product of two vectors. However, we must first convert the lists into Numpy arrays.

Let's install the Numpy library using the `pip` package manager.

```jupyter
!pip install numpy --upgrade --quiet
```

Next, let's import the `numpy` module. It's common practice to import numpy with the alias `np`.

```python
import numpy as np
```

We can now use the `np.array` function to create Numpy arrays.

```python
kanto = np.array([73, 67, 43])
kanto
# Output: array([73, 67, 43])
```
```python
weights = np.array([w1, w2, w3])
weights
# Output: array([0.3, 0.2, 0.5])
```

Numpy arrays have the type `ndarray`.

```python
type(kanto)
# Output: numpy.ndarray
```

```python
type(weights)
# Output: numpy.ndarray
```

Just like lists, Numpy arrays support the indexing notation `[]`.

```python
weights[0]
# Output: 0.3
```

```python
kanto[2]
# Output: 43
```

## Operating on Numpy arrays


We can now compute the dot product of the two vectors using the `np.dot` function.

```python
np.dot(kanto, weights)
# Output: 56.8
```

We can achieve the same result with low-level operations supported by Numpy arrays: performing an element-wise multiplication and calculating the resulting numbers' sum.

```python
(kanto * weights).sum()
# Output: 56.8
```

The `*` operator performs an element-wise multiplication of two arrays if they have the same size.

```python
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr1 * arr2
# Output: array([ 4, 10, 18])
```

```python
arr2.sum()
# Output: 15
```

## Benefits of using Numpy arrays

Numpy arrays offer the following benefits over Python lists for operating on numerical data:

> ° **Ease of use**: You can write small, concise, and intuitive mathematical expressions like `(kanto * weights).sum()` rather than using loops & custom functions like `crop_yield`.

> ° **Performance**: Numpy operations and functions are implemented internally in C++, which makes them much faster than using Python statements & loops that are interpreted at runtime
Here's a comparison of dot products performed using Python loops vs. Numpy arrays on two vectors with a million elements each.

```python
# Python lists
arr1 = list(range(1000))
arr2 = list(range(1000, 2000))

# Numpy arrays
arr1_np = np.array(arr1)
arr2_np = np.array(arr2)
```

```python
%%time
result = 0
for x1, x2 in zip(arr1, arr2):
    result += x1*x2
result

"""
Output:

CPU times: total: 0 ns
Wall time: 0 ns
832333500
"""
```

```python
%%time
np.dot(arr1_np, arr2_np)

"""
Output:

CPU times: total: 0 ns
Wall time: 21.8 ms
832333500
"""
```

As you can see, using np.dot is 100 times faster than using a for loop. This makes Numpy especially useful while working with really large datasets with tens of thousands or millions of data points.

## Multi-dimensional Numpy arrays
We can now go one step further and represent the climate data for all the regions using a single 2-dimensional Numpy array.

```python
climate_data = np.array([[73, 67, 43],
                         [91, 88, 64],
                         [87, 134, 58],
                         [102, 43, 37],
                         [69, 96, 70]])
climate_data

"""
Output:

array([[ 73,  67,  43],
       [ 91,  88,  64],
       [ 87, 134,  58],
       [102,  43,  37],
       [ 69,  96,  70]])
"""
```

If you've taken a linear algebra class in high school, you may recognize the above 2-d array as a matrix with five rows and three columns. Each row represents one region, and the columns represent temperature, rainfall, and humidity, respectively.

Numpy arrays can have any number of dimensions and different lengths along each dimension. We can inspect the length along each dimension using the `.shape` property of an array.

<img src="https://fgnt.github.io/python_crashkurs_doc/_images/numpy_array_t.png" width="420"></img>

```python
# 2D array (matrix)
climate_data.shape
# Output: (5, 3)
```

```python
weights.shape
# Output: array([0.3, 0.2, 0.5])
```

```python
# 1D array (vector)
weights.shape
# Output: (3,)
```

```python
# 3D array 
arr3 = np.array([
    [[11, 12, 13], 
     [13, 14, 15]], 
    [[15, 16, 17], 
     [17, 18, 19.5]]])

arr3.shape
# Output: (2, 2, 3)
```

All the elements in a numpy array have the same data type. You can check the data type of an array using the `.dtype` property.

```python
weights.dtype
# Output: dtype('float64')
```

```python
climate_data.dtype
# Output: dtype('int64')
```
If an array contains even a single floating point number, all the other elements are also converted to floats.

```python
arr3.dtype
# Output: dtype('float64')
```

We can now compute the predicted yields of apples in all the regions, using a single matrix multiplication between `climate_data` (a 5x3 matrix) and `weights` (a vector of length 3). Here's what it looks like visually:

<img src="https://i.imgur.com/LJ2WKSI.png" width="240"></img>

You can learn about matrices and matrix multiplication by watching the first 3-4 videos of this playlist: https://www.youtube.com/watch?v=xyAuNHPsq-g&list=PLFD0EB975BA0CC1E0&index=1 .

We can use the `np.matmul` function or the `@` operator to perform matrix multiplication.

```python
np.matmul(climate_data, weights)
# Output: array([56.8, 76.9, 81.9, 57.7, 74.9])
```

```python
climate_data @ weights
# Output: array([56.8, 76.9, 81.9, 57.7, 74.9])
```

## Working with CSV data files

Numpy also provides helper functions reading from & writing to files. Let's download a file `climate.txt`, which contains 10,000 climate measurements (temperature, rainfall & humidity) in the following format:


```
temperature,rainfall,humidity
25.00,76.00,99.00
39.00,65.00,70.00
59.00,45.00,77.00
84.00,63.00,38.00
66.00,50.00,52.00
41.00,94.00,77.00
91.00,57.00,96.00
49.00,96.00,99.00
67.00,20.00,28.00
...
```

This format of storing data is known as *comma-separated values* or CSV. 

> **CSVs**: A comma-separated values (CSV) file is a delimited text file that uses a comma to separate values. Each line of the file is a data record. Each record consists of one or more fields, separated by commas.

To read this file into a numpy array, we can use the `genfromtxt` function.

```python
import urllib.request

urllib.request.urlretrieve(
    'https://gist.github.com/BirajCoder/a4ffcb76fd6fb221d76ac2ee2b8584e9/raw/4054f90adfd361b7aa4255e99c2e874664094cea/climate.csv', 
    'climate.txt')

# Output: ('climate.txt', <http.client.HTTPMessage at 0x1acd496b1f0>)
```

```python
climate_data = np.genfromtxt('climate.txt', delimiter=',', skip_header=1)

climate_data

"""
Output:
array([[25., 76., 99.],
       [39., 65., 70.],
       [59., 45., 77.],
       ...,
       [99., 62., 58.],
       [70., 71., 91.],
       [92., 39., 76.]])
"""
```

```python
climate_data.shape
# Output: (10000, 3)
```

We can now perform a matrix multiplication using the `@` operator to predict the yield of apples for the entire dataset using a given set of weights.

```python
weights = np.array([0.3, 0.2, 0.5])
yields = climate_data @ weights
yields

# Output: array([72.2, 59.7, 65.2, ..., 71.1, 80.7, 73.4])
```

```python
yields.shape
# Output: (10000,)
```

Let's add the `yields` to `climate_data` as a fourth column using the `np.concatenate` function.

```python
climate_results = np.concatenate((climate_data, yields.reshape(10000, 1)), axis=1)

climate_results

"""
Output:

array([[25. , 76. , 99. , 72.2],
       [39. , 65. , 70. , 59.7],
       [59. , 45. , 77. , 65.2],
       ...,
       [99. , 62. , 58. , 71.1],
       [70. , 71. , 91. , 80.7],
       [92. , 39. , 76. , 73.4]])
"""
```

There are a couple of subtleties here:

* Since we wish to add new columns, we pass the argument `axis=1` to `np.concatenate`. The `axis` argument specifies the dimension for concatenation.

*  The arrays should have the same number of dimensions, and the same length along each except the dimension used for concatenation. We use the [`np.reshape`](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html) function to change the shape of `yields` from `(10000,)` to `(10000,1)`.

Here's a visual explanation of `np.concatenate` along `axis=1` (can you guess what `axis=0` results in?):

<img src="https://www.w3resource.com/w3r_images/python-numpy-image-exercise-58.png" width="300"></img>

The best way to understand what a Numpy function does is to experiment with it and read the documentation to learn about its arguments & return values. Use the cells below to experiment with `np.concatenate` and `np.reshape`.

Let's write the final results from our computation above back to a file using the `np.savetxt` function.

```python
climate_results

"""
Output:

array([[25. , 76. , 99. , 72.2],
       [39. , 65. , 70. , 59.7],
       [59. , 45. , 77. , 65.2],
       ...,
       [99. , 62. , 58. , 71.1],
       [70. , 71. , 91. , 80.7],
       [92. , 39. , 76. , 73.4]])
"""
```

```python
np.savetxt('climate_results.txt', 
           climate_results, 
           fmt='%.2f', 
           delimiter=',',
           header='temperature,rainfall,humidity,yeild_apples', 
           comments='')
```

The results are written back in the CSV format to the file `climate_results.txt`. 

```
temperature,rainfall,humidity,yeild_apples
25.00,76.00,99.00,72.20
39.00,65.00,70.00,59.70
59.00,45.00,77.00,65.20
84.00,63.00,38.00,56.80
...
```

Numpy provides hundreds of functions for performing operations on arrays. Here are some commonly used functions:


* Mathematics: `np.sum`, `np.exp`, `np.round`, arithemtic operators 
* Array manipulation: `np.reshape`, `np.stack`, `np.concatenate`, `np.split`
* Linear Algebra: `np.matmul`, `np.dot`, `np.transpose`, `np.eigvals`
* Statistics: `np.mean`, `np.median`, `np.std`, `np.max`
 

You can find a full list of array functions here: https://numpy.org/doc/stable/reference/routines.html