import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv('data/final_data/2-1-01.csv')

print(df['eda'])
df = df[df['eda'] > 1]
plt.plot(df['eda'])

plt.show()