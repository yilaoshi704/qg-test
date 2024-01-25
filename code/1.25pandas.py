import pandas as pd

# Series
data1 = [['apple', '8.5'], ['banana', '5'], ['orange', '5']]
s = pd.Series(data1)
print(s)
print(list(s.index))
# DataFrame
colunms = ['fruit', 'price']
d1 = pd.DataFrame(data1, columns=colunms)
print(d1)
data2 = {'fruit': ['apple', 'banana', 'orange'],
         'price': [8.5, 5, 5],
         'company': '翼老师'}
d2 = pd.DataFrame(data2)
print(d2)
# pd.set_option('display.unicode.east_asian_width', True)
# new_d2 = d2.T
# print(new_d2)
print(d2.loc[0])
# 抽取符合条件
print(d2.loc[(5 < d2['price']) & (9 >= d2['price'])])
# 添加删除修改
d2.drop('company', axis=1, inplace=True)
print(d2)
