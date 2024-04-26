# 1. soru class ile alan ve cevre hesapla
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)


x1 = Rectangle(9, 5)


print( x1.area())
print("Dikdörtgenin Çevresi:", x1.perimeter())

# 2.soru

class School:

    school_name = "Anadolu Lisesi"
    establishment_year = 2001 

    students = []
    teachers = {}



    def add_new_student(self, student_name, student_class):
        self.students.append({"Name": student_name, "Class": student_class})


    def add_new_teacher(self, teacher_name, subject):
        self.teachers[teacher_name] = subject


    def display_students_list(self):
        print(self.students)

    
    def display_teachers_list(self):
        print(self.teachers)

    
my_school = School()

my_school.add_new_student("Mehmet Kaya", 11)
my_school.add_new_student("Ali Demir", 11)
my_school.add_new_student("Muftafa Kar", 11)

my_school.add_new_teacher("Mahmut Can", "Bioligy")
my_school.add_new_teacher("Huseyin Yilmaz", "Math")
my_school.add_new_teacher("Ibrahim Tosun", "Physics")
print("\n\n")
my_school.display_students_list()
print("\n\n")
my_school.display_teachers_list()
print("\n\n")

# 3.soru

class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Rectangle(Shape):
    def area(self):
        return self.width * self.height

class Square(Shape):
    def area(self):
        return self.width * self.width

# Dikdörtgen örneği
rectangle1 = Rectangle(4, 6)
print("dikdortgenin alani:",rectangle1.area())

# # Kare örneği
square1 = Square(5, 5)

print("Kare Alanı:",square1.area ())


# 4.soru

class Taşıt:
    def __init__(self, marka, model, yıl):
        self.marka = marka
        self.model = model
        self.yıl = yıl

class AraziAracı(Taşıt):
    def __init__(self, marka, model, yıl, dört_çeker):
        Taşıt.__init__(self, marka, model, yıl)
        self.dört_çeker = dört_çeker

class SporAraba(Taşıt):
    def __init__(self, marka, model, yıl, maksimum_hız):
        Taşıt.__init__(self, marka, model, yıl)
        self.maksimum_hız = maksimum_hız

# Her sınıftan birer örnek oluşturun
arazi_aracı = AraziAracı("Toyota", "coralla", 1996, True)
spor_araba = SporAraba("Ferrari", "130m", 2023, 270)
print("Arazi Aracı Özellikleri:","\n", arazi_aracı.marka,  arazi_aracı.model, arazi_aracı.yıl, arazi_aracı.dört_çeker)
print("Spor Araba Özellikleri:", "\n",spor_araba.marka, spor_araba.model, spor_araba.yıl, spor_araba.maksimum_hız)


# # Özellikleri görüntülemek için bir program yazın
# print("Arazi Aracı Özellikleri:")
# print("Marka:", arazi_aracı.marka)
# # print("Model:", arazi_aracı.model)
# # print("Üretim Yılı:", arazi_aracı.yıl)
# # print("Dört Çeker:", arazi_aracı.dört_çeker)

# # print("\nSpor Araba Özellikleri:")
# # print("Marka:", spor_araba.marka)
# # print("Model:", spor_araba.model)
# # print("Üretim Yılı:", spor_araba.yıl)
# # print("Maksimum Hız:", spor_araba.maksimum_hız)

# 5.soru
class Müşteri:
    def __init__(self, ad, soyad, tc_kimlik, telefon):
        self.ad = ad
        self.soyad = soyad
        self.tc_kimlik = tc_kimlik
        self.telefon = telefon
    
    def bilgileri_görüntüle(self):
        return f"Adı: {self.ad}, Soyadı: {self.soyad}, TC Kimlik Numarası: {self.tc_kimlik}, Telefon Numarası: {self.telefon}"


class Hesap(Müşteri):
    def __init__(self, ad, soyad, tc_kimlik, telefon, hesap_no, bakiye=0):
        super().__init__(ad, soyad, tc_kimlik, telefon)
        self.hesap_no = hesap_no
        self.bakiye = bakiye
    
    def para_yatır(self, miktar):
        self.bakiye += miktar
        return f"{miktar} TL hesaba yatırıldı. Yeni bakiye: {self.bakiye} TL"
    
    def para_çek(self, miktar):
        if self.bakiye >= miktar:
            self.bakiye -= miktar
            return f"{miktar} TL çekildi. Yeni bakiye: {self.bakiye} TL"
        else:
            return "Yetersiz bakiye. İşlem gerçekleştirilemedi."
    
    def bakiyeyi_görüntüle(self):
        return f"Hesap Bakiyesi: {self.bakiye}"


# Müşteri ve Hesap nesneleri
müşteri1 = Müşteri("omer", "bahtiacik", "1234561", "061234567")
hesap1 = Hesap("omer", "bahtiacik", "1234561", "061234567", "123456789", 1000)

# Müşteri bilgilerini görüntüleme
print(müşteri1.bilgileri_görüntüle())

# Hesap işlemleri
# print(hesap1.bakiyeyi_görüntüle())
# print(hesap1.para_yatır(500))
# print(hesap1.para_çek(200))
# print(hesap1.para_çek(2500))  # Yetersiz bakiye durumu
# print(hesap1.bakiyeyi_görüntüle())


