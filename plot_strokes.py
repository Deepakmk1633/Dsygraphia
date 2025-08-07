import pandas as pd
import matplotlib.pyplot as plt

# Replace with your actual CSV filename
filename = 'write.csv'  # Change to your file

# Load the CSV data
df = pd.read_csv(filename)

# Filter movement events only
df_move = df[df['event'] == 'move'].copy()

# Plot handwriting stroke path
plt.figure(figsize=(12, 12))
plt.plot(df_move['x'], df_move['y'], color='blue')
plt.gca().invert_yaxis()  # Flip Y-axis for screen-like layout
plt.title("Handwriting Stroke Path")
plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.grid(True)
plt.show()
