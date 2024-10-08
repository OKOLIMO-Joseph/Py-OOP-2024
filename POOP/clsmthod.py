class Football:
    team = 'Arsenal'

    def __init__(self, epl_position):
        self.epl_position = epl_position 

#Decalring the class method
    @classmethod
    def my_team(cls):
        return cls.team

# Passing on the class method onto the classs itself
print(Football.my_team()) 
