class Commission:
    rate = 0.5
    def __init__(self, agent_name, property_type, gross_salary):
        self.agent_name = agent_name
        self.property_type = property_type
        self.gross_salary = gross_salary

    def incentive(self):
        commission = Commission.rate * self.gross_salary
        print(f'Agent Name: {self.agent_name}')
        print(f'Property Type: {self.property_type}')
        print(f'Gross Salary: {self.gross_salary}')
        print(f'Total Commission: {commission}')

emp1 = Commission('Joseph OKOLIMO', 'Land', 25000000)
emp1.incentive()
emp2 = Commission('Okullo Job', 'House', 4000000)
emp2.incentive()