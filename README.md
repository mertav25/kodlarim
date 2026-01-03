# kodlarim

#listeler içerisinde birden fazla değişken barındıran koleksiyonlrdır.
#herbir değişkeni tek tek tanımlamak zahmetli olacağı için listeleri kullanırız.
#Listelerde farklı veri tiplerinde değişkenler bulunabilir


orneklistem=["Selim","Mert",15,16]

print(orneklistem)
print(orneklistem[0])#stringte olduğu gibi bunda da listenin indekslerine erişebilirim
orneklistem[1]="Ali" #listenin 2.elemanını değiştirdim
#Buradan ne anlıyoruz listeler mutable yapıdadır.
#listenin sonuna eleman eklemek için append metodunu kullanırız.
orneklistem.append("Süleyman")
print(orneklistem)#Süleyman ı ekledi
orneklistem.pop()#listenin son elemanını siler
print(orneklistem)
del orneklistem[0]#listenin ilk indeksli elemanını sildim
print(orneklistem)

#listeler pythonda toplanabilir

Asinifi=["Mehmet","Can","Onur"]
Bsinifi=["Aslı","Kemal","Yunus"]
Csinifi=Asinifi+Bsinifi

#Listeler sayıyla çarpılırsa  liste o kadar tekrarlanır

oyunsira=["Selim","Kemal","Yunus","Mustafa"]
print(oyunsira*2)

#örnek:alfabeyi oluşturunuz

sesliharfler=["a","e","ı","i","o","ö","u","ü"]
sesizharfler=["b","c","ç","d","f","g","ğ","h","j","k","l","m","n","p","r","s","ş","t","x","y","z"]
alfabe=sesliharfler+sesizharfler
print(alfabe)
alfabe.sort() #alfabeyi sıraladım
print(alfabe)

#listeye manuel eleman eklemek
sayilistem=[5,8]
sayilistem+=[7]
print(sayilistem)
#dikkat köşeli parantez ekleyerek kullanmak zorundayım yoksa hata verir sayilistem+7 hata verir
print(sayilistem.reverse())#listeyi ters çevirir






sayilistem=[5,8]
