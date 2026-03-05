"""
day2_data_types_guide.py
DAY 2 — VERİ TİPLERİ (DERİN REHBER)

Amaç:
- Python’daki temel veri tiplerini "ezber" değil "mantık" ile öğrenmek
- Hangi tip mutable/immutable? Neden önemli?
- Tip dönüşümleri, sık hatalar, en çok kullanılan metotlar
- String/list/dict üzerinde gerçek hayatta en çok yapılan işlemler

Bu günün sonunda:
- “Hangi durumda hangi veri tipi?” sorusuna net cevap verebilmelisin.
"""

# ============================================================
# 0) type() ve isinstance()
# ============================================================
print("\n--- 0) type & isinstance ---")

x = 10
print(type(x))

# isinstance: daha esnek kontrol
print(isinstance(x, int))
print(isinstance(x, (int, float)))

# ============================================================
# 1) Sayılar: int / float
# ============================================================
print("\n--- 1) int / float ---")

a = 10
b = 3
print("a/b =", a / b)    # her zaman float döner
print("a//b =", a // b)  # floor division (aşağı yuvarlar)
print("a%b =", a % b)    # modulo (kalan)

# Negatiflerde // ve % dikkat:
print("\nNegatiflerde // ve %:")
print("-10 // 3 =", -10 // 3)  # -4
print("-10 % 3  =", -10 % 3)   # 2

"""
Neden böyle?
Python şu denklemi korur:
a = (a//b)*b + (a%b)

Bu yüzden negatiflerde sonuçlar “beklenmedik” gelebilir.
"""

# Float hassasiyet:
print("\nFloat hassasiyet:")
print(0.1 + 0.2)  # 0.30000000000000004 gibi

"""
Float ikili (binary) temsil nedeniyle bazen tam olmaz.
Para işlemlerinde dikkat (decimal gerekebilir).
"""

# ============================================================
# 2) Boolean (bool)
# ============================================================
print("\n--- 2) bool ---")

print(True + True)  # 2 (bool aslında int gibi davranır)
print(False + 10)   # 10

# ============================================================
# 3) NoneType (None)
# ============================================================
print("\n--- 3) None ---")

x = None
print(x, type(x))
print("x is None ->", x is None)

"""
None = "değer yok" / "henüz atanmadı" gibi düşün.
== yerine is kullanmak daha doğru bir pratik.
"""

# ============================================================
# 4) String (str) — immutable
# ============================================================
print("\n--- 4) str ---")

s = "python"
print("s =", s)
print("len(s) =", len(s))

# Indexing ve slicing
print("s[0] =", s[0])
print("s[-1] =", s[-1])
print("s[1:4] =", s[1:4])
print("s[:3] =", s[:3])
print("s[3:] =", s[3:])

"""
Slicing mantığı:
[start:stop]  -> stop dahil değildir.
"""

# String metotları
text = "  Can HARLEY python  "
print("\nString methods:")
print(text.strip())
print(text.lower())
print(text.upper())
print(text.title())
print(text.replace("python", "PYTHON"))
print("can" in text.lower())

# split/join
csv = "a,b,c"
parts = csv.split(",")
print("\nsplit:", parts)
back = "-".join(parts)
print("join :", back)

"""
String immutable olduğu için:
- replace/upper gibi işlemler yeni string döndürür.
"""

# ============================================================
# 5) List (list) — mutable
# ============================================================
print("\n--- 5) list ---")

lst = [10, 20, 30]
print(lst)
lst.append(40)
print("append:", lst)

lst.insert(1, 999)
print("insert:", lst)

removed = lst.pop()   # sondan alır
print("pop removed:", removed, "list:", lst)

lst.remove(999)       # değere göre siler (ilk bulduğunu)
print("remove:", lst)

# Slicing listelerde de var
print("lst[:2] =", lst[:2])

# List comprehension (bugün “tanışma”)
nums = [1, 2, 3, 4, 5]
squares = [n * n for n in nums]
print("squares:", squares)

# ============================================================
# 6) Tuple (tuple) — immutable
# ============================================================
print("\n--- 6) tuple ---")

t = (10, 20, 30)
print(t, type(t))

"""
Tuple:
- değişmez (immutable)
- genelde sabit veri grupları için
- performans/niyet belirtir: “bunu değiştirmeyeceğim”
"""

# unpacking
a, b, c = t
print("unpacking:", a, b, c)

# Tek eleman tuple tuzağı:
one = (10)
one_tuple = (10,)
print("\nTek eleman tuple farkı:")
print(type(one), one)
print(type(one_tuple), one_tuple)

# ============================================================
# 7) Dict (dict) — mutable
# ============================================================
print("\n--- 7) dict ---")

user = {"name": "Can", "age": 25}
print(user)
print("name:", user["name"])

# get ile güvenli erişim
print("city:", user.get("city"))          # yoksa None
print("city default:", user.get("city", "Ankara"))

# update / setdefault
user["city"] = "Ankara"
user.update({"age": 26})
print("updated:", user)

# keys/values/items
print("keys:", list(user.keys()))
print("values:", list(user.values()))
print("items:", list(user.items()))

# dict içinde döngü
print("\nDict loop:")
for k, v in user.items():
    print(k, "->", v)

# ============================================================
# 8) Set (set) — mutable (ama elemanlar hashable olmalı)
# ============================================================
print("\n--- 8) set ---")

s = {1, 2, 2, 3}
print("set unique:", s)

s.add(10)
print("add:", s)

# set operasyonları
a = {1, 2, 3}
b = {3, 4, 5}
print("union:", a | b)
print("intersection:", a & b)
print("difference:", a - b)

"""
Set neden kullanılır?
- “var mı?” kontrolü çok hızlıdır
- tekrarları temizlemek için mükemmel
"""

# ============================================================
# 9) Tip dönüşümleri ve sık hatalar
# ============================================================
print("\n--- 9) Type casting ---")

n = "123"
print(int(n) + 7)

# input() her zaman string döner
# age = input("yas: ") -> str
# age_int = int(age)

# Hatalı dönüşüm:
bad = "12.5"
# int(bad)  # ValueError (çünkü 12.5 int'e direkt çevrilmez)
print(float(bad))

# ============================================================
# 10) Mutability özeti (çok kritik)
# ============================================================
"""
IMMUTABLE:
- int, float, bool, str, tuple, NoneType

MUTABLE:
- list, dict, set

Bu ayrım, Day1’deki referans/bellek mantığı ile birleşince
“neden böyle oldu?” sorularını çözer.
"""

# ============================================================
# 11) Egzersizler (kendin yap)
# ============================================================
print("\n--- 11) Egzersizler ---")

# Egz1: Bir string al: "can harley python"
# - kelimeleri ayır (split)
# - her kelimenin ilk harfini büyüt (title)
# - tekrar birleştir
sample = "can harley python"
result = " ".join([w.capitalize() for w in sample.split()])
print("Egz1 ->", result)

# Egz2: Bir listede tekrarları temizle (set kullan)
lst = [1, 1, 2, 3, 3, 3, 4]
unique = list(set(lst))
print("Egz2 ->", unique)

# Egz3: user dict'inden güvenli şekilde "email" oku, yoksa "yok" yaz
user = {"name": "Can"}
print("Egz3 ->", user.get("email", "yok"))

"""
DAY 2 CHECKLIST ✅
- str/list/dict/set üzerinde temel işlemler
- slicing + unpacking
- dict.get ile güvenli erişim
- mutability farkını bilmek
- casting hatalarını tanımak
"""