class Employee:

    raise_coef = 1.05                               #   raise_coef attribute in Employee class
    num_emp = 0                                     #   num_emp attribute in Employee class

    def __init__(self, name, last, age, pay):       #   Instance method of the class
        self.name = name                            #   Instance variables
        self.last = last                            #   .
        self.age = age                              #   .
        self.pay = pay                              #   .
        Employee.num_emp += 1                       #   Increases num_emp value for each instance created

    def apply_raise(self):
        self.pay = self.pay * self.raise_coef       #   "self.raise_coef" yerine "Employee.raise_coef" ile 
                                                    #   "raise_coeff" attribute değerine class üzerinden de    
                                                    #   erişilebilir         

emp_1 = Employee("Oğuz", "Drader", "34", 1000)      #   Employee class türünden emp_1 object'i tanımlanır
emp_2 = Employee("Arda", "Arizona", "30", 2000)     #   Employee class türünden emp_2 object'i tanımlanır

class IT(Employee):                                 #   "IT" --> child/sub class, "Employee" --> parent/super class
    pass                                            #   Even IT does not have any attributes, it inherits all from superclass


it_1 = IT("OG","DRD","35",3000)
print(it_1.__dict__)
print(it_1.name)
#help(it_1)

it_1.apply_raise()
print(it_1.pay, it_1.raise_coef)

class IT(Employee):                                 #   "IT" inherits from "Employee"
    raise_coef = 1.2                                #   "IT" has its own attribute called "raise_coef" 

it_1 = IT("OG","DRD","35",3000)
it_1.apply_raise()
print(it_1.pay, it_1.raise_coef)


class IT(Employee):                                 #   "IT" inherits from "Employee"
    raise_coef = 1.2                                #   "IT" has its own attribute called "raise_coef" 
    def __init__(self, name, last, age, pay, lang): #   "IT" içinde __init__ fonksiyonu tanımlanır
        super().__init__(name, last, age, pay)      #   super class'ın __init__ içindeki attributeları alınır
        self.lang = lang                            #   "IT" class'ına ait __init__ içine yeni bir attribute eklenir

class IK(Employee):
    raise_coef = 1.3                                
    def __init__(self, name, last, age, pay, experience):
        super().__init__(name, last, age, pay)      
        self.experience = experience                #   "IK" class'ına ait __init__ içine yeni bir attribute eklenir

    def print_exp(self):                            #   "IK" class'ına ait yeni bir method "print_exp" eklenir
        print(f"This employee has {self.experience} years of experience")

ik_1 = IK("AG","ARZ","30",4000, 12)
ik_1.print_exp()

print(isinstance(ik_1, IK))
print(isinstance(ik_1, Employee))
print(issubclass(IK, Employee))
print(issubclass(IT, Employee))
print(issubclass(IT, IK))