import random
karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
uzunluk = int(input("parolanızın uzunluğunu belirleyiniz :"))

sifre = ""
for i in range(uzunluk):
    sifre += random.choice(karakterler)
    print(sifre)

print(sifre)
