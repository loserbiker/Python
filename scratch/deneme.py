def harf_notu(puan):
    if puan >= 85:
        return "A"
    elif puan >= 70:
        return "B"
    elif puan >= 50:
        return "C"
    else:
        return "F"
print(harf_notu(90))
print(harf_notu(72))
print(harf_notu(40))