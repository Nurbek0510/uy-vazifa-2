n = int(input("Talabalar soni: "))

with open("talabalar.txt", "w", encoding="utf-8") as fayl:
    for i in range(n):
        malumot = input().split()

        ism = malumot[0]
        yosh = malumot[1]
        ball = malumot[2]

        fayl.write(ism + " " + yosh + " " + ball + "\n")