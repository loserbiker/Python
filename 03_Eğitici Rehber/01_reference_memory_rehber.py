"""
BLOK 1 — PYTHON'DA REFERENCE VE BELLEK MANTIĞI
A'dan Z'ye öğretici rehber.
"""

# =========================================================
# BÖLÜM 1 — Python'da Değişken Nedir?
# =========================================================

# Python'da değişkenler değer tutmaz.
# Objeleri referans eder.

x = 5
y = x

# x ve y aynı int objesini gösterir.
# Ancak int immutable olduğu için değiştirilemez.


# =========================================================
# BÖLÜM 2 — Mutable ve Immutable
# =========================================================

"""
Immutable tipler:
- int
- float
- str
- tuple
- bool

Mutable tipler:
- list
- dict
- set
"""

# Immutable örnek
a = 10
b = a
a += 5

# Yeni obje oluşur.
# b değişmez.


# Mutable örnek
a = [1, 2, 3]
b = a
a.append(4)

# Aynı obje değiştiği için b de değişir.


# =========================================================
# BÖLÜM 3 — Shallow Copy
# =========================================================

"""
.copy() yalnızca dış listeyi kopyalar.
İç objeler ortak kalır.
"""

a = [[1], [2]]
b = a.copy()

a[0].append(99)

# İç liste ortak olduğu için b de etkilenir.


# =========================================================
# BÖLÜM 4 — Referans Değişimi vs İç Değişim
# =========================================================

# İç değişim:
a = [[1]]
b = a.copy()

a[0].append(5)
# Bu mevcut listeyi değiştirir.


# Referans değişimi:
a = [[1]]
b = a.copy()

a[0] = [5]
# Bu yeni liste oluşturur ve referansı değiştirir.


# =========================================================
# BÖLÜM 5 — Deep Copy
# =========================================================

"""
copy.deepcopy() tüm iç içe objeleri kopyalar.
Tam bağımsızlık sağlar.
"""

import copy

a = [[1], [2]]
b = copy.deepcopy(a)

a[0].append(99)

# b etkilenmez çünkü hiçbir obje ortak değildir.


# =========================================================
# ÖZET
# =========================================================

"""
=        → Referans ataması
.copy()  → Shallow copy (iç objeler ortak)
deepcopy → Tam bağımsız kopya

+= (list) → In-place değişim
+         → Yeni obje üretir
"""