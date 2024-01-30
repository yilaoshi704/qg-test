import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import warnings
import matplotlib

warnings.filterwarnings('ignore')

# 汉化字体
matplotlib.rc("font", family='DengXian')

# 导入数据
vg= pd.read_csv("Video_Games_Sales_as_at_22_Dec_2016.csv")
# print(vg.head())

# 去重
vg.drop_duplicates(subset=["Name", "Platform"], inplace=True)

# 数据清洗
vg.dropna(subset=['Name'],inplace=True)
vg['User_Score'].fillna(0, inplace=True)

# 每年发行量
# print(vg['Year_of_Release'].min(), vg['Year_of_Release'].max())
x1 = vg.groupby('Year_of_Release').size()  # 计算每个年份的数量
print('最多年份为', x1.idxmax(), '数量为', x1.max())
plt.figure(num='每年发行量', figsize=(15, 12))
plt.plot(x1.index, x1.values, color='blue', linewidth=1.5)
# 添加标题和标签
plt.title('每年发行量', fontsize=30)
plt.xlabel('年份', fontsize=20)
plt.ylabel('数量', fontsize=20)
# 设置 x 轴的刻度为整数
plt.xticks(x1.index, rotation=90, fontsize=15)


# 不同平台占比
x2 = vg.groupby('Platform').size()  # 计算每个平台的数量
print('最多的平台为', x2.idxmax(), '数量为', x2.max())
plt.figure(num='平台总游戏数量', figsize=(15, 12))
plt.bar(x2.index, x2.values, width=0.8, color='skyblue')
# 添加标题和标签
plt.title('平台总游戏数量', fontsize=30)
plt.xlabel('平台', fontsize=20)
plt.ylabel('数量', fontsize=20)
# 设置 x 轴标签旋转角度
plt.xticks(rotation=0, ha='right', fontsize=10)

# 2010年
game_data_2010 = vg[vg['Year_of_Release'] == 2010]  # 获取2010年的游戏发行数据
platform_sales = game_data_2010.groupby('Platform')['Global_Sales'].sum()  # 计算每个平台的总销售额
best_platform = platform_sales.idxmax()  # 找到销售额最高的平台
sales = platform_sales.max()  # 最高销售额
print(best_platform, sales)
plt.figure(figsize=(12, 6))
plt.bar(platform_sales.index, platform_sales.values, color='skyblue')
plt.title('2010年不同平台游戏销售量', fontsize=15)
plt.xlabel('平台', fontsize=12)
plt.ylabel('游戏销售量', fontsize=12)
plt.xticks(rotation=45)

# 显示图形
plt.show()
