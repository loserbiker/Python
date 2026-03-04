"""
==========================================================
3 MART
VERİ TİPLERİ & INPUT & TYPE SYSTEM
==========================================================

Bu dosya Python veri tiplerinin temel mantığını anlatır.

Konular:
- Python type system
- int / float / str
- type()
- input() mantığı
- type conversion
- string vs sayı farkı
- pratik örnekler
"""

# ==========================================================
# 1) PYTHON TYPE SYSTEM
# ==========================================================

"""
Python dinamik tipli bir dildir.

Yani değişkenin tipi yoktur.
NESNENİN tipi vardır.

Örnek:
"""

a = 10

"""
Burada:

a = değişken
10 = int nesnesi
"""

b = "hello"

"""
b bir string nesnesini gösterir.
"""

# ==========================================================
# 2) TYPE() FONKSİYONU
# ==========================================================

"""
type() fonksiyonu nesnenin tipini gösterir.
"""

x = 10
y = 3.14
z = "python"

# print(type(x))  -> int
# print(type(y))  -> float
# print(type(z))  -> str


# ==========================================================
# 3) INT (INTEGER)
# ==========================================================

"""
int = tam sayıları temsil eder.

Örnek:
"""

a = 10
b = -5
c = 0

"""
int immutable bir veri tipidir.
"""


# ==========================================================
# 4) FLOAT
# ==========================================================

"""
float = ondalıklı sayıları temsil eder.
"""

pi = 3.14
x = 0.5

"""
float da immutable bir veri tipidir.
"""


# ==========================================================
# 5) STRING
# ==========================================================

"""
string = karakter dizisidir.

Örnek:
"""

name = "Ali"
text = "Python öğreniyorum"

"""
string immutable'dır.
"""


# ==========================================================
# 6) STRING vs SAYI
# ==========================================================

"""
10 ile "10" farklı şeylerdir.
"""

a = 10
b = "10"

"""
a -> int
b -> str
"""


# ==========================================================
# 7) INPUT() MANTIĞI
# ==========================================================

"""
input() kullanıcıdan veri alır.

ÖNEMLİ KURAL:

input() HER ZAMAN STRING DÖNDÜRÜR
"""

# value = input("Bir şey yaz: ")

"""
Kullanıcı 5 yazsa bile:

value = "5"
"""


# ==========================================================
# 8) TYPE CONVERSION
# ==========================================================

"""
Bu yüzden çoğu zaman dönüşüm gerekir.
"""

# sayi = int(input("Sayı gir: "))

"""
Adımlar:

1) input() string döndürür
2) int() string'i sayıya çevirir
"""


# ==========================================================
# 9) FLOAT CONVERSION
# ==========================================================

# number = float(input("Ondalık sayı gir: "))


# ==========================================================
# 10) HATA ÖRNEĞİ
# ==========================================================

"""
Yanlış kullanım:
"""

# sayi = int(input())
# sayi + "5"

"""
Bu hata verir çünkü:

int + str yapılamaz
"""


# ==========================================================
# 11) GENEL ÖZET
# ==========================================================

"""
Önemli kurallar:

- Python'da değişken değil nesne tip taşır
- int = tam sayı
- float = ondalıklı sayı
- str = metin
- input() her zaman string döndürür
- sayılar için type conversion gerekir
"""