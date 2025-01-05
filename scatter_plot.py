import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_config import set_mpl_params # Import custom configuration

# Set Matplotlib parameters for Nature-style plots
set_mpl_params(journal='nature', column='single')

# === prepare data ===



# === plot data ===
fig, ax = plt.subplots()             # Create a figure containing a single Axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the Axes.


# Save the plot
output_path = './export/dummy_scatter_plot.pdf'
plt.tight_layout()
plt.savefig(output_path, bbox_inches='tight', dpi=300, transparent=True)
print(f"Scatter plot saved to '{output_path}'.")

# Show the plot interactively
plt.show()
