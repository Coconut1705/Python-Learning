y = 123

if type(y) == float:
    print("y là số thực")
else:
    print("y không phải số thực")

a = 4
b = 2.6
c = 7j

q = float(a)
w = int(b)
e = complex(a)

print("Giá trị chuyển đổi của a sang float là:", q)
print("Giá trị chuyển đổi của b sang int là:", w)
print("Giá trị chuyển đổi của a sang complex là:", e)

import random
print(random.randint(1, 100))

x = float("2")
print(x)