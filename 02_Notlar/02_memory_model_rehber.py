"""
==========================================================
2 MART
PYTHON MEMORY MODEL & NESNE DAVRANIŞI
==========================================================

Bu dosya referans mantığının derinleşmiş halidir.

Konular:
- Python Memory Model
- id() mantığı
- Nesne kimliği
- Immutable davranış
- Tuple içinde mutable nesne
- Nesne takip algoritması
"""

# ==========================================================
# 1) PYTHON MEMORY MODEL
# ==========================================================

"""
Python'da her şey nesnedir.

Bir nesnenin üç temel özelliği vardır:

1) Kimlik (identity)
2) Tip (type)
3) Değer (value)
"""

a = 10
b = a

"""
Burada:

a ve b aynı nesneyi gösterir.

Kontrol edebiliriz:
"""

# id(a)
# id(b)

"""
id() fonksiyonu nesnenin kimliğini gösterir.

Eğer iki değişken aynı nesneyi gösteriyorsa:

id(a) == id(b)
"""

# ==========================================================
# 2) NESNE KİMLİĞİ (IDENTITY)
# ==========================================================

"""
Kimlik = nesnenin bellekteki adresi gibi düşünülebilir.

Örnek:
"""

x = [1,2]
y = x

"""
Bellek modeli:

x ----\
       ---> [1,2]
y ----/
"""

"""
Yeni nesne oluşturursak:
"""

z = [1,2]

"""
z artık farklı bir nesnedir.

id(x) != id(z)
"""

# ==========================================================
# 3) IMMUTABLE DAVRANIŞ
# ==========================================================

"""
Immutable nesneler değiştirilemez.

Örnek:

int
str
tuple
float
"""

s1 = "hi"
s2 = s1

s1 += "!"

"""
Burada olan şey:

Yeni string oluşur.

Bellek:

s2 ----> "hi"

s1 ----> "hi!"
"""

# ==========================================================
# 4) TUPLE İÇİNDE MUTABLE NESNE
# ==========================================================

"""
Tuple immutable bir yapıdır.

Ama içinde mutable nesneler bulunabilir.
"""

t = (1, [2,3])

"""
Tuple değişmez.

Ama içindeki liste değişebilir.
"""

t[1].append(4)

"""
Bu hata vermez.

Çünkü:

tuple değişmedi
iç liste değişti
"""

# ==========================================================
# 5) NESNE TAKİP ALGORİTMASI
# ==========================================================

"""
Zor referans sorularında şu algoritma işe yarar:

1) Başlangıçta kaç nesne var?
2) Her satırda yeni nesne oluşuyor mu?
3) Referans mı değişti yoksa nesne mi?
"""

"""
Önemli kurallar:

.copy()  → yeni DIŞ liste (+1)

= [ ... ] → yeni liste (+1)

append   → in-place (+0)

+= (list) → çoğu durumda in-place (+0)

+ operatörü → yeni liste (+1)
"""

# ==========================================================
# 6) KARMAŞIK REFERANS ÖRNEĞİ
# ==========================================================

a = [[1],[2]]
b = a.copy()
c = a

"""
Bellek:

a ----\
       ----> [[1],[2]]
c ----/

b ----> yeni dış liste
"""

a[0].append(3)

"""
İç liste değişti.

a ve c etkilenir.
"""

b[1] = [4]

"""
b'nin referansı değişti.
a etkilenmez.
"""

c[0] = c[0] + [5]

"""
+ operatörü yeni liste üretir.

Bu yüzden sadece c etkilenir.
"""

# ==========================================================
# 7) BU KONUNUN GERÇEK DERSİ
# ==========================================================

"""
Referans sorularında eksik olan şey genelde bilgi değildir.

Eksik olan şey:

Nesne takip refleksi.

Çözüm:

- her satırdan sonra dur
- yeni nesne oluştu mu sor
- bellek diyagramı çiz
- acele etme
"""

# ==========================================================
# 8) GENEL ÖZET
# ==========================================================

"""
Python'da:

değişken = referans
nesne = gerçek veri

Önemli kurallar:

- id() nesne kimliğini verir
- immutable değişmez
- mutable yerinde değişir
- tuple immutable olsa da iç nesne değişebilir
- referans sorularında nesne saymayı öğrenmek gerekir
"""