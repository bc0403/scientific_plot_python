import matplotlib.pyplot as plt

# # Setting the default font to Helvetica
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Helvetica', 'Arial', 'sans-serif']


# Get the current settings
print("Default font size:", plt.rcParams['font.size'])
print("Default legend font size:", plt.rcParams['legend.fontsize'])

# Example plot to see the changes
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 4, 9], label='Test Line')
ax.set_title("Example Plot")
ax.set_xlabel("X Label")
ax.set_ylabel("Y Label")
ax.legend()

plt.show()
