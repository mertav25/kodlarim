#sözlük key ve valuedan oluşur.key benzersiz olmak zorundadır.
#Neden sözlükler var daha hızlı hash yapıp değere ulaşmak için

#sözlük syntaxı
notlar={"Mert":100,"Ahmet":99,"Nisa":73,"Melisa":85}

print(notlar["Mert"])#hangi keyin valuesini öğrenmek istiyorsam onu yazarım
kalori_hesap={"koşmak":200,"yürümek":100,"yüzmek":150}
print(kalori_hesap["koşmak"])

#sozluk keyi liste olabilir mi?
#sozluk={["mert","ali"]:84} hata verir neden çünkü key hashable olmalı bundan dolayı değiştirilemez tipler alınır

sozluk={("mert","ali"):97}
print(sozluk[("mert","ali")])#bu oldu neden tupple immutable hashlenebilir
#mantıken düşünürsek liste değiştirilebilir ve listeye eleman eklense o keye artık o değerlerle ulaşılmaz

#sözlüğün valueları ayrı tip olabilir

sozluk2={"key1":5155,"key2":"yağmur"}

#sözlüğün keyleri de ayrı tip olabilir

sozluk3={"isim":"Mert","Soyisim":"Avcı",20:30}
print(sozluk3)


#sözlüğün içinde sözlük tanımı

mertbilgi={"isim":"Mert","soyisim":"Avcı","aldiginotlar":{"Sınav1":100,"Sınav2":85,"Sınav3":55}}
print(mertbilgi["aldiginotlar"]["Sınav1"])#listelerde olduğu gibi burada da bu şekilde iç indekslere ulaşabiliriz.


#sözlük değiştirilebilir bir yapıdır

filmler={"Mullholland":120,"Kitap":250}

filmler["Kitap"]=240
print(filmler)
#sozlüğe eleman ekleme
filmler["Yeni Film"]=220#direk key ve value belirterek sözlüğe eleman ekleyebiliriiz.
print(filmler)
