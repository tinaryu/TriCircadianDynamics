import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

# Only the files of interest
files = [
    "wtonly_meta2d_nr1d1_WT.txt",
    "wtonly_meta2d_nr1d1_KO.txt"
]

# Read data and extract AMP values
amplitudes = []
for file in files:
    df = pd.read_csv(file, sep='\t')  # assuming tab-separated values
    cleaned_amp = df['meta2d_rAMP'].dropna().tolist()
    if cleaned_amp:  # Check if list is not empty
        amplitudes.append(cleaned_amp)

# Calculate t-test significance between the two conditions
p_value = ttest_ind(amplitudes[0], amplitudes[1], equal_var=False).pvalue

# Plotting
plt.figure(figsize=(10, 8))  # Adjust the figure size if needed
# Set positions explicitly to control box width
positions = [1, 2]
boxes = plt.boxplot(amplitudes, positions=positions, widths=0.5, vert=True, patch_artist=True, showfliers=False)

# Apply colors
colors = ['red', 'blue']
for patch, color in zip(boxes['boxes'], colors):
    patch.set_facecolor(color)

# Labels
labels = ['WT', 'KO']
plt.xticks(positions, labels)
plt.ylabel('Amplitude (AMP)')
plt.title('Comparison of Amplitudes for WT and KO')

# Annotate significance on the plot
y_max = max([max(lst) for lst in amplitudes if lst])  # Safeguard against empty lists
y_pos = y_max + y_max * 0.05  # slightly above the highest data point
x_pos = sum(positions) / len(positions)  # in the middle of the two positions
p_text = f'p = {p_value:.2e}'  # Adjusted formatting for better legibility

plt.annotate(p_text, xy=(x_pos, y_pos), xytext=(x_pos, y_pos), ha='center', va='bottom')

# Adjust layout to fit everything
plt.subplots_adjust(left=0.15, right=0.85, top=0.85, bottom=0.15)

plt.savefig("nr1d1_WT_KO_boxplot.pdf", bbox_inches='tight')
plt.show()

print(f"P-value for t-test between WT and KO: {p_value:.2e}")  # More readable scientific notation

