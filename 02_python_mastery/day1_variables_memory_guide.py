"""
day1_variables_memory_guide.py
DAY 1 — DEĞİŞKENLER, REFERANSLAR, BELLEK MODELİ (DERİN REHBER)

Bu rehberin amacı:
- "Değişken = kutu" masalını bırakıp, Python'ın gerçek çalışma mantığını öğrenmek
- Değişkenlerin "değer tutmadığını", OBJELERE REFERANS tuttuğunu görmek
- Mutable / Immutable farkını bellek açısından anlamak
- Kopyalama (copy) problemlerini temelden çözmek

⭐ Bu konu oturursa:
- list/dict hatalarının %70’i bitiyor
- OOP ve fonksiyonlarda "neden böyle oldu?" sorusu azalıyor
- Debug becerin hızlanıyor

Not:
- id() çıktıları her çalıştırmada farklı olabilir. Bu normal.
"""

# ============================================================
# 0) Python'da "değer" nerede durur?
# ============================================================
print("\n--- 0) Python bellek fikri ---")

x = 5
print("x =", x)
print("id(x) =", id(x))

"""
Burada olan şey:

1) Python bellekte bir INTEGER OBJESİ oluşturur (değer: 5)
2) x ismi (label) o objeye bağlanır (referans eder)

Yani:
x  ->  [int object: 5]

x "5'i içinde tutmaz"
x sadece "5 değerli objeyi işaret eder"
"""

# ============================================================
# 1) Atama (=) aslında "kopyalama" değildir
# ============================================================
print("\n--- 1) Atama kopyalama değildir ---")

a = 10
b = a

print("a =", a, "id(a) =", id(a))
print("b =", b, "id(b) =", id(b))

"""
b = a demek:
- a'nın işaret ettiği objeyi b de işaret etsin demek

Yani:
a -> [10]
b -> [10]   (aynı obje)

Bu yüzden id(a) ve id(b) genelde aynı çıkar.
"""

# ============================================================
# 2) Immutable: "değiştirilemeyen" objeler
# ============================================================
print("\n--- 2) Immutable (int/float/str/tuple) ---")

x = 10
print("x =", x, "id(x) =", id(x))

x = x + 1
print("x =", x, "id(x) =", id(x))

"""
Kritik fikir:
- Immutable objeler "yerinde" değişmez
- x = x + 1 dediğinde, 10 objesi değişmez
- yeni bir 11 objesi oluşur, x artık onu işaret eder

Yani:
x -> [10]  (önce)
x -> [11]  (sonra)
"""

# String de immutable’dır:
s = "can"
print("\nString immutable örneği:")
print("s =", s, "id(s) =", id(s))
s = s.upper()
print("s =", s, "id(s) =", id(s))

# ============================================================
# 3) Mutable: "yerinde değişebilen" objeler
# ============================================================
print("\n--- 3) Mutable (list/dict/set) ---")

lst = [1, 2, 3]
print("lst =", lst, "id(lst) =", id(lst))

lst.append(4)
print("lst =", lst, "id(lst) =", id(lst))

"""
Burada id aynı kalır çünkü:
- list objesi yerinde değiştirildi
- yeni obje oluşmadı, aynı objenin içeriği değişti
"""

# ============================================================
# 4) En kritik bug: Aynı listeyi iki isimle paylaşmak
# ============================================================
print("\n--- 4) Referans bug'ı (paylaşılan mutable) ---")

a = [1, 2, 3]
b = a

b.append(999)

print("a =", a)
print("b =", b)
print("id(a) =", id(a))
print("id(b) =", id(b))

"""
Şok etkisi 😄
b.append(999) yaptın ama a da değişti.

Neden?
- a ve b aynı liste objesini işaret ediyor

a -> [1,2,3,999]
b -> [1,2,3,999]
"""

# ============================================================
# 5) Shallow copy (yüzeysel kopya) nedir?
# ============================================================
print("\n--- 5) Shallow copy (.copy / list() / [:]) ---")

a = [1, 2, 3]
b = a.copy()

b.append(999)

print("a =", a, "id(a) =", id(a))
print("b =", b, "id(b) =", id(b))

"""
Artık a ve b farklı listeler.
Shallow copy = dış kabuğu kopyalar.
"""

# 3 farklı shallow copy yöntemi:
a = [1, 2, 3]
b1 = a.copy()
b2 = list(a)
b3 = a[:]
print("\nShallow copy yöntemleri aynı işi görür:")
print(b1, b2, b3)

# ============================================================
# 6) Deep copy (derin kopya) ne zaman gerekir?
# ============================================================
print("\n--- 6) Nested (iç içe) yapılarda copy tuzağı ---")

nested = [[1, 2], [3, 4]]
shallow = nested.copy()   # sadece dış listeyi kopyalar

shallow[0].append(999)

print("nested  =", nested)
print("shallow =", shallow)

"""
Burada nested da değişti!
Çünkü:
- dış liste kopyalandı ama iç listeler aynı referanslar

nested[0] ve shallow[0] aynı iç listeyi işaret ediyor.
"""

# Deep copy için:
import copy

nested = [[1, 2], [3, 4]]
deep = copy.deepcopy(nested)

deep[0].append(999)

print("\nDeep copy sonrası:")
print("nested =", nested)
print("deep   =", deep)

# ============================================================
# 7) is vs ==  (kimlik vs eşitlik)
# ============================================================
print("\n--- 7) is vs == ---")

a = [1, 2, 3]
b = [1, 2, 3]

print("a == b :", a == b)   # içerik eşit mi?
print("a is b :", a is b)   # aynı obje mi?

"""
== : değer/ içerik karşılaştırır
is : aynı memory objesi mi diye bakar (kimlik)

Çoğu zaman list/dict karşılaştırırken == kullanırsın.
is genelde None kontrolünde temizdir:
if x is None: ...
"""

x = None
print("x is None:", x is None)

# ============================================================
# 8) Pratik düşünme: "değişken okları" tekniği
# ============================================================
"""
Bu konuyu kalıcı yapmanın en iyi yolu:
- kağıda oklarla çizmek

Örnek:
a = [1,2]
b = a
b.append(9)

Çiz:
a ---> [1,2,9]
b ---^

Bu çizim refleksi gelişince debug kolaylaşır.
"""

# ============================================================
# 9) Egzersizler (kendin yap)
# ============================================================
print("\n--- 9) Egzersizler ---")

# Egzersiz 1:
# a = 10
# b = a
# a = 20
# Çıktı olarak b kaç olur ve neden?
a = 10
b = a
a = 20
print("Egz1 -> b =", b)
# Beklenti: b = 10 (b hala 10 objesini işaret ediyor)

# Egzersiz 2:
# a = [1,2]
# b = a
# a = [1,2,3]
# b ne olur? neden?
a = [1, 2]
b = a
a = [1, 2, 3]
print("Egz2 -> a =", a, "b =", b)
# Beklenti: b eski [1,2] listesini işaret etmeye devam eder.

# Egzersiz 3 (nested copy):
# nested = [[1],[2]]
# shallow = nested.copy()
# shallow[0].append(9)
# nested ne olur? (Önce tahmin et, sonra çalıştır)
nested = [[1], [2]]
shallow = nested.copy()
shallow[0].append(9)
print("Egz3 -> nested =", nested, "shallow =", shallow)

"""
DAY 1 CHECKLIST ✅
- Atama kopyalama değildir (referans bağlar)
- Mutable objeler yerinde değişir
- Immutable objeler yeni obje üretir
- Shallow copy dış kabuğu kopyalar
- Nested yapılarda deep copy gerekebilir
- == içerik, is kimliktir
"""