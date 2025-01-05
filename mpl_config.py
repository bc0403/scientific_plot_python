# Created by Hao Jin on 2025/1/5.

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

def get_nature_palette():
    """
    Returns the Nature Reviews palette.
    """
    return [
        "#E64B35",  # Red
        "#4DBBD5",  # Blue
        "#00A087",  # Green
        "#3C5488",  # Dark Blue
        "#F39B7F",  # Orange
        "#8491B4",  # Light Grayish Blue
        "#91D1C2",  # Cyan
        "#DC0000",  # Bright Red
        "#7E6148",  # Brown
        "#B09C85"   # Beige
    ]

def get_generic_palette():
    """
    Returns the generic palette.
    """
    return [
        'black',
        'gray',
        'blue',
        'red',
        'green'
    ]

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

    # Check font availability and set fallback explicitly
    fonts = [f.name for f in font_manager.fontManager.ttflist]
    if 'Helvetica' in fonts:
        mpl.rcParams['font.sans-serif'] = ['Helvetica']
        print("Using Helvetica as the font.")
    elif 'Arial' in fonts:
        mpl.rcParams['font.sans-serif'] = ['Arial']
        print("Using Arial as a substitute for Helvetica.")
    else:
        mpl.rcParams['font.sans-serif'] = ['sans-serif']
        print("Neither Helvetica nor Arial available. Using a generic sans-serif font.")
    mpl.rcParams['font.family'] = 'sans-serif'

    # === Figure Size Settings ===
    # Determine figure width based on column type
    if column == 'single':
        width = 3.5  # Single column (in inches)
    elif column == 'double':
        width = 7.1  # Double column (in inches)
    else:
        raise ValueError("Column must be 'single' or 'double'.")
    height = width / 1.618  # Golden ratio for height
    mpl.rcParams['figure.figsize'] = [width, height]

    # Journal-specific settings
    if journal.lower() == 'nature':
        # Nature setting
        mpl.rcParams['font.size'] = 7
        mpl.rcParams['axes.labelsize'] = 7
        mpl.rcParams['xtick.labelsize'] = 7
        mpl.rcParams['ytick.labelsize'] = 7
        mpl.rcParams['legend.fontsize'] = 7
        mpl.rcParams['legend.frameon'] = False
        mpl.rcParams['axes.linewidth'] = 0.75
        mpl.rcParams['lines.linewidth'] = 1.0
        mpl.rcParams['axes.prop_cycle'] = mpl.cycler(color=get_nature_palette())
        mpl.rcParams['axes.spines.top'] = False
        mpl.rcParams['axes.spines.right'] = False
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
        mpl.rcParams['axes.prop_cycle'] = mpl.cycler(color=get_generic_palette())

    print(f"Figure size set to {width:.2f} x {height:.2f} inches for {journal} journal.")


# === Example Usage ===
if __name__ == "__main__":
    # Set parameters for Nature journal, single column
    set_mpl_params(journal='generic', column='single')

    # Example plot using the Nature palette
    x = range(10)
    fig, ax = plt.subplots()
    ax.plot(x, [xi**0.5 for xi in x], label="Power 0.5")
    ax.plot(x, [xi**1.0 for xi in x], label="Power 1.0")
    ax.plot(x, [xi**1.5 for xi in x], label="Power 1.5")
    ax.set_xlabel("X-Axis")
    ax.set_ylabel("Y-Axis")
    ax.legend(loc='upper left', frameon=False)  # Legend inside plot

    # Save the figure with high DPI and transparent background
    plt.savefig('./export/example_plot_nature.pdf', bbox_inches='tight', dpi=300, transparent=True)
    print("Figure saved as 'example_plot_nature.pdf'.")
