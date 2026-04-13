"""
====================================
RANDOM MODÜLÜ EĞİTİMİ
====================================

Python'da rastgele sayılar ve seçimler yapmak için random modülü kullanılır.
random modülü, oyunlarda, şans uygulamalarında veya simülasyonlarda çok kullanışlıdır.
"""

# ------------------------------
# 1. random() -> 0 ile 1 arasında rastgele sayı
# ------------------------------

import random

print(random.random())  
# 0.0 <= x < 1.0 arasında rastgele bir ondalıklı sayı üretir

# ------------------------------
# 2. randint() -> Belirli aralıkta tam sayı (dahil)
# ------------------------------

print(random.randint(1, 10))  
# 1 ile 10 (her iki sınır dahil) arasında rastgele bir tam sayı üretir

# ------------------------------
# 3. randrange() -> Belirli aralıkta tam sayı (son dahil değil)
# ------------------------------

print(random.randrange(1, 10))  
# 1 <= x < 10 arası rastgele tam sayı üretir
# Not: 10 dahil değildir

# ------------------------------
# 4. choice() -> Listeden rastgele seçim
# ------------------------------

myList = ["black", "white", "orange"]
print(random.choice(myList))  
# Liste içerisinden rastgele bir eleman döndürür

# ------------------------------
# 5. choices() -> Ağırlıklı seçim
# ------------------------------

myList = ["cherry", "strawberry", "grape", "banana"]
# weights parametresi ile bazı elemanlara daha yüksek olasılık verebiliriz
print(random.choices(myList, weights=[10, 1, 1, 1], k=5))  
# 5 eleman seçer, "cherry" daha sık seçilme olasılığına sahiptir

# ------------------------------
# 6. shuffle() -> Listeyi karıştırır (değiştirir)
# ------------------------------

myList = ["harley", "bmw", "honda"]
random.shuffle(myList)  # Listeyi yerinde karıştırır
print(myList)

# ------------------------------
# 7. sample() -> Listeyi bozmadan rastgele seçim
# ------------------------------

# k parametresi ile kaç eleman seçileceğini belirleriz
print(random.sample(myList, k=2))  # Listeyi bozmaz, yeni liste döndürür

# ------------------------------
# 8. uniform() -> Ondalıklı sayılar için aralık
# ------------------------------

print(random.uniform(30, 70))  
# 30 <= x <= 70 arasında rastgele ondalıklı sayı üretir

# ------------------------------
# 9. triangular() -> Üçgensel dağılımlı rastgele sayı
# ------------------------------

print(random.triangular(30, 70, 33))  
# min=30, max=70, mode=33 olacak şekilde rastgele sayı üretir

# ------------------------------
# 10. getrandbits() -> Rastgele bit üretme
# ------------------------------

print(random.getrandbits(8))  
# 8 bitlik rastgele sayı üretir (0-255 arası)
