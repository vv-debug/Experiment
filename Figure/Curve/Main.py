import pandas as pd
import matplotlib.pyplot as plt


# 假设df是一个DataFrame，其中包含的列有'Year', 'Province', 'Rank'，
# 其中'Year'是年份，'Province'是省份，'Rank'是那一年的GDP排名

# 导入数据
# df = pd.read_csv('path_to_your_data.csv')

# 画图
def plot_gdp_rank_changes(df):
    plt.figure(figsize=(20, 10))

    provinces = df['Province'].unique()
    years = df['Year'].unique()

    for province in provinces:
        province_data = df[df['Province'] == province]
        plt.plot(province_data['Year'], province_data['Rank'], marker='o', label=province)

    plt.gca().invert_yaxis()  # 因为排名1是最高的，所以让y轴倒序

    plt.title('中国各省份GDP排名变化（1978-2021）')
    plt.xlabel('年份')
    plt.ylabel('GDP排名')
    plt.xticks(years, rotation=45)  # 如果年份太密集，可以考虑只显示部分年份或旋转标签
    plt.legend()
    plt.grid(True)
    plt.show()

# 替换这里的df为包含您数据的DataFrame
# plot_gdp_rank_changes(df)