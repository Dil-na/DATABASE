# public

# class Employee:
#     def __init__(self):
#         self.name = "Anu"
#         self.salary = 25000

#     def show_details(self):
#         print("Name:", self.name)
#         print("Salary:", self.salary)


# emp = Employee()

# print(emp.name)
# print(emp.salary)

# emp.show_details()

# protected

class Employee:
    def __init__(self):
        self._department = "IT"
        self._salary = 30000


class Manager(Employee):
    def show_details(self):
        print("Department:", self._department)
        print("Salary:", self._salary)
obj = Manager()
obj.show_details()

# private
class BankAccount:
    def __init__(self):
        self.__balance = 50000

    def show_balance(self):
        print("Account Balance:", self.__balance)


account = BankAccount()

account.show_balance()