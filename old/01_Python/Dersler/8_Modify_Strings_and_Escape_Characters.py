# ====================================================
# Python String Metodları ve Kaçış Karakterleri Özet
# ====================================================
# Bu dosya Python string metodlarını ve kaçış karakterlerini
# örneklerle gösterir. Not alırken veya GitHub referansı
# olarak kullanılabilir.

# ==========================================
# STRING METODLARI
# ==========================================

text = "Python is doing well"

# 1. upper() - Tüm harfleri büyük yapar
print("upper():", text.upper())  # PYTHON IS DOING WELL

# 2. lower() - Tüm harfleri küçük yapar
print("lower():", text.lower())  # python is doing well

# 3. strip() - Baş ve sondaki boşlukları temizler
text_with_spaces = "   Python is doing well   "
print("strip():", text_with_spaces.strip())  # Python is doing well

# 4. replace() - Belirli karakter veya kelimeyi değiştirir
print("replace():", text.replace("P", "T"))  # Tython is doing well

# 5. split() - Stringi boşluklardan veya belirli karakterden listeye böler
print("split():", text.split())  # ['Python', 'is', 'doing', 'well']

# 6. join() - Listeyi string hâline getirir
words = ['Python', 'is', 'doing', 'well']
print("join():", " ".join(words))  # Python is doing well

# 7. find() - Belirli karakter veya kelimenin ilk konumunu bulur
print("find():", text.find("doing"))  # 10

# 8. count() - Belirli karakter veya kelimenin kaç kez geçtiğini sayar
print("count():", text.count("o"))  # 3

# 9. startswith() - Belirli karakter veya kelime ile başlıyor mu?
print("startswith():", text.startswith("Python"))  # True

# 10. endswith() - Belirli karakter veya kelime ile bitiyor mu?
print("endswith():", text.endswith("well"))  # True

# 11. isalpha() - Sadece harflerden oluşmuş mu?
print("isalpha():", text.isalpha())  # False (boşluk var)

# 12. isdigit() - Sadece rakamlardan oluşmuş mu?
number_string = "12345"
print("isdigit():", number_string.isdigit())  # True

# 13. isspace() - Sadece boşluk karakterlerinden oluşmuş mu?
space_string = "   "
print("isspace():", space_string.isspace())  # True

# 14. capitalize() - İlk harfi büyük yapar
print("capitalize():", text.capitalize())  # Python is doing well

# 15. title() - Her kelimenin ilk harfini büyük yapar
print("title():", text.title())  # Python Is Doing Well

# 16. swapcase() - Büyük harfleri küçük, küçük harfleri büyük yapar
print("swapcase():", text.swapcase())  # pYTHON IS DOING WELL

# 17. len() - Stringin uzunluğunu döndürür
print("len():", len(text))  # 22

# 18. index() - Belirli karakter veya kelimenin konumu (bulamazsa ValueError)
print("index():", text.index("doing"))  # 10

# 19. rindex() - Belirli karakterin son konumu
print("rindex():", text.rindex("o"))  # 17

# 20. zfill() - Başına sıfır ekler, toplam uzunluk belirlenir
number_string = "123"
print("zfill():", number_string.zfill(5))  # 00123

# 21. lstrip() - Başındaki boşlukları temizler
text_with_leading_spaces = "   Python is doing well"
print("lstrip():", text_with_leading_spaces.lstrip())  # Python is doing well

# 22. rstrip() - Sonundaki boşlukları temizler
text_with_trailing_spaces = "Python is doing well   "
print("rstrip():", text_with_trailing_spaces.rstrip())  # Python is doing well

# 23. center() - Belirli genişlikte ortalar
print("center():", text.center(30))  # Python is doing well ortalanır

# 24. ljust() - Belirli genişlikte sola yaslar
print("ljust():", text.ljust(30))  # Python is doing well sola yaslanır

# 25. rjust() - Belirli genişlikte sağa yaslar
print("rjust():", text.rjust(30))  # Python is doing well sağa yaslanır

# 26. partition() - Belirli kelimeye göre üç parçaya böler
print("partition():", text.partition("doing"))  # ('Python is ', 'doing', ' well')

# 27. rpartition() - Son eşleşmeye göre üç parçaya böler
print("rpartition():", text.rpartition("o"))  # ('Python is d', 'o', 'ing well')

# 28. splitlines() - Satır sonuna göre böler
multiline_text = "Python is doing well\nIt's a great language!"
print("splitlines():", multiline_text.splitlines())  # ['Python is doing well', "It's a great language!"]

# 29. expandtabs() - Sekme karakterlerini boşlukla değiştirir
text_with_tabs = "Python\tis\tdoing\twell"
print("expandtabs():", text_with_tabs.expandtabs(4))  # Sekmeler 4 boşluk ile değiştirildi

# 30. maketrans() ve translate() - Belirli karakterleri dönüştürmek için kullanılır
translation_table = str.maketrans("aeiou", "12345")  # a->1, e->2, i->3, o->4, u->5
translated_text = text.translate(translation_table)
print("translate():", translated_text)  # Pyth4n 3s d4ing w2ll

# 31. format() - String içine değer yerleştirmek
name = "Alice"
age = 30
formatted_text = "My name is {} and I am {} years old.".format(name, age)
print("format():", formatted_text)

# 32. f-string (Python 3.6+) - String içinde değişken kullanımı
formatted_text_fstring = f"My name is {name} and I am {age} years old."
print("f-string:", formatted_text_fstring)

# ==========================================
# KAÇIŞ KARAKTERLERİ (ESCAPE CHARACTERS)
# ==========================================

# \n - Yeni satır
print("Newline:\\n\nPython is doing well\nGreat!")

# \t - Sekme
print("Tab:\\t\tPython\tis\tfun!")

# \\ - Ters eğik çizgi
print("Backslash:\\\\C:\\Program Files\\Python")

# \' - Tek tırnak
print("Single quote:\\'Python\\'s syntax is simple.")

# \" - Çift tırnak
print("Double quote: \"He said, \\\"Python is awesome!\\\"\"")

# \r - Satır başına dönme
print("Carriage return:\\rHello\rWorld")

# \b - Geri silme
print("Backspace:\\bHello\bWorld")

# \f - Form feed
print("Form feed:\\fHello\fWorld")

# \v - Dikey sekme
print("Vertical tab:\\vHello\vWorld")

# \ooo - Oktal karakter
print("Octal:\\101")  # A

# \xhh - Hexadecimal karakter
print("Hexadecimal:\\x41")  # A

# \uXXXX - Unicode
print("Unicode 16-bit:\\u0041")  # A

# \UXXXXXXXX - Unicode 32-bit
print("Unicode 32-bit:\\U00000041")  # A

# \N{name} - Unicode karakter isimle
print("Unicode named:\\N{LATIN CAPITAL LETTER A}")  # A

# \a - Alarm (bell)
print("Alarm:\\aHello World")

# \0 - Null karakter
print("Null char:\\0Hello")

# Not: Python'da \Z, \cX, \e, \g, \h, \i, \j, \k, \l, \m gibi bazı gelecekteki veya geçersiz escape karakterleri
# çalıştırıldığında SyntaxError verir. Bu yüzden eğitim amaçlı yorum satırı ile bırakıldı.
