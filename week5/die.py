class Die:
    def __init__(self, one, two, three, four, five, six):
        self.one = one
        self.two = two
        self.three = three
        self.four = four
        self.five = five
        self.six = six

    def roll(self):
        print(self.one, 'has shown up')
        print(self.two, 'has shown up')
        print(self.three, 'has shown up')
        print(self.four, 'has shown up')
        print(self.five, 'has shown up')
        print(self.six, 'has shown up')

die1 = Die('1', '2', '3', '4', '5', '6', )
die1.roll()