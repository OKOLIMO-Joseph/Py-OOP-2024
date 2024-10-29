base_salary = 1000000
overtime = 40
rate = 250000

def get_wage(base_salary, overtime, rate):
    return base_salary + (overtime*rate)

print(f'Your salary: {get_wage(base_salary, overtime, rate)}')