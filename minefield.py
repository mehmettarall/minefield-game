import random
import os   #Ekran temizleme icin.
skor = 0
def tabloOlustur(boyut):
    tablo = list()
    for eleman in range(0,pow(boyut,2)):
        tablo.append('?')
    tahminTablosu = tablo.copy()
    

    mayinSayisi = pow(boyut, 2) * 0.3
    mayinSayisi = int(mayinSayisi)
    for mayin in range(mayinSayisi):
        while(True):

            konum = random.randint(0,boyut**2-1)                
            if(tablo[konum] == 'X'):
                pass
            else:
                tablo[konum] = 'X'
                break
    matris(tahminTablosu, boyut)
    tahminSirasi(tablo, tahminTablosu, boyut,mayinSayisi,skor)

def matris(matris,oyun_boyutu):
    sayac = 0 
    sayac1 = 1
    while sayac <oyun_boyutu*oyun_boyutu:
        if sayac1 == oyun_boyutu:
            sayac1=0
            print(matris[sayac],end=" \t")
            print("\n")
        else:
            print(matris[sayac],end=" \t")
        sayac=sayac+1
        sayac1=sayac1+1
    print("\n")

def tahminSirasi(tablo,tahminTablosu,boyut,mayinSayisi,skor):
    while(True):
        mod = input("Acik Mod = A \nNormal Mod = N : ")
        if(mod == 'a' or mod == 'A'):
            matris(tablo, boyut)
            tahminSirasi(tablo, tahminTablosu, boyut, mayinSayisi,skor)
            break
        elif(mod == "n" or mod == "N" ):
            pass

        tahminX = int(input("X degeri = "))
        tahminY = int(input("Y degeri = "))
        
        lokasyon = (tahminX - 1) + (boyut*(tahminY-1))
        if (tablo[lokasyon] == 'X'):
            matris(tablo, boyut)
            print("Patladiniz")
            print("skorunuz =",skor)
            print("\n")
            break
        else:
            if(skor < (boyut*boyut)- mayinSayisi):
                cevrem = 0
                if(lokasyon >= 2 and lokasyon < boyut):
                    if(tablo[lokasyon - 1] == 'X'):
                        cevrem +=1
                    if(tablo[lokasyon + 1] == 'X'):
                        cevrem +=1
                    if(tablo[lokasyon +boyut - 1] == 'X'):
                        cevrem +=1
                    if(tablo[lokasyon +boyut] == 'X'):
                        cevrem +=1
                    if(tablo[lokasyon + boyut + 1] == 'X'):
                        cevrem +=1
                elif(lokasyon >= boyut*(tahminY-1)+2 and lokasyon < boyut*(tahminY-1)+(boyut - 1 )):
                    if(tablo[lokasyon - boyut -1 ] == 'X'):
                        cevrem +=1
                    if(tablo[lokasyon - boyut  ] == 'X'):
                        cevrem +=1
                    if(tablo[lokasyon - boyut +1 ] == 'X'):
                        cevrem +=1
                    if(tablo[lokasyon  -1 ] == 'X'):
                        cevrem +=1
                    if(tablo[lokasyon +1 ] == 'X'):
                        cevrem +=1
                elif(lokasyon >= boyut*2 and lokasyon < boyut*(boyut-1)):
                    if(tablo[lokasyon-boyut-1] == 'X'):
                        cevrem +=1
                    if(tablo[lokasyon-boyut] == 'X'):
                        cevrem +=1
                    if(tablo[lokasyon -1] == 'X'):
                        cevrem +=1
                    if(tablo[lokasyon +boyut-1] == 'X'):
                        cevrem +=1
                    if(tablo[lokasyon +boyut] == 'X'):
                        cevrem +=1

                elif(lokasyon >=boyut+1 and lokasyon < boyut*(boyut-1)+1):
                    if(tablo[lokasyon - boyut] == 'X'):
                        cevrem +=1
                    if(tablo[lokasyon - boyut +1] == 'X'):
                        cevrem +=1
                    if(tablo[lokasyon +1] == 'X'):
                        cevrem +=1
                    if(tablo[lokasyon + boyut] == 'X'):
                        cevrem +=1
                    if(tablo[lokasyon + boyut +1] == 'X'):
                        cevrem +=1
                
                elif(lokasyon == 1):
                    if(tablo[lokasyon +1] == 'X'):
                        cevrem +=1
                    if(tablo[lokasyon +boyut] == 'X'):
                        cevrem +=1
                    if(tablo[lokasyon + boyut +1] == 'X'):
                        cevrem +=1
                elif(lokasyon == boyut):
                    if(tablo[lokasyon-1] == 'X'):
                        cevrem +=1
                    if(tablo[lokasyon + boyut -1] == 'X'):
                        cevrem +=1
                    if(tablo[lokasyon+boyut] == 'X'):
                        cevrem +=1
                elif(lokasyon == boyut*(tahminY-1)+1):
                    if(tablo[lokasyon-boyut] == 'X'):
                        cevrem +=1
                    if(tablo[lokasyon-boyut +1] == 'X'):
                        cevrem +=1
                    if(tablo[lokasyon+1] == 'X'):
                        cevrem +=1
                elif(lokasyon == (boyut*boyut)-1):
                    if(tablo[lokasyon -boyut -1] == 'X'):
                        cevrem +=1
                    if(tablo[lokasyon -boyut ] == 'X'):
                        cevrem +=1
                    if(tablo[lokasyon -1] == 'X'):
                        cevrem +=1
                else:

                    if(tablo[lokasyon -boyut-1] == 'X'):
                        cevrem = cevrem + 1
                    if(tablo[lokasyon -boyut] == 'X'):
                        cevrem = cevrem + 1
                    if(tablo[lokasyon -boyut +1] == 'X'):
                        cevrem = cevrem + 1
                    if(tablo[lokasyon -1] == 'X'):
                        cevrem = cevrem + 1
                    if(tablo[lokasyon +1] == 'X'):
                        cevrem = cevrem + 1
                    if(tablo[lokasyon +boyut-1] == 'X'):
                        cevrem = cevrem + 1
                    if(tablo[lokasyon +boyut] == 'X'):
                        cevrem = cevrem + 1
                    if(tablo[lokasyon +boyut+1] == 'X'):
                        cevrem = cevrem + 1
            
               
        
                tahminTablosu[lokasyon] = cevrem
                skor = skor + 1
                matris(tahminTablosu, boyut)
            else:
                print("Tebrikler Kazandiniz skorunuz: ", skor)
        os.system('cls')
        matris(tahminTablosu,boyut)
            


def menu ():
    while(True):
        print("Yeni Bir Oyuna Başlamak İçin -1- Yazınız")
        print("Çıkmak İçin -2- Yazınız")
        secim = input("Seçiminiz: ")
        if(secim == "1"):
            boyut = int(input("Oyun boyutu: "))
            if boyut < 10 :
                print("Oyun Boyutu 10'dan küçük olamaz")
                return menu()
            else:
                pass

            tabloOlustur(boyut)
        elif(secim == "2"):
            return 0
        else:
            print("Yanlış seçim yaptınız lütfen tekrar deneyiniz: ")
            menu()

menu()


