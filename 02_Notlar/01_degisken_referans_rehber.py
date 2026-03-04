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
Birçok dilde değişken = kutu gibi anlatılır.

Python'da bu model YANLIŞTIR.

Python'da:

Değişken = bellekteki nesneye verilmiş isimdir.

Yani değişken nesnenin kendisi değildir.
Sadece nesneyi işaret eden bir etikettir.
"""

a = [1, 2]

"""
Bu satırın yaptığı şey:

1) Bellekte bir LIST nesnesi oluşturulur
2) a bu nesnenin referansını tutar

Görsel model:

a ----> [1,2]
"""

# ==========================================================
# 2) REFERANS NEDİR?
# ==========================================================

"""
Referans = aynı nesneyi işaret eden başka bir isim.
"""

b = a

"""
Yeni liste oluşmaz.

Bellek modeli:

a ----\
       ----> [1,2]
b ----/
"""

a.append(3)

"""
append in-place çalışır.
Yani aynı nesne değişir.

Sonuç:

a = [1,2,3]
b = [1,2,3]
"""

# ==========================================================
# 3) IMMUTABLE NEDİR?
# ==========================================================

"""
Immutable = değiştirilemeyen nesne.

Python immutable tipleri:

int
float
str
tuple
"""

x = 5
y = x

x += 2

"""
Burada ne olur?

5 nesnesi değişmez.

Yeni bir nesne oluşur.

Bellek modeli:

y ----> 5

x ----> 7
"""

# ==========================================================
# 4) MUTABLE NEDİR?
# ==========================================================

"""
Mutable = yerinde değiştirilebilen nesne.

Python mutable tipleri:

list
dict
set
"""

L = [1]
K = L

L.append(2)

"""
append in-place çalışır.

Sonuç:

L = [1,2]
K = [1,2]
"""

# ==========================================================
# 5) IN-PLACE NEDİR?
# ==========================================================

"""
In-place = aynı nesne üzerinde değişiklik yapmak.

Yeni nesne oluşturulmaz.
"""

A = [1]
A.append(2)

"""
Bellek:

A ----> [1,2]
"""

B = [1]
B = B + [2]

"""
Burada farklı bir durum var.

+ operatörü yeni bir liste üretir.

B artık yeni nesneyi gösterir.
"""

# ==========================================================
# 6) += vs +
# ==========================================================

"""
Listelerde önemli bir fark vardır.
"""

L1 = [1,2]
L2 = L1

L1 += [3]

"""
+= çoğu durumda in-place çalışır.

Sonuç:

L1 = [1,2,3]
L2 = [1,2,3]
"""

L3 = [1,2]
L4 = L3

L3 = L3 + [3]

"""
+ operatörü yeni nesne üretir.

Sonuç:

L3 = [1,2,3]
L4 = [1,2]
"""

# ==========================================================
# 7) SHALLOW COPY
# ==========================================================

"""
.copy() sadece dış listeyi kopyalar.

İç nesneler paylaşılır.
"""

X = [[1], [2]]
Y = X.copy()

"""
Bellek:

X ----> [list1, list2]
Y ----> [list1, list2]

İç listeler ortaktır.
"""

X[0].append(9)

"""
Sonuç:

X = [[1,9],[2]]
Y = [[1,9],[2]]
"""

# ==========================================================
# 8) REFERANS DEĞİŞTİRME
# ==========================================================

Y[0] = [5]

"""
Bu durumda:

Y'nin referansı değişir.

X etkilenmez.

Sonuç:

X = [[1,9],[2]]
Y = [[5],[2]]
"""

# ==========================================================
# 9) ÇOK ÖNEMLİ FARK
# ==========================================================

"""
a[0].append(9)

→ iç nesne değişir


a[0] = [9]

→ referans değişir
"""

# ==========================================================
# 10) ÖRNEK SORU
# ==========================================================

"""
a = [[1]]
b = a.copy()
a[0].append(2)

Sonuç:

a = [[1,2]]
b = [[1,2]]

Sebep:

İç liste ortaktır.
"""

# ==========================================================
# 11) GENEL ÖZET
# ==========================================================

"""
Python değişken modeli:

değişken = etiket
nesne = gerçek veri

Önemli kurallar:

- değişken kutu değildir
- referans aynı nesneyi gösterir
- mutable nesneler yerinde değişir
- immutable nesneler değişmez
- append in-place çalışır
- + yeni nesne üretir
- copy() shallow kopyadır
- reassignment referansı değiştirir
"""