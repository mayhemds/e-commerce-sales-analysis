import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Data set

file_path = "../../Datasets/real_world_datasets/ecommerce_sales.xlsx"

# Read the file 
df = pd.read(file_path) 

# View the first 5 rows
df.head()
