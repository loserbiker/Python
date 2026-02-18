"""
======================================
SEQUENCE TYPES VE TEMEL VERİ YAPILARI
======================================

Python'da farklı veri yapıları vardır. Bunlar, verileri saklama ve organize etme şeklimizi belirler.

Önemli veri yapıları:
1- List (liste)        -> değiştirilebilir (mutable)
2- Tuple (demet)       -> değiştirilemez (immutable)
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
myList = ["Apple", "Grape", "Cherry"]

# Örnekler:
myList.append("Banana")       # append() → listeye öğe ekler
myList.extend(["Mango","Kiwi"]) # extend() → listeyi başka bir liste ile genişletir
myList.insert(1,"Strawberry") # insert() → belirli konuma öğe ekler
myList.remove("Grape")        # remove() → belirli öğeyi siler
myList.pop()                  # pop() → son öğeyi çıkarır
print(myList)                 # ['Apple', 'Strawberry', 'Cherry', 'Banana', 'Mango', 'Kiwi']

# ------------------------------
# 2. TUPLE (DEĞİŞTİRİLEMEZ)
# ------------------------------
myTuple = ("Red", "Blue", "White")

# Tuple içindeki elemanlar değiştirilemez
print(myTuple[1])  # 'Blue'

# ------------------------------
# 3. RANGE
# ------------------------------
myRange = range(7)   # 0,1,2,3,4,5,6
print(*myRange)

# ------------------------------
# 4. DICTIONARY (SÖZLÜK / MAPPING TYPE)
# ------------------------------
myDict = {"name": "Can", "yas": 27}
myDict["meslek"] = "Öğrenci"
print(myDict)

# ------------------------------
# 5. SET TYPES
# ------------------------------
mySet = {"Apple", "Grape", "Cherry"}        # Sırasız ve benzersiz
myFrozen = frozenset({"Apple", "Grape"})   # Değiştirilemez set

# ------------------------------
# 6. BOOLEAN VE NONE
# ------------------------------
myBool = True
myNone = None

# ------------------------------
# 🔑 ÖNEMLİ ANAHTAR KELİMELER / METOTLAR
# ------------------------------
# append()  -> listeye öğe ekler
# extend()  -> listeyi başka liste ile genişletir
# insert()  -> belirli konuma öğe ekler
# remove()  -> öğeyi siler
# pop()     -> son öğeyi çıkarır
# len()     -> uzunluk döndürür
# range()   -> sayı dizisi oluşturur
# dict()    -> sözlük oluşturur
# set()     -> benzersiz elemanlar saklar
# frozenset()-> değiştirilemez set
