import pandas as pd 
import matplotlib.pyplot as plt
import sys

final_data = []

name = 'Low, Medium, and High Load (Wet)'
xaxis = 'Time'
yaxis = 'Potential'

# df = pd.read_csv('data/Aman_Low_Dry.csv')

# print(df['eda'])
# df = df[df['eda'] > 1]
# # plt.plot(df['eda'])

# final_data += df['eda'].tolist()

# df = pd.read_csv('data/Aman_Medium_Dry.csv')

# print(df['eda'])
# df = df[df['eda'] > 1]
# # plt.plot(df['eda'])

# final_data += df['eda'].tolist()


df = pd.read_csv('data/catherine_low-mid-high_wet.csv')

print(df['eda'])
df = df[df['eda'] > 1]
# plt.plot(df['eda'])

final_data += df['eda'].tolist()

plt.plot(final_data)

plt.ylabel(yaxis)
plt.xlabel(xaxis)
plt.title(name)

plt.show()
