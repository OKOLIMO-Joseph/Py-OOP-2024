class Universities:

    def __init__(self, name, location, abbreviation, branches=1):
        self.name = name
        self.location = location
        self.abbreviation = abbreviation
        self.branches = branches

    def __str__(self) -> str:
        return(f'Name: {self.name} Location: {self.location} Abbreviation: {self.abbreviation} Branches: {self.branches}')

uni1 = Universities('Uganda Christian University', 'Mukono', 'UCU', 5)
uni2 = Universities('Makerere University', 'Kampala', 'MUK', 10)
uni3= Universities('Kampala Internatinal University', 'Kansanga', 'KIU', 4)
uni4 = Universities('Victoria University', 'Kampala', 'VU')
uni5 = Universities('Cavendish University', 'Kabalagala', 'CU', 3)

# unies = Universities[('Uganda Christian University', 'Mukono', 'UCU', '5 campuses'), ('Makerere University', 'Kampala', 'MUK', '10 campuses'), ('Kampala Internatinal University', 'Kansanga', 'KIU')]

# uni1.__str__()
# uni2.__str__()
# uni3.__str__()

print(uni1)
print(uni5)