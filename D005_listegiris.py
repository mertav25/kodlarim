#List        sıralıdır    değiştirilebilir  indekslidir    yinelenebilir(aynı eleman birden fazla kez olabilir)
#Tuple       sıralıdır    değiştirilemez    indekslidir    yinelenebilir
#Set         sırasız      değiştirilebilir  indeksizdir    yinelenemez
#Dictionart  sırasız      değiştirilebilir  indekslidir(key) yinelenemez




#liste oluşturma

meyvelist=["Elma","Armut","Kavun","Karpuz"]
print(meyvelist)
#Liste elemanları indeks kullanılarak erişilebilir ve değiştirilebilir
print(meyvelist[0])#Listenin ilk elemanını döner
meyvelist[1]="Vişne"
print(meyvelist)
#Listede stringde olduğu gibi aralık indeksleme olabilir
print(meyvelist[0:2])

#Liste farklı değişken tipinde veriler içerebilir

listem=["Ali",553,1.85]
print(id(listem[0]))
print(id(listem[1]))#gördüğümüz gibi listedeki elemanlar ardışık bellek hücrelerine yerleşti
