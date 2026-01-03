#listeler ileri seviye
#nested list

#liste içinde liste kullanabiliriz

ogrenciler=[[1,"Mert","Avcı"],[2,"Süleyman","Kural"],["3","Aleyna","Bitli"]]

print(ogrenciler[2])#listenin içindeki 3.listeyi çekeriz
print(ogrenciler[0][1])#listenin 1. elemanının içindeki listenin 2.elemanını çekeriz

#listelerde de stringlerde olduğu gibi dilimleme vardır

print(ogrenciler[:2])#ilk elemandan başla 3.elemana kadar

#listenin bellekteki yapısı
liste1=[1,2,5]
liste2=[0,5,8]
liste1=liste2
liste1.append(9)
print(liste1)
print(liste2)
#liste1 e liste2 yi atadım liste1 e eleman eklediğimde neden liste2 de değişti
#Çünkü liste1 asslında liste2nin adresini kendine kopyaladı ve liste1 de yaptığım bir değişiklik aynı nesneyi gören 2 nesnede değişecektir.
print(id(liste1))
print(id(liste2))#ikisinin de adresi aynı
