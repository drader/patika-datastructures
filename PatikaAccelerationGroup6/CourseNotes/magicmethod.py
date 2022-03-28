# Class içinde __xxx__ gibi tanımlanan methodlara magicmethod ya da dunder denir. Bazı built-in davranışları değiştirebilir

class Employee:

    raise_coef = 1.05                               #   raise_coef attribute in Employee class
    num_emp = 0                                     #   num_emp attribute in Employee class

    def __init__(self, name, last, age, pay):       #   Instance method of the class
        self.name = name                            #   Instance variables
        self.last = last                            #   .
        self.age = age                              #   .
        self.pay = pay                              #   .
        Employee.num_emp += 1                       #   Increases num_emp value for each instance created

    def __str__(self):                              #   __str__ magic method
        return f"Employee(name={self.name}, last={self.last}, age={self.age}, pay={self.pay})"

    def __add__(self, other):                       #   __add__ magic method
        return self.pay + other.pay                 #   returns --> sum of pays for two objects of class

    def __len__(self):                              #   __len__ magic method
        return len(self.name)                       #   returns --> length of the name of the class object

    def apply_raise(self):
        self.pay = self.pay * self.raise_coef       #   "self.raise_coef" yerine "Employee.raise_coef" ile 
                                                    #   "raise_coeff" attribute değerine class üzerinden de    
                                                    #   erişilebilir         

emp_1 = Employee("Oğuz", "Drader", "34", 1000)      #   Employee class türünden emp_1 object'i tanımlanır
emp_2 = Employee("Arda", "Arizona", "30", 2000)     #   Employee class türünden emp_2 object'i tanımlanır

emp_3 = Employee("OG", "Drd", "35", 3000)
print(emp_3)

print(emp_1 + emp_3)