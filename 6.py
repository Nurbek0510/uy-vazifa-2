malumot = input("Ism, yosh va ballni kiriting: ").split()

ism = malumot[0]
yosh = malumot[1]
ball = malumot[2]

with open("talabalar.txt", "a", encoding="utf-8") as fayl:
    fayl.write(ism + " " + yosh + " " + ball + "\n")