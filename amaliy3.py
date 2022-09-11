######AMALIYOT3#######
#SAVOL
#Pythonda quyidagi o'zgaruvchilarni yaratin:

#JAVOB
street = "Bog'bon"
streettest = "Sag'bon"
shtaat = "Bodomzor"
city = "Samarqand"

print(street, streettest, shtaat, city)

#SAVOL
#Yuqoridagi o'zgaruvchilarning qiymatini foydalanuvchidan so'rang. Va avvalgi mashqni takrorlang. 

#JAVOB

street = input("Ko'changizni nomini kiriting")
streettest = input("Mahallangizni nomini kiriting")
shtaat = input("Tumaningizni nomini kiriting")
city = input("Viloyatingizni nomini kiriting")
print(street, streettest, shtaat, city)


#SAVOL
#Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi satrdan yozing.

#JAVOB
street = "Bog'bon\n"
streettest = "Sag'bon\n"
shtaat = "Bodomzor\n"
city = "Samarqand"

print(street, streettest, shtaat, city)

#SAVOL
#Yuqoridagi matnni f-string yordamida yangi, manzil deb nomlangan o'zgaruvchiga yuklang. 

manzil = f"{street}, {streettest}, {shtaat}, {city}"
print(manzil)

#SAVOL 
#manzil o'zgaruvchisiga yuqorida biz o'rgangan title(), upper(), lower(), capitalize() metodlarini qo'llab ko'ring.

#JAVOB
manzil = f"{street.title()}, {streettest.upper()}, {shtaat.lower()}, {city.capitalize()}"
print(manzil)