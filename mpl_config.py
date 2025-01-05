# Created by Hao Jin on 2025/1/5.

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import rc
import matplotlib.font_manager as font_manager

def set_mpl_params(journal='nature', column='single'):
    """
    Configure Matplotlib parameters for a specific journal and figure size.

    Parameters:
    - journal (str): Target journal ('nature', 'ieee', or 'generic').
    - column (str): Column width ('single' or 'double').
    """
    # === General Font Settings ===
    mpl.rcParams['pdf.fonttype'] = 42  # Use Type 42 (TrueType) fonts
    mpl.rcParams['ps.fonttype'] = 42
    mpl.rcParams['text.usetex'] = False  # Disable TeX for simplicity
    mpl.rcParams['font.sans-serif'] = ['Helvetica', 'Arial', 'sans-serif']
    mpl.rcParams['font.family'] = 'sans-serif'

    # Check font availability
    fonts = [f.name for f in font_manager.fontManager.ttflist]
    if 'Helvetica' in fonts:
        print("Helvetica is available and will be used as the font for figures.")
    elif 'Arial' in fonts:
        print("Helvetica is not available. Using Arial as a substitute.")
    else:
        print("Neither Helvetica nor Arial is available. Using a generic sans-serif font.")

    # === Figure Size Settings ===
    # Determine figure width based on column type
    if column == 'single':
        width = 3.5  # Single column (in inches)
    elif column == 'double':
        width = 7.1  # Double column (in inches)
    else:
        raise ValueError("Column must be 'single' or 'double'.")

    # Set height using golden ratio unless specified otherwise
    height = width / 1.618

    # Apply journal-specific settings
    if journal.lower() == 'nature':
        # Nature-specific settings
        mpl.rcParams['font.size'] = 7
        mpl.rcParams['axes.labelsize'] = 7
        mpl.rcParams['xtick.labelsize'] = 7
        mpl.rcParams['ytick.labelsize'] = 7
        mpl.rcParams['legend.fontsize'] = 7
        mpl.rcParams['legend.frameon'] = False  # Remove legend outline
        mpl.rcParams['axes.linewidth'] = 0.75  # Thinner axis lines for Nature
        mpl.rcParams['lines.linewidth'] = 1.0  # Data lines

        # Color palette
        mpl.rcParams['axes.prop_cycle'] = mpl.cycler(color=[
            'black', 'gray', 'blue', 'red', 'green'
        ])

    elif journal.lower() == 'ieee':
        # IEEE-specific settings
        mpl.rcParams['font.size'] = 8
        mpl.rcParams['axes.labelsize'] = 8
        mpl.rcParams['xtick.labelsize'] = 8
        mpl.rcParams['ytick.labelsize'] = 8
        mpl.rcParams['legend.fontsize'] = 8
        mpl.rcParams['legend.frameon'] = False  # Remove legend outline
        mpl.rcParams['axes.linewidth'] = 1.0  # Standard axis lines for IEEE
    else:
        # Generic settings
        mpl.rcParams['font.size'] = 9
        mpl.rcParams['axes.labelsize'] = 9
        mpl.rcParams['xtick.labelsize'] = 9
        mpl.rcParams['ytick.labelsize'] = 9
        mpl.rcParams['legend.fontsize'] = 9
        mpl.rcParams['legend.frameon'] = False  # Remove legend outline
        mpl.rcParams['axes.linewidth'] = 1.0  # Standard axis lines

    # Set default figure size
    mpl.rcParams['figure.figsize'] = [width, height]

    # Remove top and right spines for cleaner appearance
    mpl.rcParams['axes.spines.top'] = False
    mpl.rcParams['axes.spines.right'] = False

    print(f"Figure size set to {width:.2f} x {height:.2f} inches.")

# === Example Usage ===
if __name__ == "__main__":
    # Set parameters for Nature journal, single column
    set_mpl_params(journal='nature', column='single')

    # Example plot
    x = range(10)
    y1 = [xi**2 for xi in x]
    y2 = [xi**1.5 for xi in x]

    fig, ax = plt.subplots()
    ax.plot(x, y1, label='Quadratic', color='blue')
    ax.plot(x, y2, label='Power 1.5', color='red')
    ax.set_xlabel('X-Axis Label')
    ax.set_ylabel('Y-Axis Label')
    ax.legend(frameon=False)  # No legend frame
    fig.tight_layout()  # otherwise the right y-label is slightly clipped

    # Save the figure with embedded fonts
    plt.savefig('./export/example_plot_nature.pdf', bbox_inches='tight', dpi=300, transparent=True) # transparent for Adobe Illustrator.
    print("Figure saved as 'example_plot_nature.pdf'.")

