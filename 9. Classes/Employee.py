class Employee:
    '所有'
    empCount = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

if __name__ == '__main__':
    print(Employee.__doc__)
    print(Employee.__dict__)
    print(Employee.__name__)
    print(Employee.__class__)