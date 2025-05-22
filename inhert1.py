class Employe():
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def display_info(self):
        print("employes name is {} and salary is {}".format(self.name, self.salary))

class Manager (Employe):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department = department

    def display_manager_info(self):
        print("manager's name is Priya, salary 85000, department HR")

manager1 = Manager("Priya","85000","HR")
print(manager1.name)
print(manager1.salary)
manager1.display_info()
manager1.display_manager_info()