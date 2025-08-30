import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"D:\Algoviz\1-datasets\housing.csv")
print(df)

dataset = pd.DataFrame(df)
print(dataset)

dataset.columns = df.columns.to_list()
print(dataset.head())

