#int ve float olmak üzere 2 tane sayısal değişken tipi vardır.int tam sayı tutar.float ise ondalık sayı tutar
intsayi=25
floatsayi=14.25
print(type(intsayi))#tipini döndüren fonksiyon (type)
print(type(floatsayi))

sayi1=25
sayi2=14
sonuc=sayi1+sayi2
sonuc=sayi1-sayi2
sonuc=sayi1/sayi2
print(type(sonuc))#bölme işleminin sonucu Pythonda her zaman float çıkar
sonuc=sayi1//sayi2 #tam bölme işlemidir
print(type(sonuc))
print(sonuc)
sonuc=sayi1%sayi2 #mod alma işlemi
print(sonuc)
sonuc=sayi1**sayi2
print(sonuc)

#işlem önceliği

islem=5**5/25+4 #Matematikteki işlem önceliği aynen geçerlidir
print(islem)
#Adres meselesi

#Pythonda sayısal ifadelerde her değer aslında farklı bir nesne tutar
sayia=15
sayib=15
sayic=5.155
print(id(sayia),id(sayib))#Aynı adresleri tutar.Çünkü pythonda her değer bir nesne oluşturur.Aynı değer ise aynı nesnedir
print(id(5.155),id(sayic))#Aynı adres
