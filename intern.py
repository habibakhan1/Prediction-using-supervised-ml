import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt  


url = "http://bit.ly/w-data"
s_data = pd.read_csv(url)
print("Data imported successfully")

s_data.head(10)