name = input("İsim girin: ")
prize = ["Altın" , "Gümüş" , "Bronz" , "Boş Sandık"]
gold = [100 , 200 , 300, 400]
import random
print (name , "sandığı açtı!")
print ("Ödül: " , random.choice(prize))
print ("Kazandığın para: " , random.choice(gold))