import pandas as pd
import matplotlib.pyplot as plt

# Load the data from CSV
data = pd.read_csv('simulation_data.csv')

# Create a line plot
plt.figure(figsize=(10, 5))
plt.plot(data['Tick'], data['DCacheMissRate'], label='D-Cache Miss Rate', marker='o')
plt.plot(data['Tick'], data['ICacheMissRate'], label='I-Cache Miss Rate', marker='o')
plt.title('Cache Miss Rates Over Simulation Time')
plt.xlabel('Simulation Time (Ticks)')
plt.ylabel('Miss Rate')
plt.legend()
plt.grid(True)
plt.savefig('CacheMissRates.png')  # Save the plot as a PNG file
plt.show()
