import pandas as pd 
import matplotlib.pyplot as plt
import sys

path = 'data/'
path += sys.argv[1]
path += '.csv'

df = pd.read_csv(path)

print(df['eda'])
df = df[df['eda'] > 1]
plt.plot(df['eda'])

plt.show()