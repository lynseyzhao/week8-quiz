import pandas as pd
import matplotlib.pyplot as plt

# Create a dictionary containing data
data = {
    'Year': [1950, 1960, 1970, 1980, 1990, 2000, 2010],
    'CO2': [250, 265, 272, 260, 300, 320, 389],
    'Temperature': [14.1, 15.5, 16.3, 18.1, 17.3, 19.1, 20.2]
}

# Create a pandas DataFrame using the dictionary
df = pd.DataFrame(data)

# Print the DataFrame
print(df)

# Initialize empty lists to store the data
years = []
co2 = []
temp = []

# Read data from the CSV file
data = pd.read_csv('climate.csv')

# Extract data into lists
years = data['Year'].tolist()
co2 = data['CO2'].tolist()
temp = data['Temperature'].tolist()

# Plot the data
plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--')
plt.title("Climate Data")
plt.ylabel("[CO2]")
plt.xlabel("Year (decade)")

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-')
plt.ylabel("Temp (C)")
plt.xlabel("Year (decade)")

plt.tight_layout()
plt.show()






