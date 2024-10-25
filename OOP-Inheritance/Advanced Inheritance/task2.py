class Camera:
    def take_photo(self):
        print('Taking a photo...')

class Phone:
    def  make_call(self):
        print('Making a phone call...')

class Smartphone(Camera, Phone):
    pass

Smartphone1 = Smartphone()
Smartphone1.take_photo()
Smartphone1.make_call()
