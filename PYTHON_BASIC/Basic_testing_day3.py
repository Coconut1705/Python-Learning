print(9 + 6)
print("=======================================Arithmetic Operators=========================================")

a = 15 + 20
b = a + 80
c = b + a

print(a)
print(b)
print(c)

print("=======================================Comparison Operators=========================================")

x = 8
y = 12

print(x * y)
print(x >= y)
print(1 < x < 13)
print(2 < x and x > 7)
print(not(x > y))

print("=======================================Identity Operators=========================================")

n = ["Dell", "HP", "Asus"]
m = ["Acer", "MSI"]
z = m

print(m is n)
print(m is z)
print(m == n)
print(m == z)

print("=======================================Membership Operators=========================================")

cars = ["Ford", "Volvo", "BMW"]
if "Volvo" in cars:
    print("Có Volvo trong danh sách")
else:
    print("Không có Volvo trong danh sách")

if "Audi" not in cars:
    print("Không có Audi trong danh sách")
else:
    print("Có Audi trong danh sách")

text = "Con meo keu sao ?"
print("C" in text)
print("meo" in text)

print("=======================================Precedence of Operators======================================")

print((5 - 2) + ( 8 + 1)) # tính 5 - 2 trước, sau đó tính 8 + 1, cuối cùng cộng hai kết quả lại với nhau
print(95 + 24 * 2) # tính 24 * 2 trước, sau đó cộng với 95

print("=======================================Data Structures: List========================================")

list = ["Thang Ca", "Thang Dat", "Thang O"]
print(list)

list2 = ["Thang Ca", "Thang Dat", "Thang O", "Thang Ngu", "Thang Dat"]
print(list)
print(len(list))

list3 = ["XXX", 123, True, 45.67]
print(list3[1])

list4 = [list, list2, list3]
print(list4[-2])

list5 = ["con cho", "con meo", "con vit"]
print(type(list))
print(list2[1:3])

print("=======================================Modify Lists============================================")

listA = ["mot", "hai", "bon", "bon", "nam", "sau", "bay", "tam"]
listA[2] = "ba"
print(listA)
listA[2:6] = ["BA", "BON", "NAM"]
print(listA)
listA.insert(3, "BON BON")
print(listA)

print("=======================================Add Items to a List=======================================")

listB = ["iPhone", "Samsung", "Xiaomi", "Oppo"]
listB.append("Huawei")
print(listB)
listB.insert(2, "Realme")
print(listB)
listC = ["Canon", "Nikon"]
listB.extend(listC)
print(listB)

print("=======================================Remove Items from a List=================================")

listD = ["Red", "Blue", "Green", "Yellow", "Black"]
listD.remove("Green")
print(listD)
listD.pop(3)
print(listD)
listD.pop()
print(listD)

del listD[0]
print(listD)
del listD 
listE = ["Circle", "Square", "Triangle", "Rectangle"]
listE.clear()
print(listE)

print("=======================================Looping Through a List======================================")
listF = ["Java", "Python", "C++", "JavaScript"]
for x in listF:
    print(x)
for i in range(len(listF)):
    print(listF[i])