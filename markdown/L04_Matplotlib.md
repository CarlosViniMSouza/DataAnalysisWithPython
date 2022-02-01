# Data Visualization using Python, Matplotlib and Seaborn


![](https://i.imgur.com/9i806Rh.png)

### Part 8 of "Data Analysis with Python: Zero to Pandas"


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

- Creating and customizing line charts using Matplotlib
- Visualizing relationships between two or more variables using scatter plots
- Studying distributions of variables using histograms & bar charts to 
- Visualizing two-dimensional data using heatmaps
- Displaying images using Matplotlib's `plt.imshow`
- Plotting multiple Matplotlib and Seaborn charts in a grid

## Introduction

Data visualization is the graphic representation of data. It involves producing images that communicate relationships among the represented data to viewers. Visualizing data is an essential part of data analysis and machine learning. We'll use Python libraries [Matplotlib](https://matplotlib.org) and [Seaborn](https://seaborn.pydata.org) to learn and apply some popular data visualization techniques. We'll use the words _chart_, _plot_, and _graph_ interchangeably in this tutorial.

To begin, let's install and import the libraries. We'll use the `matplotlib.pyplot` module for basic plots like line & bar charts. It is often imported with the alias `plt`. We'll use the `seaborn` module for more advanced plots. It is commonly imported with the alias `sns`.

```jupyter
!pip install matplotlib seaborn --upgrade --quiet
```

```python
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
```

Notice this we also include the special command `%matplotlib inline` to ensure that our plots are shown and embedded within the Jupyter notebook itself. Without this command, sometimes plots may show up in pop-up windows.

