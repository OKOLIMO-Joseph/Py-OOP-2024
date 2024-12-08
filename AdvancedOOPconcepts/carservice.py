from abc import ABC, abstractmethod

class Service(ABC):
    @abstractmethod
    def make_service(self, motor_type):
        pass

class OilChange(Service):
    def make_service(self, motor_type):
        print(f'Oil Change service on a : {motor_type}')

class TyreChange(Service):
    def make_service(self, motor_type, number_of_tyres):
        print(f'Tyre change service on a: {motor_type}')
        print(f'Number of tyres: {number_of_tyres}')

class EngineRepair(Service):
    def make_service(self, motor_type):
        print(f'Engine Repair Service on a : {motor_type}')

service1 = OilChange()
service1.make_service('Honda Motorcycle')
print(sep='\n')

service2 = TyreChange()
service2.make_service('Subaru', 3)
print(sep='\n')

service3 = EngineRepair()
service3.make_service('Premo')