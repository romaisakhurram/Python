
class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def __str__(self):
        return f"Name: {self.name}, ID: {self.employee_id}"

class Department:
    def __init__(self, department_name, employee):
        self.department_name = department_name
        self.employee = employee 

    def __str__(self):
        return f"Department Name: {self.department_name}, Employee: {self.employee}"

if __name__ == "__main__":
    emp = Employee("Uzair", 101)
    dept = Department("HR", emp)

    print(dept)
