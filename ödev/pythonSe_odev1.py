ilerlemeDurumu=0
sayac=int(input("Sayacı giriniz->"))
for i in range(0,sayac):
    ilerlemeDurumu+=1   
    if ilerlemeDurumu==1:
        print("Ders Programı kısmıdır."+" %25 tamamlandı.")
    elif ilerlemeDurumu==2:
        print("Değerlendirme kısmıdır."+" %50 tamamlandı." )
    elif ilerlemeDurumu==3:
        print("Ödev1 kısmıdır."+" %75 tamamlandı." )
    elif ilerlemeDurumu==4:
        print("Ödev2 kısmıdır."+" %100 tamamlandı." )
    else:
         print("Aşama kalmadı.")