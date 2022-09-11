######AMALIYOT3#######
#SAVOL
#Pythonda quyidagi o'zgaruvchilarni yaratin:

#JAVOB
kocha = "Bog'bon"
mahalla = "Sag'bon"
tuman = "Bodomzor"
viloyat = "Samarqand"

print(kocha, mahalla, tuman, viloyat)

#SAVOL
#Yuqoridagi o'zgaruvchilarning qiymatini foydalanuvchidan so'rang. Va avvalgi mashqni takrorlang. 

#JAVOB

kocha = input("Ko'changizni nomini kiriting")
mahalla = input("Mahallangizni nomini kiriting")
tuman = input("Tumaningizni nomini kiriting")
viloyat = input("Viloyatingizni nomini kiriting")
print(kocha, mahalla, tuman, viloyat)


#SAVOL
#Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi satrdan yozing.

#JAVOB
kocha = "Bog'bon\n"
mahalla = "Sag'bon\n"
tuman = "Bodomzor\n"
viloyat = "Samarqand"

print(kocha, mahalla, tuman, viloyat)

#SAVOL
#Yuqoridagi matnni f-string yordamida yangi, manzil deb nomlangan o'zgaruvchiga yuklang. 

manzil = f"{kocha}, {mahalla}, {tuman}, {viloyat}"
print(manzil)

#SAVOL 
#manzil o'zgaruvchisiga yuqorida biz o'rgangan title(), upper(), lower(), capitalize() metodlarini qo'llab ko'ring.

#JAVOB
manzil = f"{kocha.title()}, {mahalla.upper()}, {tuman.lower()}, {viloyat.capitalize()}"
print(manzil)