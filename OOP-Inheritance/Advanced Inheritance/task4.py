class Employee:
    def work(self):
        print('Employee is working')

class Manager(Employee):
    def work(self):
        print('Manager is managing the team')

manager1 = Manager()
manager1.work()

class Developer(Employee):
    def work(self):
        print('Developer is writing code')

dev1 = Developer()
dev1.work()