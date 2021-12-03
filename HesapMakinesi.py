# -*- coding:utf-8 -*-
# Hoşgeldiniz Bu Program rusy4 Adlı GitHub Kullanıcısı Tarafından Kodlanmıştır!
# Gelişmiş Hesap Makinesi :)
import time
print("""#############################
##                         ##
##     =[HesapMakinesi]=   ##
##   ~[rusy4li]~           ##
##                         ##
#############################""")
print("'help' yazarak yapabileceğiniz hesaplamaları görebilirsiniz :)")
print("Çıkmak için 'ex' yazabilirsiniz!")
while True:
    print("Ne tür bir işlem yapmak istiyorsunuz?")
    sorgu = input("->> ")
    if sorgu.lower() == "toplama":
        sayi1 = int(input("Sayı(1)-->"))
        sayi2 = int(input("Sayı(2)-->"))
        toplam = (sayi1 + sayi2)
        # 31 Vakası
        if toplam == int("31"):
            print(toplam, "Sjbsjbvjkasbdvjka")
        else:
            print("Sonuç:", toplam)
    if sorgu.lower() == "çıkarma":
        sayi1 = int(input("Sayı(1)-->"))
        sayi2 = int(input("Sayı(2)-->"))
        cıkar = (sayi1 - sayi2)
        # 31 Vakası
        if cıkar == int("31"):
            print(cıkar, "Sjbsjbvjkasbdvjka")
        else:
            print("Sonuç:", cıkar)
    if sorgu.lower() == "bölme":
        sayi1 = int(input("Sayı(1)-->"))
        sayi2 = int(input("Sayı(2)-->"))
        bolme = (sayi1/sayi2)
        # 31 Vakası
        if bolme == int("31"):
            print(bolme, "Sjbsjbvjkasbdvjka")
        else:
            print("Sonuç:", bolme)
    if sorgu.lower() == "çarpma":
        sayi1 = int(input("Sayı(1)-->"))
        sayi2 = int(input("Sayı(2)-->"))
        carpma = (sayi1*sayi2)
        # 31 Vakası
        if carpma == int("31"):
            print(carpma, "Sjbsjbvjkasbdvjka")
        else:
            print("Sonuç:", carpma)
    if sorgu.lower() == "faktöriyel":
        faktoriyel = 1
        sayi = int(input("Lütfen negatif olamayan bir sayı giriniz:"))
        if (sayi <= 0):
            print("Lütfen negatif olmayan bir sayı giriniz.")
            continue
        else:
            for i in range(1, sayi + 1):
                faktoriyel *= i
            else:
                print("Faktöriyel", faktoriyel)
    if sorgu.lower() == "dikdörtgen":
        dikdörütü = str(input(
            "Dikdörtgenin Alanını mı Yoksa Çevresini mi Hesaplamak İstiyorsunuz:"))
        if dikdörütü.lower() == "alan":
            uzunkenar = input("Uzun Kenar:")
            kısakenar = input("Kısa Kenar:")
            alan = int(uzunkenar) * int(kısakenar)
            print("Alan: {}".format(alan))
        elif dikdörütü.lower() == str("çevre"):
            uzunkenar = input("Uzun Kenar:")
            kısakenar = input("Kısa Kenar:")
            cevre = 2 * (int(uzunkenar) + int(kısakenar))
            print("Çevre: {}".format(cevre))
    if sorgu.lower() == "ex":
        print(exit())
    if sorgu.lower() == "help":
        print("toplama = 2 farklı sayı kullanarak toplama işlemi yapabilirsiniz.\nçıkarma = 2 farklı sayı kullanarak çıkarma işlemi yapabilirsiniz.\nbölme = 2 farklı sayı kullanarak bölme işlemi yapabilirsiniz.\nçarpma = 2 farklı sayı kullanarak çarpma işlemi yapabilirsiniz.\nfaktöriyel = negatif olmayan bir sayı girerek faktöriyel hesaplama yapabilirsiniz.\ndikdörtgen = dikdörtgenin uzun ve kısa kenarlarını kullanarak alan ve çevre hesaplaması yapabilirsiniz.")
    elif sorgu.lower() == "'help'":
        print("toplama = 2 farklı sayı kullanarak toplama işlemi yapabilirsiniz.\nçıkarma = 2 farklı sayı kullanarak çıkarma işlemi yapabilirsiniz.\nbölme = 2 farklı sayı kullanarak bölme işlemi yapabilirsiniz.\nçarpma = 2 farklı sayı kullanarak çarpma işlemi yapabilirsiniz.\nfaktöriyel = negatif olmayan bir sayı girerek faktöriyel hesaplama yapabilirsiniz.\ndikdörtgen = dikdörtgenin uzun ve kısa kenarlarını kullanarak alan ve çevre hesaplaması yapabilirsiniz.")
    else:
        ("Sadece sayı kullanarak işlem yapabilirsiniz! Ve 'help' yazarak yapabileceğiniz tüm hesaplamaları görebilirsiniz!")
