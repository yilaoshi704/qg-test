import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 50)
# y = [15, 13, 14, 17, 20, 25, 26, 26, 24, 22, 18, 15]
y = 2*x+1
plt.figure(1, figsize=(8, 6))
l1, = plt.plot(x, y, color='black', linewidth=1.5, linestyle='--')
plt.xlim((-3, 3))
plt.ylim((-2, 3))
plt.xlabel('x')
plt.ylabel('y')
new_ticks = np.linspace(-1, 2, 5)
# plt.xticks(new_ticks)
# plt.yticks([-2, 0, 2], [r'$bad$', 'not bad', 'good' ])

# gca = ‘get current axis’
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position(('data', -1))
ax.spines['left'].set_position(('data', 0))

# 图例
plt.legend(handles=[l1], labels=['aaa'], loc='best')

# 标点
x0 = 0.5
y0 = x0*2+1
plt.scatter(x0, y0, s=50, color='red')
plt.plot([x0, x0], [y0, -1], color='black')

# 标注1
plt.annotate(r'$Y=2X+1%s$' %y0, xy=(x0, y0), xycoords='data', xytext=(+30, -30),
             textcoords='offset points', fontsize=16,     arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2'))

# 标注2
plt.text(-3.7, 3, r'$Y=2X+1$', fontdict={'weight': 'bold', 'size': 16, 'color':'black'})

# ticks能见度
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(12)
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.7))

# 散点图
plt.figure(2, figsize=(8, 6))
n = 1024
x1 = np.random.normal(0, 1, n)
y1 = np.random.normal(0, 1, n)
t1 = np.arctan2(y1, x1)

# plt.xlim((-1.5, 1.5))
# plt.ylim((-1.5, 1.5))
# plt.scatter(x1, y1, s=50, c=t1, alpha=0.5)
plt.scatter(np.arange(5), np.arange(5))
plt.xlabel('x')
plt.ylabel('y')

# gca = ‘get current axis’
ax2 =plt.gca()
ax2.spines['right'].set_color('none')
ax2.spines['top'].set_color('none')
ax2.spines['bottom'].set_position(('data', 0))
ax2.spines['left'].set_position(('data', 0))

# 柱状图
plt.figure(3, figsize=(8, 6))
n2 = 12
x2 = np.arange(n2)
y2 = (1-x2/float(n2)) * np.random.uniform(0.5, 1.0, n2)

plt.bar(x2, +y2)
for x2, y2 in zip(x2, y2):
    # ha: horizontal alignment
    plt.text(x2-0.3, y2+0.05, r'$%.2f$' % y2, ha='center', va='bottom')

plt.xlim(-0.5, n2)
plt.ylim(-1.25, 1.25)
plt.xlabel('x')
plt.ylabel('y')
ax3 = plt.gca()
ax3.spines['right'].set_color('none')
ax3.spines['top'].set_color('none')
ax3.spines['bottom'].set_position(('data', 0))
ax3.spines['left'].set_position(('data', 0))
plt.show()
