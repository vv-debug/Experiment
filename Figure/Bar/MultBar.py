import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['font.serif'] = ['Times New Roman']

def drawMultBar(categories, data, labels):
    # colors = ['#E76254', '#EF8A47', '#F7AA58', '#FFD06F', '#FFE6B7', 
    #         '#AADCE0', '#72BCD5', '#528FAD', '#376795', '#1E466E', 
    #         '#768FC6']
    colors = ['#1E466E', '#528FAD', '#FFE6B7', '#E76254']
    width = 0.2

    x = np.arange(len(categories))    # Position of the bar
    r = []
    for i in range(len(labels)):
        if i == 0:
            r.append(x)
        else:
            r.append([x + width for x in r[i - 1]])
    # r1 = x
    # r2 = [x + width for x in r1]
    # r3 = [x + width for x in r2]
    # r4 = [x + width for x in r3]
    for i in range(len(r)):
        plt.bar(r[i], data[i], width, label=labels[i], color=colors[i], edgecolor='black', linewidth=0.5)
    # # Draw the first data series
    # plt.bar(r1, data[0], width, label='10 Dim', color='#97001B', edgecolor='black', linewidth=0.5)
    # # Draw the second data series
    # plt.bar(r2, data[1], width, label='30 Dim', color='#F65F5F', edgecolor='black', linewidth=0.5)
    # # Draw the third data series
    # plt.bar(r3, data[2], width, label='50 Dim', color='#F687C1', edgecolor='black', linewidth=0.5)
    # # Draw the forth data series
    # plt.bar(r4, data[3], width, label='100 Dim', color='#BB528B', edgecolor='black', linewidth=0.5)

    # Add the title and the labels
    plt.xlabel('Algorithms', fontsize = 18)
    plt.ylabel('Friedman-rank', fontsize = 18)
    plt.xticks([r + width * 1.5 for r in range(len(categories))], categories)

    plt.legend(loc='best')

    # Hide the top and the right
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Show
    plt.tight_layout()
    plt.show()

