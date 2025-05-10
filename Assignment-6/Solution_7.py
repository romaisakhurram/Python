
class Employee:
    def __init__(self , name , salary , ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

    def get_ssn(self):
        return self.__ssn
    
    def set_salary(self , new_salary):
        if new_salary > 0:
            self._salary = new_salary
        else:
            print("Salary must be positive")

    def dispaly(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self._salary}")
        print(f"SSN: {self.__ssn}")

class Manager(Employee):
    def __init__(self , name , salary , ssn , department):
        super().__init__(name , salary , ssn)
        self.department = department

    def show_manager_info(self):
        print(f"Manager: {self.name}")
        print(f"Protected Salary: {self._salary}")
        print(f"SSN: {self.get_ssn()}")
        print(f"Department: {self.department}")

m = Manager("Ali" , "12000" , "123-345-6789" , "HR")
m.show_manager_info()
m.set_salary(80000)

print(f"Updated Salary: {m._salary}")

print("SSN via managed:", m._Employee__ssn)


    


        