"""
======================================
SEQUENCE TYPES VE TEMEL VERİ YAPILARI
======================================

Python'da farklı veri yapıları vardır. Bunlar, verileri saklama ve organize etme şeklimizi belirler.

Önemli veri yapıları:
1- List (liste)        -> değiştirilebilir
2- Tuple (demet)       -> değiştirilemez
3- Range               -> belirli aralıklar oluşturmak için
4- Dictionary (sözlük) -> key-value ilişkisi
5- Set                 -> benzersiz değerler
6- FrozenSet           -> değiştirilemez set
7- Boolean             -> True veya False değerler
8- None                -> boş değer, yokluk göstergesi
"""

# ------------------------------
# 1. LIST (DEĞİŞTİRİLEBİLİR)
# ------------------------------

# Listeler köşeli parantez [] ile oluşturulur
# Listeler içindeki elemanlar değiştirilebilir (mutable)
myList = ["Apple", "Grape", "Cherry"]
print(myList)           # ['Apple', 'Grape', 'Cherry']
print(myList[0])        # İlk eleman -> 'Apple'

# Eleman ekleme:
myList.append("Banana")
print(myList)           # ['Apple', 'Grape', 'Cherry', 'Banana']

# Eleman değiştirme:
myList[1] = "Strawberry"
print(myList)           # ['Apple', 'Strawberry', 'Cherry', 'Banana']

# ------------------------------
# 2. TUPLE (DEĞİŞTİRİLEMEZ)
# ------------------------------

# Tuple parantez () ile oluşturulur
# Tuple içindeki elemanlar değiştirilemez (immutable)
myTuple = ("Red", "Blue", "White")
print(myTuple)          # ('Red', 'Blue', 'White')
print(myTuple[1])       # 1. indeks -> 'Blue'

# ------------------------------
# 3. RANGE
# ------------------------------

# Range belirli aralıklar oluşturmak için kullanılır
# Örnek: 0'dan 6'ya kadar sayılar
myRange = range(7)      # 0,1,2,3,4,5,6
print(*myRange)         # * operatörü ile tüm elemanları yazdırır

# ------------------------------
# 4. DICTIONARY (SÖZLÜK / MAPPING TYPE)
# ------------------------------

# Dictionary, key-value (anahtar-değer) çifti ile veri saklar
myDict = {"name": "Can", "yas": 27}
print(myDict)           # {'name': 'Can', 'yas': 27}

# Key üzerinden değere erişim
print(myDict["name"])   # Can

# Yeni key ekleme
myDict["meslek"] = "Öğrenci"
print(myDict)           # {'name': 'Can', 'yas': 27, 'meslek': 'Öğrenci'}

# ------------------------------
# 5. SET TYPES
# ------------------------------

# Set, benzersiz elemanlar saklar ve sırasızdır
mySet = {"Apple", "Grape", "Cherry"}
print(mySet)            # Örnek çıktı: {'Cherry', 'Apple', 'Grape'}

# FrozenSet: değiştirilemez set
myFrozen = frozenset({"Apple", "Grape", "Cherry"})
print(myFrozen)         # frozenset({'Apple', 'Grape', 'Cherry'})

# ------------------------------
# 6. BOOLEAN VE NONE
# ------------------------------

# Boolean (True / False)
myBool = True
print(type(myBool))     # <class 'bool'>

# None: boş değer, yokluk göstergesi
myNone = None
print(type(myNone))     # <class 'NoneType'>
