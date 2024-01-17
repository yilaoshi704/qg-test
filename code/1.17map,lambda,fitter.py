def multiply(x, y):
    return x * y


a = [1, 4, 6]
b = [2, 3, 5]
result = map(multiply, a, b)
print(*result)
print(*map(lambda x, y: x * y, a, b))

from scipy import stats
import numpy as np
# N(0,2)+N(0,10)
data1 = list(stats.norm.rvs(loc=0, scale=2, size=70000))
data2 = list(stats.norm.rvs(loc=0, scale=20, size=30000))
data=np.array(data1+data2)
from fitter import Fitter
f = Fitter(data, distributions=['norm', 't', 'laplace'])
f.fit()
f.summary()
