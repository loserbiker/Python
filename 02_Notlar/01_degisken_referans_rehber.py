"""
==========================================================
1 MART
DEĞİŞKEN - REFERANS - MUTABLE - IMMUTABLE
==========================================================

Bu dosya Python'un en kritik temelini anlatır.

Konular:
- Değişken nedir?
- Referans nedir?
- Mutable vs Immutable
- In-place nedir?
- += vs +
- Shallow copy
- append vs reassignment farkı
- Soru-cevap örnekleri

Bu konu oturmadan OOP TAM OTURMAZ.
"""

# ==========================================================
# 1) PYTHON'DA DEĞİŞKEN NEDİR?
# ==========================================================

"""
Python'da değişken bir kutu değildir.

Değişken = Bellekteki nesneye yapıştırılmış etikettir.

Örnek:
"""

a = [1, 2]

"""
Bu satırın yaptığı:

1) Bellekte bir liste nesnesi oluşturulur.
2) 'a' bu nesneyi işaret eder.

Yani:
a içine liste konmadı.
a bu listeyi gösteriyor.
"""

# ==========================================================
# 2) REFERANS NEDİR?
# ==========================================================

b = a

"""
Yeni liste oluşmadı.

a ve b aynı nesneyi gösteriyor.

a ----\
        ---> [1, 2]
b ----/
"""

a.append(3)

"""
append in-place çalışır.
Yeni liste oluşmaz.

a = [1, 2, 3]
b = [1, 2, 3]
"""

# ==========================================================
# 3) MUTABLE vs IMMUTABLE
# ==========================================================

"""
IMMUTABLE:
- int
- float
- str
- tuple

Immutable nesne değişmez.
Değiştirilmeye çalışılırsa yeni nesne oluşur.
"""

x = 5
y = x
x += 2

"""
5 değişmedi.
Yeni 7 nesnesi oluştu.

x = 7
y = 5
"""

"""
MUTABLE:
- list
- dict
- set

Yerinde değişir.
"""

L = [1]
K = L
L.append(2)

"""
L ve K aynı nesneyi gösterir.
İkisi de [1, 2] olur.
"""

# ==========================================================
# 4) IN-PLACE NEDİR?
# ==========================================================

"""
In-place = Aynı nesne üzerinde değişiklik yapmak.
"""

A = [1]
A.append(2)      # in-place

"""
Yeni liste oluşmaz.
"""

B = [1]
B = B + [2]      # yeni liste

"""
Yeni nesne oluşur.
"""

# ==========================================================
# 5) += vs +
# ==========================================================

L1 = [1, 2]
L2 = L1
L1 += [3]

"""
Listede += in-place çalışır.
"""

L3 = [1, 2]
L4 = L3
L3 = L3 + [3]

"""
+ yeni liste üretir.
"""

# ==========================================================
# 6) SHALLOW COPY
# ==========================================================

"""
.copy() sadece dış listeyi kopyalar.
İç listeler ortaktır.
"""

X = [[1], [2]]
Y = X.copy()

"""
Yeni dış liste oluştu.
İç listeler paylaşılıyor.
"""

X[0].append(9)

"""
Y de etkilenir.
"""

Y[0] = [5]

"""
Bu referans değişimidir.
X etkilenmez.
"""

# ==========================================================
# 7) SIK SORULAN KRİTİK FARKLAR
# ==========================================================

"""
a[0].append(9)
→ İç liste değişir.

a[0] = [9]
→ Referans değişir.

Bu fark shallow copy sorularının kalbidir.
"""

# ==========================================================
# 8) ÖRNEK SORU
# ==========================================================

"""
a = [[1]]
b = a.copy()
a[0].append(2)

Sonuç:
a = [[1,2]]
b = [[1,2]]

Çünkü iç liste ortaktı.
"""

# ==========================================================
# 9) GENEL ÖZET
# ==========================================================

"""
- Değişken = etiket
- Referans = aynı nesneyi gösteren isim
- append = in-place
- + = yeni nesne
- += listede in-place
- copy() shallow'dur
- reassignment referansı değiştirir

Bu temel %100 oturmadan ilerleme.
"""