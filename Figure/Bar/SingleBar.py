import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

rcParams['font.family'] = 'serif'
rcParams['font.serif'] = ['Times New Roman']
def drawSglBar(categories, data):
    
    colors = ['#F65F5F', '#FF9C66', '#F97578', '#D25A8A', '#9B4D93', 
            '#006AAD', '#007EB0', '#0097BA', '#00B0BA', '#00C7B2', 
            '#48DDA5']
    # colors = ['#1E466E', '#528FAD', '#FFE6B7', '#E76254']

    # Create a vertical bar chart
    plt.bar(categories, data[0], color=colors, edgecolor='black', linewidth=1, width=0.5)
    for i in range(len(categories)):
        plt.text(i, data[0][i] + 0.05, f'{data[0][i]:.2f}', 
                 ha='center', va='bottom', fontsize=25)

    # Create title and labels
    plt.xlabel('Optimizers', fontsize = 30)
    plt.ylabel('Friedman-Rank', fontsize = 30)
    # plt.ylabel('FeatureError-Rank', fontsize = 30)

    plt.xticks(np.arange(len(categories)), categories, fontsize=20)
    plt.yticks(fontsize=20)
    # Hide the top and the right
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xlim(-0.5, len(categories) - 0.5)
    # Show the chart
    plt.show()

