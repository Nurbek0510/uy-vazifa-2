ism = input("Ism: ")
yosh = input("Yosh: ")
ball = input("Ball: ")

with open("talaba.txt", "w", encoding="utf-8") as fayl:
    fayl.write(ism + "\n")
    fayl.write(yosh + "\n")
    fayl.write(ball)