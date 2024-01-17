a = [1, "abc"]
b = [a, 'e']
a.append(b)
print("a + b = ", a)
a.extend(b)
print("a + b = ", a)
b.insert(0, 0)
print("0 + b = ", b)
b.remove(0)
print("b - 0 = ", b)
a.clear()
print("删除", a)
b.reverse()
print("倒转", b)
##推导式
c = [x * 2 for x in range(5) if x % 2 != 0]
print(c)
persons = ["小米", "华为", "oppo"]
for person in persons:
    print(person)
