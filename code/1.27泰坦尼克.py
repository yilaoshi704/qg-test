import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings('ignore')
# 汉化字体
import matplotlib

matplotlib.rc("font", family='DengXian')

train = pd.read_csv("train.csv")
# print(train.describe())
# train.info()
n = train['Survived'].value_counts()
# print(n)

# 总生还率
plt.figure(num='总生还率', figsize=(6, 6))
plt.pie(n, autopct='%.2f%%', labels=['死亡', '存活'], pctdistance=0.4, labeldistance=0.6,
        shadow=True, explode=[0, 0.1], textprops=dict(size=15))
plt.title('总生还率', fontdict={'fontsize': 25})
# plt.text(0.5, 1.0, '总体生还率')

# 不同性别生还率
sex_count = train.groupby(by='Sex')['Survived'].value_counts()
plt.figure(num='不同性别生还率', figsize=(2 * 5, 5))
ax_sex1 = plt.subplot(1, 2, 1)
ax_sex1.pie(sex_count.loc['female'][::-1], autopct='%.2f%%', labels=['死亡', '存活'], pctdistance=0.4,
            labeldistance=0.6,
            shadow=True, explode=[0, 0.1], textprops=dict(size=15), colors=['red', 'green'], startangle=90)
ax_sex1.set_title('女性生还率', fontdict={'fontsize': 25})
ax_sex2 = plt.subplot(1, 2, 2)
ax_sex2.pie(sex_count.loc['male'], autopct='%.2f%%', labels=['死亡', '存活'], pctdistance=0.4, labeldistance=0.6,
            shadow=True, explode=[0, 0.1], textprops=dict(size=15), colors=['red', 'green'])
ax_sex2.set_title('男性生还率', fontdict={'fontsize': 25})

# 不同年龄段生还率,直方图
age_range = train['Age']
print('船上年龄范围从最小到最大', age_range.min(), age_range.max())
age_num, _ = np.histogram(age_range, range=[0, 80], bins=16)  # 下划线忽略另一个返回值
age_survived = []
for age in range(5, 81, 5):
    survived_num = train.loc[(age_range >= age - 5) & (age_range <= age)]['Survived'].sum()
    age_survived.append(survived_num)
# 绘制条形图
plt.figure(num='不同年龄段生还率', figsize=(12, 6))
plt.bar(np.arange(2, 78, 5) + 0.5, age_num, width=5, label='总人数', alpha=0.8)
plt.bar(np.arange(2, 78, 5) + 0.5, age_survived, width=5, label='生还人数')
plt.xticks(range(0, 81, 5))
plt.yticks(range(0, 121, 10))
plt.xlabel('年龄', position=(0.95, 0), fontsize=15)
plt.ylabel('人数', position=(0, 0.95), fontsize=15)
plt.title('各年龄阶段人数和生还人数条形图', fontsize=25)
plt.grid(True, linestyle=':', alpha=0.6)

# 不同船舱等级乘客生还率
pc = train.groupby(by='Pclass')['Survived'].value_counts()
plt.figure(num='不同船舱等级乘客生还率', figsize=(3 * 5, 5))

ax_pc1 = plt.subplot(1, 3, 1)
ax_pc1.pie(pc.loc[1][::-1], autopct='%.2f%%', labels=['死亡', '存活'], pctdistance=0.4, labeldistance=0.6,
           shadow=True, explode=[0, 0.1], textprops=dict(size=15), colors=['red', 'green'], startangle=45)
ax_pc1.set_title('一等舱乘客生还率', fontsize=15)

ax_pc2 = plt.subplot(1, 3, 2)
ax_pc2.pie(pc.loc[2], autopct='%.2f%%', labels=['死亡', '存活'], pctdistance=0.4, labeldistance=0.6,
           shadow=True, explode=[0, 0.1], textprops=dict(size=15), colors=['red', 'green'], )
ax_pc2.set_title('二等舱乘客生还率', fontsize=15)

ax_pc3 = plt.subplot(1, 3, 3)
ax_pc3.pie(pc.loc[3], autopct='%.2f%%', labels=['死亡', '存活'], pctdistance=0.4, labeldistance=0.6,
           shadow=True, explode=[0, 0.1], textprops=dict(size=15), colors=['red', 'green'], )
ax_pc3.set_title('三等舱乘客生还率', fontsize=15)

