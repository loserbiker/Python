# Python String Manipülasyonu ve Kaçış Karakterleri

# 1. upper() - Tüm harfleri büyük yapar
text = "Python is doing well"
print(text.upper())  # PYTHON IS DOING WELL

# 2. lower() - Tüm harfleri küçük yapar
print(text.lower())  # python is doing well

# 3. strip() - Baş ve sondaki boşlukları temizler
text_with_spaces = "   Python is doing well   "
print(text_with_spaces.strip())  # Python is doing well

# 4. replace() - Karakter veya kelime değiştirir
print(text.replace("P", "T"))  # Tython is doing well

# 5. split() - Stringi bir listeye ayırır
print(text.split())  # ['Python', 'is', 'doing', 'well']


# Kaçış Karakterleri

# 1. \n - Satır başı (new line)
text_with_newline = "Python is doing well\nIt's a great language!"
print(text_with_newline)

# 2. \t - Sekme (tab)
text_with_tab = "Python is doing well\tGreat!"
print(text_with_tab)

# 3. \\ - Ters eğik çizgi (backslash)
path = "C:\\Program Files\\Python"
print(path)

# 4. \' - Tek tırnak karakteri
single_quote_text = 'Python\'s syntax is simple.'
print(single_quote_text)

# 5. \" - Çift tırnak karakteri
double_quote_text = "He said, \"Python is awesome!\""
print(double_quote_text)
