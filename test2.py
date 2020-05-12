
a = [1, 2, 5, 6, 10]

b = [1, 3, 7, 5, 5, 7, 8, 9, 2, 4, 3, 6, 5, 3, 2, 1, 9]

c = [1, 5, 5, 9, 2, 4, 6, 5, 3, 2, 1, 9]
print("Del the position should be like this one:", c) 

a.sort(reverse=True)
print("Sort the a", a)

for i in range(len(a)):
    del b[a[i]]

print("Output del use result:", b)