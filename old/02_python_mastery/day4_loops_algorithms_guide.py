"""
day4_loops_algorithms_guide.py
DAY 4 — DÖNGÜLER (WHILE/FOR) + ALGORİTMA PATTERN’LERİ (DERİN REHBER)

Amaç:
- while ve for mantığını gerçek kullanımla öğrenmek
- break/continue ve loop-else (az bilinen ama önemli)
- range, enumerate, zip
- döngüyle temel algoritma pattern’leri:
  - sayaç (count)
  - toplam (sum)
  - max/min bulma
  - arama (search)
  - filtreleme (filter)
- nested loops ve “zaman karmaşıklığı” sezgisi

Bu konu oturursa:
- LeetCode / algoritma sorularına giriş kapısı açılır
- oyun döngüsü (game loop) mantığı daha anlaşılır hale gelir
"""

# ============================================================
# 1) while: Koşul True olduğu sürece çalışır
# ============================================================
print("\n--- 1) while ---")

i = 0
while i < 5:
    print("i =", i)
    i += 1

"""
while kullanırken en büyük hata:
- i'yi artırmayı unutmak -> sonsuz döngü
"""

# ============================================================
# 2) for: Bir koleksiyon / range üzerinde dolaşır
# ============================================================
print("\n--- 2) for ---")

for i in range(5):
    print("i =", i)

# range(start, stop, step)
print("\nrange örnekleri:")
print(list(range(3, 10)))        # 3..9
print(list(range(3, 10, 2)))     # 3,5,7,9
print(list(range(10, 0, -1)))    # 10..1

# ============================================================
# 3) break / continue
# ============================================================
print("\n--- 3) break / continue ---")

print("break örneği:")
for i in range(10):
    if i == 5:
        break
    print(i)

print("\ncontinue örneği:")
for i in range(10):
    if i == 5:
        continue
    print(i)

# ============================================================
# 4) for-else: Döngü normal biterse else çalışır
# ============================================================
print("\n--- 4) for-else ---")

target = 7
for i in range(10):
    if i == target:
        print("bulundu:", i)
        break
else:
    print("bulunamadı")

"""
for-else mantığı:
- break olursa else çalışmaz
- break olmazsa (normal biterse) else çalışır

Arama (search) problemlerinde temizdir.
"""

# ============================================================
# 5) enumerate: index + değer birlikte
# ============================================================
print("\n--- 5) enumerate ---")

names = ["can", "harley", "python"]
for idx, name in enumerate(names):
    print(idx, name)

# ============================================================
# 6) zip: iki listeyi paralel gezmek
# ============================================================
print("\n--- 6) zip ---")

ids = [101, 102, 103]
users = ["Ali", "Veli", "Ayse"]

for i, u in zip(ids, users):
    print(i, "->", u)

# ============================================================
# 7) Pattern 1: Toplama (sum)
# ============================================================
print("\n--- 7) Pattern: sum ---")

nums = [5, 3, 8, 1]
total = 0
for n in nums:
    total += n
print("total =", total)

# ============================================================
# 8) Pattern 2: Sayma (count)
# ============================================================
print("\n--- 8) Pattern: count ---")

nums = [1, 2, 2, 3, 2, 4]
count_2 = 0
for n in nums:
    if n == 2:
        count_2 += 1
print("2 sayısı adedi:", count_2)

# ============================================================
# 9) Pattern 3: max/min bulma
# ============================================================
print("\n--- 9) Pattern: max ---")

nums = [5, 3, 8, 1]
current_max = nums[0]
for n in nums:
    if n > current_max:
        current_max = n
print("max =", current_max)

# ============================================================
# 10) Pattern 4: Arama (search)
# ============================================================
print("\n--- 10) Pattern: search ---")

nums = [10, 20, 30, 40]
target = 30
found = False

for n in nums:
    if n == target:
        found = True
        break

print("found =", found)

# for-else ile daha temiz:
for n in nums:
    if n == target:
        print("for-else: bulundu")
        break
else:
    print("for-else: bulunamadı")

# ============================================================
# 11) Pattern 5: Filtreleme (filter)
# ============================================================
print("\n--- 11) Pattern: filter ---")

nums = [1, 2, 3, 4, 5, 6]
evens = []
for n in nums:
    if n % 2 == 0:
        evens.append(n)
print("evens =", evens)

# ============================================================
# 12) Nested loops: iç içe döngü
# ============================================================
print("\n--- 12) Nested loops ---")

for i in range(3):
    for j in range(3):
        print(i, j)

"""
Zaman sezgisi (çok önemli):
- tek döngü: ~N iş
- nested döngü: ~N*N iş

N büyüdükçe N^2 çok pahalı olur.
Bu fikir ileride algoritmada çok işine yarayacak.
"""

# ============================================================
# 13) Mini algoritmalar (kas geliştirme)
# ============================================================
print("\n--- 13) Mini algoritmalar ---")

# 13.1) Listeyi ters çevirme (slice kullanmadan, mantık)
nums = [1, 2, 3, 4]
reversed_nums = []
for i in range(len(nums) - 1, -1, -1):
    reversed_nums.append(nums[i])
print("reversed =", reversed_nums)

# 13.2) İki listenin elemanlarını toplayıp yeni liste üretme
a = [1, 2, 3]
b = [10, 20, 30]
c = []
for x, y in zip(a, b):
    c.append(x + y)
print("sum lists =", c)

# 13.3) Basit “en yakın” mantığı: hedefe en yakın sayı
nums = [2, 9, 15, 21]
target = 14
closest = nums[0]
for n in nums:
    if abs(n - target) < abs(closest - target):
        closest = n
print("closest to", target, "=", closest)

# ============================================================
# 14) Egzersizler (kendin geliştir)
# ============================================================
print("\n--- 14) Egzersizler ---")

# Egz1: 1'den 100'e kadar çift sayıların toplamı
total = 0
for i in range(1, 101):
    if i % 2 == 0:
        total += i
print("Egz1 çift toplam =", total)

# Egz2: Bir listede kaç tane negatif var?
nums = [3, -1, -5, 7, -2, 0]
neg_count = 0
for n in nums:
    if n < 0:
        neg_count += 1
print("Egz2 negatif sayısı =", neg_count)

# Egz3: Kullanıcı adı listesinde arama (case-insensitive)
users = ["Can", "Ali", "Veli"]
query = "can"

found = False
for u in users:
    if u.lower() == query.lower():
        found = True
        break
print("Egz3 bulundu mu?", found)

"""
DAY 4 CHECKLIST ✅
- while/for + range
- break/continue + for-else
- enumerate + zip
- sum/count/max/search/filter pattern’leri
- nested loop sezgisi
"""