# 不同码头
dock_count = train.groupby(by='Embarked')['Survived'].value_counts()
plt.figure(figsize=(3 * 5, 5))

ax_dock1 = plt.subplot(1, 3, 1)
ax_dock1.pie(dock_count.loc['C'][::-1], autopct='%.2f%%', labels=['死亡', '存活'], pctdistance=0.4, labeldistance=0.6,
             shadow=True, explode=[0, 0.1], textprops=dict(size=15), colors=['red', 'green'], startangle=45)
ax_dock1.set_title('法国瑟堡市乘客生还率', fontsize=15)

ax_dock2 = plt.subplot(1, 3, 2)
ax_dock2.pie(dock_count.loc['Q'], autopct='%.2f%%', labels=['死亡', '存活'], pctdistance=0.4, labeldistance=0.6,
             shadow=True, explode=[0, 0.1], textprops=dict(size=15), colors=['red', 'green'])
ax_dock2.set_title('爱尔兰昆士敦乘客生还率', fontsize=15)

ax_dock3 = plt.subplot(1, 3, 3)
ax_dock3.pie(dock_count.loc['S'], autopct='%.2f%%', labels=['死亡', '存活'], pctdistance=0.4, labeldistance=0.6,
             shadow=True, explode=[0, 0.1], textprops=dict(size=15), colors=['red', 'green'])
ax_dock3.set_title('英国南安普顿乘客生还率', fontsize=15)

# 不同登入港口乘客的船舱分布情况情况
dock_pclass = train.groupby(by='Embarked')['Pclass'].value_counts()
plt.figure(figsize=(3 * 5, 5))

ax_dock3 = plt.subplot(1, 3, 1)
ax_dock3.pie(dock_pclass.loc['C'], autopct='%.2f%%', labels=['一等舱', '三等舱', '二等舱'], pctdistance=0.4,
             labeldistance=0.6,
             shadow=True, explode=[0, 0.1, 0.1], textprops=dict(size=15), colors=['#698B69', '#76EE00', '#76EEC6'])
ax_dock3.set_title('法国瑟堡市乘客生还率', fontsize=15)

ax_dock4 = plt.subplot(1, 3, 2)
ax_dock4.pie(dock_pclass.loc['Q'], autopct='%.2f%%', labels=['三等舱', '二等舱', '一等舱'], pctdistance=0.4,
             labeldistance=0.6,
             shadow=True, explode=[0, 0.1, 0.1], textprops=dict(size=10), colors=['#698B69', '#76EE00', '#76EEC6'],
             startangle=10)
ax_dock4.set_title('爱尔兰昆士敦乘客生还率', fontsize=15)

ax_dock5 = plt.subplot(1, 3, 3)
ax_dock5.pie(dock_pclass.loc['S'], autopct='%.2f%%', labels=['三等舱', '二等舱', '一等舱'], pctdistance=0.4,
             labeldistance=0.6,
             shadow=True, explode=[0, 0.1, 0.1], textprops=dict(size=15), colors=['#698B69', '#76EE00', '#76EEC6'],
             startangle=180)
ax_dock5.set_title('英国南安普顿乘客生还率', fontsize=15)

# 不同票价乘客生还率
fare_range = train['Fare']
print('票价从最小到最大', fare_range.min(), fare_range.max())
fare_num, _ = np.histogram(fare_range, range=[0, 520], bins=16)  # 下划线忽略另一个返回值
fare_survived = []
for fare in range(32, 520, 32):
    survived_num = train.loc[(fare_range >= fare - 32.5) & (fare_range <= fare)]['Survived'].sum()
    fare_survived.append(survived_num)
# 绘制条形图
plt.figure(num='不同票价生还率', figsize=(12, 6))
plt.bar(np.arange(0, 520, 32.5) + 0.5, fare_num, width=32.5, label='总人数', alpha=0.8, edgecolor='black')
plt.bar(np.arange(0, 520, 32.5) + 0.5, fare_survived, width=32.5, label='生还人数', edgecolor='black')
plt.xticks(range(0, 520, 65))
plt.yticks(range(0, 800, 200))
plt.xlabel('票价', position=(0.95, 0), fontsize=15)
plt.ylabel('人数', position=(0, 0.95), fontsize=15)
plt.title('各年龄阶段人数和生还人数条形图', fontsize=25)
plt.grid(True, linestyle=':', alpha=0.6)
plt.show()
