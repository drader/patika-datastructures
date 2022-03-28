class Employee:                     #   Class oluşturma
    pass                            #   Class'ın boş olacağını belirtir

e = Employee()                      #   Employee class türünde bir e object'i oluşturulur

e.a = 4                             #   e object'ine a isminde bir attribute eklenir ve değeri 4'e eşitlenir

print(e.a)                          #   Employee class türündeki e object'inin a attribute değerini yazdırır

#####################################

class Employee:

    raise_coef = 1.05                               #   raise_coef attribute in Employee class
    num_emp = 0                                     #   num_emp attribute in Employee class

    def __init__(self, name, last, age, pay):       #   Instance method of the class
        self.name = name                            #   Instance variables
        self.last = last                            #   .
        self.age = age                              #   .
        self.pay = pay                              #   .
        Employee.num_emp += 1                       #   Increases num_emp value for each instance created

    def fullname(self):                             #   Regular method of a class
        print(f"{self.name} {self.last}")           #   İlk input olarak instance object'i (self) alır

    def apply_raise(self):
        self.pay = self.pay * self.raise_coef       #   "self.raise_coef" yerine "Employee.raise_coef" ile 
                                                    #   "raise_coeff" attribute değerine class üzerinden de erişilebilir 

    @classmethod                                    #   Classmethod ilk input olarak instance yerine class referansı alır
    def set_raise(cls, amount):                     #   Classmethod dekoratörü ile tanımlanan method instance ile
        cls.raise_coef = amount                     #   erişilebilir olduğundan class'a ait herhangi bir
                                                    #   attribute değeri bu metod ile güncellenebilmektedir
    @classmethod
    def from_string(cls, emp_str):
        name, last, age, pay = emp_str.split("-")
        return cls(name, last, int(age), float(pay))

    @staticmethod                                   #   Class içinde otomatik olarak hiçbir input almayan methodlardır
    def holiday_print(day):                         #   İlk input olarak otomatik olarak class referansı alktarılır
        if day == "weekend":
            print("This is an off day")
        else:
            print("This is not an off day")

print(Employee.num_emp)
emp_1 = Employee("Oğuz", "Drader", "34", 1000)      #   Employee class türünden emp_1 object'i tanımlanır
print(Employee.num_emp)
emp_2 = Employee("Arda", "Arizona", "30", 2000)     #   Employee class türünden emp_2 object'i tanımlanır
print(Employee.num_emp)


print(emp_1.name)                                   #   emp_1 object'inin name attribute değeri yazdırılır
emp_2.fullname()                                    #   Call of the class method
print(emp_1.raise_coef)                             #   raise_coeff attribute değerine instance object ile erişim
print(Employee.raise_coef)                          #   raise_coeff attribute değerine class üzerinden erişim

print(emp_1.pay, emp_2.pay)
emp_1.apply_raise()                                 #   emp_1 object'ine apply_raise metodu uygulanır
emp_2.apply_raise()                                 #   emp_2 object'ine apply_raise metodu uygulanır
print(emp_1.pay, emp_2.pay)

print(emp_1.__dict__)                               #   __dict__ ile instance object'in attribute değerleri return edilir
print(Employee.__dict__)                            #   __dict__ ile Employe class'ına ait attribute değerleri return edilir

emp_1.experience = 10                               #   instance object'ine "experience" atribute'u eklenip 10 değeri verilir

print(emp_1.__dict__)

print(emp_1.raise_coef, emp_2.raise_coef, Employee.raise_coef)
Employee.raise_coef = 1.07                          #   Class içindeki raise_coeff değeri güncellenir
print(emp_1.raise_coef, emp_2.raise_coef, Employee.raise_coef)
emp_1.raise_coef = 1.03                             #   Instance içinde raise_coeff adında bir attribute oluşturulur
print(emp_1.raise_coef, emp_2.raise_coef, Employee.raise_coef)
Employee.raise_coef = 1.04                          #   raise_coef class üzerinden güncellenir

#   Instance içinde raise_coef olduğundan, class güncellemesinden etkilenmez
print(emp_1.raise_coef, emp_2.raise_coef, Employee.raise_coef)  
Employee.set_raise(2.3)                             #   Class üzerinden class method ile attribute güncelleme
print(emp_1.raise_coef, emp_2.raise_coef, Employee.raise_coef)
emp_1.set_raise(2.9)                                #   Instance üzerinden class method ile attribute güncelleme
print(emp_1.raise_coef, emp_2.raise_coef, Employee.raise_coef)

emp_1_str = "James-Hughes-32-5000"                  #   Attribute için string türünde input alınır
emp_2_str = "Charlie-Brown-22-3000"

print(emp_1_str.split("-"))

name, last, age, pay = emp_1_str.split("-")         #   Alınan string parse edilir ve değişkenlere atanır

emp_1 = Employee(name, last, age, pay)              #   ilgili değişkenler ile instance object güncellenir


emp_1_str = "Oğuz-Hughes-35-5000"                   #   Attribute için string türünde input alınır
emp_2_str = "Arda-Brown-22-3000"

emp_1 = Employee.from_string(emp_1_str)             #   Class üzerinden class method ile attribute güncellenir
emp_2 = Employee.from_string(emp_2_str)             #   Instance üzerinden class method ile attribute güncelleme

print(emp_1.name)
print(emp_2.name)

Employee.holiday_print("weekend")

emp_1 = Employee("James", "Gençer", "34", 4000)

emp_1.holiday_print("working day")


