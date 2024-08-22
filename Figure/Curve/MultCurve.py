import matplotlib.pyplot as plt
from matplotlib.sankey import Sankey

Sankey(flows=[0.25, 0.15, -0.10, -0.30], labels=['输入1', '输入2', '输出1', '输出2'], orientations=[-1, 1, 1, -1]).finish()
plt.title('基本桑基图')
plt.show()