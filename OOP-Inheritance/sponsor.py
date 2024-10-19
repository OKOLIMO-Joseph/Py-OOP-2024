class Sponsor:
    def __init__(self, name, slang):
        self.name = name
        self.slang = slang

    def  display_info(self):
        print(f"Sponsor: {self.name}")
        print(f"Slang: {self.slang}")

Sponsor1 = Sponsor('Nike', 'Just Do It!')
Sponsor1.display_info()
