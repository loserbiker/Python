"""
==========================================================
4 MART
OPERATÖRLER - TRUTHY/FALSY - LOOPS
==========================================================

Konular:
- Aritmetik operatörler
- % operatörü
- Truthy / Falsy
- while döngüsü
- break
- for döngüsü
- range()
"""

# ==========================================================
# 1) ARİTMETİK OPERATÖRLER
# ==========================================================

"""
Python temel operatörleri:

+  toplama
-  çıkarma
*  çarpma
/  bölme
%  kalan
"""

a = 10
b = 3

# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a % b)


# ==========================================================
# 2) MODULO (%)
# ==========================================================

"""
% operatörü bölmenin kalanını verir.
"""

# print(10 % 3) -> 1
# print(14 % 2) -> 0

"""
Bu yüzden çift kontrolünde kullanılır.
"""

# if sayi % 2 == 0:
#     print("çift")


# ==========================================================
# 3) TRUTHY / FALSY
# ==========================================================

"""
Python bazı değerleri False kabul eder.

Falsy değerler:

0
""
[]
{}
None
"""

"""
Diğer tüm değerler Truthy kabul edilir.
"""

# if "":
#     print("çalışmaz")

# if "hello":
#     print("çalışır")


# ==========================================================
# 4) WHILE LOOP
# ==========================================================

"""
while = koşul doğru olduğu sürece çalışır.
"""

i = 1

# while i <= 5:
#     print(i)
#     i += 1


# ==========================================================
# 5) INFINITE LOOP
# ==========================================================

"""
while True sonsuz döngüdür.
"""

# while True:
#     print("sonsuz")


# ==========================================================
# 6) BREAK
# ==========================================================

"""
break döngüyü anında durdurur.
"""

# while True:
#     sayi = int(input("Sayı: "))
#
#     if sayi == 0:
#         break


# ==========================================================
# 7) FOR LOOP
# ==========================================================

"""
for belirli sayıda tekrar için kullanılır.
"""

# for i in range(5):
#     print(i)


# ==========================================================
# 8) RANGE()
# ==========================================================

"""
range(start, stop, step)
"""

# for i in range(1, 6):
#     print(i)

"""
çıktı:

1
2
3
4
5
"""


# ==========================================================
# 9) GERİ SAYIM
# ==========================================================

# for i in range(10, 0, -1):
#     print(i)


# ==========================================================
# 10) GENEL ÖZET
# ==========================================================

"""
- % kalan operatörüdür
- Truthy/Falsy Python'un boolean mantığıdır
- while koşula bağlı döngüdür
- for belirli tekrar içindir
- break döngüyü durdurur
- range sayı üretir
"""