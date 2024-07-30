import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


# Replace your file path
file_path = 'test.xlsx'

# Load the Excel file
data = pd.read_excel(file_path, sheet_name='Sheet1')

# Drop rows with NaN values to clean the data
data = data.dropna()

data['time'] = pd.to_timedelta(data['time'].astype(str))

print(data['time'])

# Size of the figure, change the value to for different fig size
plt.figure(figsize=(12, 8))

# The data has time, colum and ph and bank columns
for column in data.columns[1:]:  #start the y-axis from the second colum, and keep the time x-axis
    plt.plot(data['time'], data[column], label=column)
    
# x-axis label name
plt.xlabel('Time - 30 Seconds Interval')

# x-axis lable direction
plt.xticks(rotation=90)

# y-axis lable name
plt.ylabel('PH Value Over time')

# figure title
plt.title('PH Change')

# Position of the legends
plt.legend(bbox_to_anchor=(1, .5), loc='upper left')

# Figure grid, make it False to remove grid
plt.grid(True)

# Display the fig
plt.show()
