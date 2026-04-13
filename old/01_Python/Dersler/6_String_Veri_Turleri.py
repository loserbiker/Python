########## STRING VERİ TÜRLERİ EĞİTİMİ ############

# STRING (metin) NEDİR?
# Python'da string, tırnaklar içine yazılan metinleri ifade eder.
# Örneğin bir isim, cümle veya kelime string olarak saklanabilir.

# Tek tırnak ile string oluşturma
text = 'python'
print(text)  # Çıktı: python

# Çift tırnak ile string oluşturma
text2 = "python"
print(text2)  # Çıktı: python

# Üçlü tırnak ile çok satırlı string oluşturma
text3 = """python
python
python"""
print(text3)
# Çıktı:
# python
# python
# python

# Aynı şekilde tek üçlü tırnak da kullanabiliriz
text4 = '''python
python
python'''
print(text4)
# Çıktı yine aynı

# -------------------------------------------------
# STRINGLER VE LİSTELER ARASINDA BENZERLİK
# -------------------------------------------------

# Liste örneği
araba_listesi = ["BMW", "Volvo", "Skoda", "Nissan"]

# Listelerdeki elemanlara indeks ile erişebiliriz
# İndeksler 0'dan başlar!
print(araba_listesi[0])  # 0. indeks 1. eleman -> BMW
print(araba_listesi[3])  # 3. indeks 4. eleman -> Nissan

# Stringlerde de aynı mantık geçerlidir
text5 = "Hello, Python!"
print(text5[0])   # 0. karakter -> H
print(text5[13])  # 13. karakter -> !

# -------------------------------------------------
# STRING İÇİNDEKİ HER KARAKTERİ TEK TEK YAZDIRMA
# -------------------------------------------------

# for döngüsü ile stringdeki her karakteri teker teker yazdırabiliriz
text6 = "Python is weird"

for x in text6:  # text6 içindeki her karakter sırayla x değişkenine aktarılır
    print(x)

# Çıktı:
# P
# y
# t
# h
# o
# n
#  
# i
# s
#  
# w
# e
# i
# r
# d

# -------------------------------------------------
# STRING UZUNLUĞUNU ÖLÇMEK
# -------------------------------------------------

# len() fonksiyonu, stringin içindeki karakter sayısını döndürür
text7 = "Python is weird"
print(len(text7))  # Çıktı: 15

# NOT: Boşluklar ve noktalama işaretleri de karakter sayısına dahildir

# -------------------------------------------------
# STRING İÇİNDE KELİME ARAMA: in ve not in
# -------------------------------------------------

text8 = "The best languages in life are free!"

# in ifadesi
# "free" kelimesi text8 içinde var mı kontrol eder
print("free" in text8)  # Çıktı: True

# not in ifadesi
# "free" kelimesi text8 içinde yok mu kontrol eder
print("free" not in text8)  # Çıktı: False

# Daha anlaşılır bir örnek
search = "best"  # Aradığımız kelimeyi bir değişkene atayabiliriz

# in kullanımı
if search in text8:  # Eğer text8 içinde "best" varsa
    print("Best kelimesi var")
else:
    print("Best kelimesi yok")

# not in kullanımı
if search not in text8:  # Eğer text8 içinde "best" yoksa
    print("Best kelimesi yok")
else:
    print("Best kelimesi var")

# Özet:
# - in: aranan ifade varsa True, yoksa False döner
# - not in: aranan ifade yoksa True, varsa False döner

# -------------------------------------------------
# ÖRNEKLERLE PEKİŞTİRME
# -------------------------------------------------

# 1. Stringin ilk 3 karakterini yazdırma
ornek_text = "Python"
print(ornek_text[0:3])  # Çıktı: Pyt

# 2. Stringin son 4 karakteri
print(ornek_text[-4:])  # Çıktı: thon

# 3. String içinde boşlukları sayma
bosluk_sayisi = ornek_text.count(" ")
print("Boşluk sayısı:", bosluk_sayisi)  # Çıktı: 0 (çünkü boşluk yok)

# 4. Kelimenin string içinde olup olmadığını kontrol et
if "Py" in ornek_text:
    print("Py bulundu!")
else:
    print("Py bulunamadı!")
