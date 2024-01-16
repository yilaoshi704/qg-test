a = dict(name="michael", age=18, height=170)
print(a.get('name'))
a['weight'] = 55
b = {'address': 'Shantou', 'num': 18}
a.update(b)
print(a)
a.pop('num')

p1 = {'age': 18, 'height': 170}
p2 = {'age': 10, 'height': 150}
p3 = {'age': 11, 'height': 148}
p = [p1, p2, p3]
for i in range(3):
    print(p[i].values())
