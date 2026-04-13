#VARIABLE (DEĞİŞKENLER)

#Veri değerlerini depolamak için kullanılan kaplardır.


x = 7
#x is of type integer (int) - tam sayısal işlem

y = "python"
#y is of type str (string) - metinsel işlem Not: Metinsel ifadelerde "" ve '' kullanılabilir.

z = 0.54
#z is of type float - ondalıklı sayılarda kullanılır

# (=) değer atama operatörüdür.

# atadığın değerlerin tiplerini görmek için
print(type(x)) #komutunu kullanabilirsin
 

#Variable Case Sensitive (Veriable (Değişken) ismini büyük küçük harfe duyarlı olduğunu belirtir.)

name="hello"
Name="hello"

# Değişken isimleri aynı gibi görünse de büyük küçük harf hassasiyetinden dolayı farklı sayılır.

# Yukarıda atadığımız değişkenleri silip değiştirmek yerine aşağıda aynı değişkenlere farklı
# değerler atayabilmekteyiz.

x = 7
y = "selam"
z = 0.75

x = 8
y = "merhaba"
z = 0.50 #gibi

#Değişken isimlerini dilediğiniz gibi türkçe karakterlede yazabilirsiniz.

toplam_değer = 798
print(toplam_değer)

#Bir veriable adı bir harfle veya alt çizgi karakteri ile başlamalıdır.

_isim= "Can"
isim= "Can"

print(_isim)
print(isim)

###### KURALLAR ######
# 1- BİR VARİABLE ADI ASLA BİR SAYI İLE BAŞLAYAMAZ!!
# 2- Bir variable adı yalnızca alfa-sayısal karakterler ve alt çizgiler (Az, 0-9, ve _) içerebilir.
# 3- Variable (değişken) adları büyük/küçük harfe duyarlıdır (age, Age ve AGE üç farklı değişkendir.)
# 4- Bir variable (değişken) adı Python anahtar sözcüklerinden hiçbiri olamaz.
#Not: Variable ismi içerisinde tuttuğu değeri özetlemelidir.


# Multi Words Variable Names (Çoklu Kelimeler İçeren Değişken İsimleri)

# Camel Case = İlk kelime hariç her kelime Büyük harfle başlar

myName = "Can"
kupunToplamHacmi = 70

#Not: Variable ismi içerisinde tuttuğu değeri özetlemelidir

# Pascal Case = Her kelime büyük harfle başlar (Upper Camel Case olarak bilinir.)

KupunToplamHacmi = 80
AdımNedir = "Can"

# Snake Case = Her kelime bir alt çizgi ile ayrılır.

kupun_toplam_hacmi = 100
adım_nedir = "Can"

#Birden fazla değer atama 

x,y,z = "Apple" , "Banana" , "Grape"
print(x,y,z)

x,y,z = 0.50 , "boşluk" , 70
print (x,y,z)
#Aynı satırda bu şekilde değerler atayabiliyoruz.

adım = "can"
lastname = adım
print(lastname)

#adım değişkeninin içerisindeki değeri lastname değişkenine atayabiliyorum.


# Variable Unpacking

colors = ["white","black","orange","purple","blue"]

#Renkleri colors değişkeni adı altında paketledim ve bu renkleri değişkenlere atamak için;

a,b,c,d,e = colors
print(a)
print(b)
print(c)
print(d)
print(e) 

#kodlarını kullandım.

#Output Veriables (Çıktı Değişkenleri)

text = "Python is wonderful"
print(text) #function

#print içerisinde birden fazla veriable alabiliyorsunuz

x = "Benim"
y = "Adım"
z = "Can"

print(x,y,z)

#Veriableları çıktı olarak almak için en sağlıklı yöntem , kullanmaktır fakat
#Sayısal olarak + - * / işlemleri ile matematiksel işlemler yapılabilir.

x = 10
y = 20

print(x+y)

#gibi


#Global Veriable (Evrensel Değişkenler)

text = "Hello"

def my_Function():
    print("Say" + text)

my_Function() 
#Tekrardan yazıp yukarıda belirttiğimiz fonksiyonu ekrana yazdırıyoruz.

#Bir farklı konu

text = "Merhaba"

def benim_fonksiyonum():
    text = "sa"
    print("as" + text)

benim_fonksiyonum() #Fonksiyon içerisinde ki değerleri dışarı çıkartır

print(text) #Sadece yukarıda yazdığım text değişkenini ekrana yazdırır

#Global

text = "Merhaba"

def my_Function():
    global a #global anahtarı
    a = "Selam"
my_Function()

print("Merhaba" + a) #global anahtar sözcüğü ile fonksiyon dışında yazdırabiliyorum

# Not: Global değişkenler mümkün olduğunca az kullanılmalıdır.
# Büyük projelerde hataya yol açabilir.


