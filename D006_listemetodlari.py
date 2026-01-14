

meyvelistesi=["elma","armut","kivi","kavun","karpuz"]
#print(meyvelistesi.count("armut"))#Verilen elemanın kaç defa tekrarladığını tespit eder.
#meyvelistesi.append("portakal")#Listenin sonuna eleman ekler
#print(meyvelistesi)
#meyvelistesi.insert(1,"çilek")#Belirtilen indekse eleman ekler.
#print(meyvelistesi)
#meyvelistesi.clear()#meyve listesini temizler ancak listeyi silmez
#print(meyvelistesi)
#del meyvelistesi  #meyve listesini direk ortadan kaldırır
#print(meyvelistesi)
#print(len(meyvelistesi))#listede kaç eleman olduğunu verir
#meyvelistesi.extend(["muz","avakado"])#listeye birden fazla eleman ekler
#print(meyvelistesi)

#del meyvelistesi[1]#verilen indekse göre silme yapar
#print(meyvelistesi)
#meyvelistesi.remove("elma")#Eğer elemanın indeksini bilmiyorsak bu metodu kullanırız
#print(meyvelistesi)
#silinecekmeyve=meyvelistesi.pop(0)#indeksi verilen elemanı siler ama onu bir değişkenen atmamı sağlar
#print(f"{silinecekmeyve} silindi")
#print(meyvelistesi)

#meyvelistesiyedek=meyvelistesi.copy()
#print(meyvelistesiyedek)
#print(id(meyvelistesiyedek))
#print(id(meyvelistesi))#Gördüğümüz gibi adresleri farklı çünkü sadece içindeki verileri kopyalar

#print(meyvelistesi.index("armut"))#Verilen elemanın ilk bulunduğu indeksi verir
#meyvelistesi.sort()#listeyi sıralar
#print(meyvelistesi)
"""sorted(meyvelistesi) #yerel parametre olarak aldığı listenin kopyasını sıralar ancak listenin referansında
değişim yapmaz o yüzden başka liste döner bunu yakalayıp ayrı bir listeye atamamız lazım"""
#print(meyvelistesi)
#meyvelistesi.reverse() #listeyi ters çevirir
#print(meyvelistesi)
