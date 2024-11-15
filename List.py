# a = ['a','b','c',30]
# print(a)
#
# print(f"a[1]={a[-2]}")
# print(f"a[0]={a[0]}")
# print(f"a[3]={a[-1]}")



a = [1,2,3,4,5,6,7,8,9,10]
for i in a:
    print(i)

print(f"a[3:6]={a[3:6]}")
print(f"a[0:6]={a[0:6]}")
print(f"a[6:]={a[6:]}")
print(f"a[1:6]={a[1:6]}")

a[1] = 30
print(a)

a.insert(8,90)
print(a)