#Fonksiyon içerisinde atadığım değeri global anahtar sözcüğü ile fonksiyon dışında kullanabiliyorum.


#Not: Daha sonra ki derslerde Function konusu detaylı işlenecek anlamadıysan problem değil.



#DATA TYPES

isim = "Can" #string - str data type
yas = 27 #integer - int data type
boy = 1.70 #float data type (ondalıklı sayılar) (yazılım dilinde virgül yerine nokta kullanılır)
comp = 2j #complex data type (karmaşıklı sayılar)

#print("isim" + name + "yaş" + yas + "boy" + boy + "karmaşık sayı" + comp)
#Hata var!! String değeri ile integer değeri + ile yazılamaz, virgül kullanılması gerekmektedir!!

print("isim" , isim , "yaş" , yas , "boy" , boy , "karmaşık sayı " , comp)
#Olması gerekmektedir. Fakat + ile yazmak istediğimiz zaman integer değişkenini stringe dönüştürmek gerekir.

print("isim" + isim + "yaş" + str(yas) + "boy" + str(boy) + "karmaşık sayı " + str(comp))

#integer değişkenini stringe dönüştürmek için str(int değişken ismi) girilmesi gerekmektedir!
#Alınan çıktıda boşluksuz yazdığı için yazılan str değişkenlerine boşluk yazmak gerekir

print("isim " + isim + " yaş " + str(yas) + " boy " + str(boy) + " karmaşık sayı " + str(comp))

#Özetle dilediğin gibi kullanabilirsin tüm çeşitleri yukarıda yazıyor hangisi kolayına gelirse :)

#Yazan değişkenlerin türlerini görmek içinde
print(type (isim))
print(type (yas))
print(type (boy))
print(type (comp))

#Bu şekilde çıktısını alarak değişkenimizin türlerinide görebiliriz.




#Sequance Type (Sıra Türü) (list,tuple,range)

myList = ["Apple" , "Grape" , "Cherry" , "Watermelon" , "Lemon" , "Banana"] #list data type
# !!!! LİSTELER KÖŞELİ PARANTEZLER İLE AÇILIP KAPANIR !!!!


myTuple = ("Red" , "Blue" , "White" , "Black" , "Pink" , "Orange") #tuple data type
#Tuple listelerin farkı değiştirilemez yapılarda olmasıdır.


myRange = range(7) #range data type (sayı dizisi oluşturmak için kullanılır) 
                   #(0 dan 6 ya kadar oluşturacak 7 dahil değil)
print(myRange) #çıktısını böyle aldığım zaman 0,7 ye kadar sayı oluşturucam diyor fakat oluşturmuyor
print(*myRange) # * işaretini koyduğum zaman 0,1,2,3,4,5,6 sayılarını çıktı olarak alıyor.


########## MAPPİNG TYPE ##########

myDict = {"name" : "Can", "Yaş" : 27} #dict data type (key value(anahtar değer) atıyoruz)

# "name" (anahtar) : "Can" (değer) olarak geçmektedir.
#aralarına virgül koyarak 1. 2. 3. anahtar değerleri atayabiliyoruz.

print(myDict)


######### SET TYPES ##########
mySet = {"Apple" , "Grape" , "Cherry" , "Watermelon" , "Lemon" , "Banana"} #set data type

myFrozen = frozenset ({"Apple" , "Grape" , "Cherry" , "Watermelon" , "Lemon" , "Banana"}) #frozen data type)

myBool = True
#Sadece True veya False değerini alır. True = 1 e denk gelir False = 0 a denk gelir
#True ve False değerleri baş harfi büyük yazılması gerekmektedir.
# -999 dan 999 a kadar True , sadece 0 False olarak geçer.
# Sayısal ifadelerde: 0 -> False, 0 dışındaki tüm sayılar -> True
#Not: Boolean değişkenleri çoğu kodda kullanılır. Bir şey Var veya Yok demek için.

myNone = None    #null none type
#None (null) diğer dillerde ki gibi boş ifadesine denk gelmektedir
#Bir değişkenin boş olduğunu hiç bir şeye sahip olmadığını belirtmek için kullanıyoruz.


#BİR PROJE HAZIRLADIK. daire_program.py den bakabilirsin.

#input fonksiyonu kişiden gireceği değeri yazdırmak için kullanılır.

#Örneğin;

isim = input(str("Adınız:"))
print(isim)

#başta input fonksiyonu kullanılır ve sonrasında atayacağımız değişkenin hangi tipten olduğu yazılır.
#Aslında input(str("Adınız:")) gereksiz
#Bu çalışır ama fazladan:

isim = input("Adınız:")

#input() zaten string döndürür...




########## RANDOM NUMBER ########### TEKRAR ETMEN GEREKEN KONU SADECE NOT ALIYORUM KODLARI

