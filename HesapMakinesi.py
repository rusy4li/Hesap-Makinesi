# -*- coding:utf-8 -*-
# Gelişmiş Hesap Makinesi
import time
import os


def dikdortgen(dikdörütü):
    artirma = 0
    a = 0
    while artirma == a:
        if dikdörütü.lower() == "alan":
            print(">>> Uzun Kenar")
            uzunkenar = int(input("-> "))
            print(">>> Kısa Kenar")
            kısakenar = int(input("-> "))
            alan = uzunkenar * kısakenar
            print(">>> Alan: {}".format(alan))
            artirma += 1
        elif dikdörütü.lower() == "çevre" or dikdörütü.lower() == "cevre":
            print(">>> Uzun Kenar")
            uzunkenar = int(input("-> "))
            print(">>> Kısa Kenar")
            kısakenar = int(input("-> "))
            cevre = uzunkenar + kısakenar
            cevre *= 2
            print(">>> Çevre: {}".format(cevre))
            artirma += 1
        else:
            print(">>> Doğru sayı girdiğinizden emin olunuz lütfen!")
            print()


print("""#############################
##                         ##
##     =[HesapMakinesi]=   ##
##   ~[rusy4li]~           ##
##                         ##
#############################""")
print()
print(">>> help! yazarak yapabileceğiniz hesaplamaları görebilirsiniz :)")
print(">>> Çıkmak için ex! yazabilirsiniz!")
print()
print(">>> Ne tür bir işlem yapmak istiyorsunuz?")
while True:
    sorgu = input("-> ")
    if sorgu.lower() == "toplama":
        print()
        artirma = 0
        a = 0
        while artirma == a:
            try:
                print(">>> 1. Sayı")
                sayi1 = int(input("-> "))
                print(">>> 2. Sayı")
                sayi2 = int(input("-> "))
                toplam = sayi1 + sayi2
                # 31 Vakası
                if toplam == 31:
                    print(">>>", toplam, "Sjbsjbvjkasbdvjka")
                    artirma += 1
                else:
                    print(">>> Sonuç:", toplam)
                    artirma += 1
            except ValueError:
                print(">>> Lütfen Doğru Sayı Giriniz!")
                print()
    elif sorgu.lower() == "çıkarma":
        print()
        artirma = 0
        a = 0
        while artirma == a:
            try:
                print(">>> 1. Sayı")
                sayi1 = int(input("-> "))
                print(">>> 2. Sayı")
                sayi2 = int(input("-> "))
                cıkar = sayi1 - sayi2
                # 31 Vakası
                if cıkar == 31:
                    print(">>>", cıkar, "Sjbsjbvjkasbdvjka")
                    artirma += 1
                else:
                    print(">>> Sonuç:", cıkar)
                    artirma += 1
            except ValueError:
                print(">>> Lütfen Doğru Sayı Giriniz!")
                print()
    elif sorgu.lower() == "bölme":
        print()
        artirma = 0
        a = 0
        while artirma == a:
            try:
                print(">>> 1. Sayı")
                sayi1 = int(input("-> "))
                print(">>> 2. Sayı")
                sayi2 = int(input("-> "))
                bolme = sayi1/sayi2
                # 31 Vakası
                if bolme == 31:
                    print(">>>", bolme, "Sjbsjbvjkasbdvjka")
                    artirma += 1
                else:
                    print(">>> Sonuç:", bolme)
                    artirma += 1
            except ValueError:
                print(">>> Lütfen Doğru Sayı Giriniz!")
                print()
    elif sorgu.lower() == "çarpma":
        print()
        artirma = 0
        a = 0
        while artirma == a:
            try:
                print()
                print(">>> 1. Sayı")
                sayi1 = int(input("-> "))
                print(">>> 2. Sayı")
                sayi2 = int(input("-> "))
                carpma = sayi1*sayi2
                # 31 Vakası
                if carpma == 31:
                    print(">>>", carpma, "Sjbsjbvjkasbdvjka")
                    artirma += 1
                else:
                    print(">>> Sonuç:", carpma)
                    artirma += 1
            except ValueError:
                print(">>> Lütfen Doğru Sayı Giriniz!")
                print()
    elif sorgu.lower() == "faktöriyel":
        print()
        artirma = 0
        a = 0
        while artirma == a:
            try:
                print(">>> Faktöriyelini Hesaplamak istediğiniz sayı?")
                faktoriyel = 1
                sayi = int(input("-> "))
                for i in range(1, sayi + 1):
                    faktoriyel *= i
                print(">>> Faktöriyel", faktoriyel)
                artirma += 1
            except ZeroDivisionError:
                print(">>> Negatif Olmayan Bir Sayı Giriniz Lütfen!")
                print()
            except:
                print(">>> Lütfen Doğru Sayı Giriniz!")
                print()
    elif sorgu.lower() == "dikdörtgen":
        print()
        print(">>> Dikdörtgenin Alanını mı Yoksa Çevresini mi Hesaplamak İstiyorsunuz")
        dikdorutu = str(input("-> "))
        dikdortgen(dikdorutu)
    elif sorgu.lower() == "ex" or sorgu.lower() == "exit":
        print()
        print(">>> Kapatılıyor...")
        time.sleep(0.5)
        print(exit())
    elif sorgu.lower() == "cls":
        os.system("cls")
    elif sorgu.lower() == "help" or sorgu.lower() == "'help'" or sorgu.lower() == "help!":
        print()
        print(">>> Toplama = 2 farklı sayı kullanarak toplama işlemi yapabilirsiniz.\nçıkarma = 2 farklı sayı kullanarak çıkarma işlemi yapabilirsiniz.\nbölme = 2 farklı sayı kullanarak bölme işlemi yapabilirsiniz.\nçarpma = 2 farklı sayı kullanarak çarpma işlemi yapabilirsiniz.\nfaktöriyel = negatif olmayan bir sayı girerek faktöriyel hesaplama yapabilirsiniz.\ndikdörtgen = dikdörtgenin uzun ve kısa kenarlarını kullanarak alan ve çevre hesaplaması yapabilirsiniz.")
    else:
        print(">>> Sadece sayı kullanarak işlem yapabilirsiniz! Ve 'help' yazarak yapabileceğiniz tüm hesaplamaları görebilirsiniz!")
        print()
    print()
    print(">>> Başka hangi işlemi yapmak istiyorsunuz?")
