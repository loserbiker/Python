"""
==========================================================
2 MART
MEMORY MODEL & DAVRANIŞ DERİNLEŞME
==========================================================

Bu dosya referans mantığının derinleşmiş halidir.

Konular:
- Python Memory Model
- id() mantığı
- Nesne kimliği
- Immutable davranış
- Tuple içinde mutable
- Nesne sayma algoritması
"""

# ==========================================================
# 1) PYTHON MEMORY MODEL
# ==========================================================

"""
Python'da her şey nesnedir.

Her nesnenin:
- kimliği (id)
- tipi
- değeri vardır.
"""

a = 10
b = a

"""
id(a) == id(b)
Aynı nesne.
"""

# ==========================================================
# 2) IMMUTABLE DAVRANIŞ
# ==========================================================

s1 = "hi"
s2 = s1
s1 += "!"

"""
Yeni string oluştu.
s2 etkilenmedi.
"""

# ==========================================================
# 3) TUPLE İÇİNDE LİSTE
# ==========================================================

t = (1, [2, 3])

"""
Tuple immutable.
Ama içindeki liste mutable.
"""

t[1].append(4)

"""
Hata vermez.
Çünkü tuple değişmedi.
İç nesne değişti.
"""

# ==========================================================
# 4) NESNE SAYMA ALGORİTMASI
# ==========================================================

"""
Zor sorularda şu algoritmayı kullan:

1) Başlangıçta kaç liste var?
2) .copy() → +1 dış liste
3) = [ ... ] → +1 yeni liste
4) append → +0
5) += listeyse +0
6) + operatörü → +1
"""

# ==========================================================
# 5) KARMAŞIK ÖRNEK
# ==========================================================

a = [[1], [2]]
b = a.copy()
c = a

a[0].append(3)
b[1] = [4]
c[0] = c[0] + [5]

"""
Bu tip sorularda her satırdan sonra dur.
Yeni nesne oluştu mu diye sor.
"""

# ==========================================================
# 6) GERÇEK DERS
# ==========================================================

"""
Eksik olan genelde bilgi değil,
nesne takip refleksidir.

Çözüm:
- Bol soru
- Bol çizim
- Yavaş takip

Temel artık atıldı.
"""