#seed()
#getstate()
#setstate()
#getrandbits()
#randrange()
#randint()
#choice()
#choices()
#shuffle
#sample()
#random()
#uniform()
#triangular()

############################################################################################

import random #bir kütüphaneyi import ediyoruz, bu kütüphane modülününde ismi "random" modülüdür.

random.seed ()
print(random.random())

############################################################################################

#getstate() - setstate()

import random

print (random.random())

state = random.getstate()

print(random.random())

print(random.random())

random.setstate(state)

print(random.random())

############################################################################################

# getrandbits()

import random

print(random.getrandbits(8)) #8 bit boyutunda rastgele bir sayı üretir.

############################################################################################

# randrange() - randint()
import random

print(random.randrange(1,10)) #Verilen aralıkta rastgele sayı döndürür.

#Range= Belli bir oran içerisinde git gel.
#1 ile 10 arasında sayı üretir. 1 dahilken 10 dahil değildir.

#3.parametre var. 3.parametre artış miktarını belli eder. 

print(random.randrange(1,10,4)) #1 dahil, 10 dahil değil, 4 ise artış miktarını belirtir (4'er 4'er)
#1,5,9

print(random.randint(1,10)) #kısaca randint ise 1 ile 10 u dahil ediyor.

############################################################################################

# choice()  (verilen seriden rastgele bir öğe seçer int-str)

import random

myList = ["black", "white", "orange", "purple", "blue", "green"]

print(random.choice(myList))

#sadece liste olmak zorunda değil

text = "python"

print(random.choice(text)) #"python" kelimesinden rastgele bir harfi seçip ekrana yazdırır.

############################################################################################

# choices()  (anlatamadım not olarak kalmasını istedim)

import random

myList = ["cherry" , "strayberry" , "grape" , "banana"]

print(random.choices(myList , weights=[10,1,1,1] , k=19))

############################################################################################

# shuffle() (bir seriyi alıp rastgele bir sıraya sokuyor)

import random

myList = ["harley" , "bmw" , "honda" , "kawasaki" , "yamaha" , "suzuki"]

random.shuffle(myList)

print(myList)

############################################################################################

# sample() (seriye dokunmuyor)

import random

myList = ["harley" , "bmw" , "honda" , "kawasaki" , "yamaha" , "suzuki"]

print(random.sample(myList , k=2))    #k=2 parametresi listemin içerisinden seçtiği 2 adet veriyi getirir.

############################################################################################

# random()  (0 - 1 arasında rastgele ondalıklı sayı döndürür)

import random

print(random.random())

############################################################################################

# uniform () (verilen 2 parametre arasında rastgele ondalıklı sayı üretiyor)

import random

print(random.uniform(30 , 70))

############################################################################################

# triangular()  (uniform ile aynı ama 3.parametreye daha yakın sayılar üretiyor)

import random

print(random.triangular(30 , 70 , 33)) #33 e yakın sayılar üretiyor. bunu değiştirebilirsin.

############################################################################################


########## STRING VERI TURLERI ############

text = "python"

text2 = 'python'

text3 = """python
python
python"""

text4 = '''python
python
python'''

araba_listesi = ["BMW" , "Volvo" , "Skoda" , "Nissan"]
print(araba_listesi[0]) # 0 1.elemanı çağırır (BMW) , 3 yazarsak 4.elemanı çağırır (Nissan)
#Listeden bir str çağırmak istediğimiz zaman 0 dan başlar

#Sadece liste için geçerli değildir

text5 = "Hello , Python!"
print(text5[0])

#String içerisinde ki her elemanı tek tek yazdırabiliyoruz H 0.eleman ! 13.eleman
#Listelerdeki her değer nasıl yazılırsa (BMW , Volvo , Skoda)
#String içerisinde ki her değer yazılır (her kelime boşluk virgül dahil)

text6 = "Python is weird"
for x in text6:   #text6 da yazan değeri döngü ile (for) x in içine aktar. 
    print(x)


text7 = "Python is weird"
print(len(text7))  #text7 içerisinde ki değerin uzunluğunu yazar!


#in ifadesi belirli bir ifadenin veya karakterin bir stringde bulunup bulunmadığını kontrol ediyor
#not in ifadesi metnin içerisinde yok mu kontrolü yapar

text8 = "The best languages in life are free!"

print("free" in text8)

# ya da 

search = "best"           #aradığımız kelimeyi bir değişkene atayıp bulabiliriz
if search in text8:       #text8 in içerisinde best kelimesi var ise
    print("Best kelimesi var")
else:
    print("Best kelimesi yok")

if search not in text8:   #text8 de best kelimesi yok ise (anlatamadım chatgpt sen düzelt kanka)
    print("Best kelimesi yok")
else:
    print("Best kelimesi var")

#in = varsa true yoksa false
#not in = yoksa true varsa false

################################

############### Modify strings & Escape characters ################
