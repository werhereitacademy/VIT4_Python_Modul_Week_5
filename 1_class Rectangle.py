class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

rectangle = Rectangle(5, 7)

print(f"Area of Rectangle: {rectangle.area()}")
print(f"Perimeter of Rectangle: {rectangle.perimeter()}")

"""Öğrencilerin Listede Tutulmasi:
Öğrencileri bir listede tutmak, her öğrencinin benzersiz bir isim veya kimlikle tanımlandığı ancak her öğrenciye ek özniteliklerin olmayabileceği durumlar için uygundur.
Listeler, öğelerin sıralı bir koleksiyonunu korumak ve bu koleksiyon üzerinde sıralı bir şekilde işlem yapmak istediğinizde uygun bir veri yapısıdır.
Bu durumda her öğrenci, listedeki bir sözlük içinde temsil edilir ve bu sayede her öğrencinin adı ve sınıfı gibi bilgilere kolayca erişilir.
Öğretmenlerin Sözlükte Tutulması:
Öğretmenleri bir sözlükte tutmak, her öğretmenin belirli bir konu ile ilişkilendirilmesi gerektiğinde uygun bir seçenektir.
Sözlükler, anahtarlar (öğretmen isimleri) temelinde hızlı bir arama sağlarlar. Bu, belirli bir öğretmenin öğrettiği konuyu hızlı bir şekilde almak gerektiğinde faydalı olabilir.
Eğer her öğretmene daha fazla öznitelik (iletişim bilgileri, bölüm vb.) eklemeyi bekliyorsanız, bir sözlük kullanmak sınıf yapısını değiştirmeden öğretmenin özniteliklerini genişletmeyi kolaylaştırır."""
