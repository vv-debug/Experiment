import matplotlib.pyplot as plt
from matplotlib.sankey import Sankey

# 创建一个Sankey实例
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(1, 1, 1, xticks=[], yticks=[], title="Simple Sankey Diagram")

# 初始化Sankey diagram
sankey = Sankey(ax=ax, scale=0.01, offset=0.2, head_angle=180,
                 format='%.0f%%', unit=None)

# 添加流
sankey.add(flows=[0.25, 0.15, 0.6], # 流量
           labels=['Source A', 'Source B', 'Source C'], # 源标签
           orientations=[0, 0, 1], # 流的方向，0从左到右，1从上到下
           pathlengths=[0.25, 0.25, 0.5], # 流的长度比例
           patchlabel='Total') # 汇总标签

# 绘制Sankey diagram
diagrams = sankey.finish()

plt.show()