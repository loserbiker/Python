"""
BLOK 1 — REFERENCE & MEMORY MANTIĞI
Temiz ve sade notlar.
"""

# =========================================================
# 1) Immutable vs Mutable
# =========================================================

# Immutable (değiştirilemez)
# int, float, str, tuple, bool

a = 5
b = a
a = 10

# b değişmez çünkü int immutable'dır.


# Mutable (değiştirilebilir)
# list, dict, set

a = [1, 2, 3]
b = a

a.append(4)

# b de değişir çünkü aynı objeyi gösterir.


# =========================================================
# 2) id() fonksiyonu
# =========================================================

a = [1, 2, 3]
b = a

print(id(a))
print(id(b))
# Aynı çıkar → aynı obje


# =========================================================
# 3) Shallow Copy
# =========================================================

a = [[1], [2]]
b = a.copy()

a[0].append(5)

# İç liste ortak olduğu için b de değişir.


# =========================================================
# 4) Referans Değişimi
# =========================================================

a = [[1]]
b = a.copy()

a[0] = [10]

# Bu referans değişimidir.
# İç obje değişmez.
# b etkilenmez.


# =========================================================
# 5) Deep Copy
# =========================================================

import copy

a = [[1], [2]]
b = copy.deepcopy(a)

a[0].append(99)

# Deepcopy sonrası hiçbir obje ortak değildir.
# b etkilenmez.


# =========================================================
# 6) += vs +
# =========================================================

a = [[1]]
b = a.copy()

a[0] += [5]
# İç değişim (in-place)

a[0] = a[0] + [5]
# Yeni obje üretir (referans değişimi)