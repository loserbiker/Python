import copy
a = [[1]]
b = a.copy()

#a[0] += [5]
# İç değişim (in-place)

a[0] = a[0] + [5]
# Yeni obje üretir (referans değişimi)

print(a)

