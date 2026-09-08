#dictionaries
'''cars = {
    "lightning mcqueen" : 1500,
    "honey badger" : 1200,
    "ferrari" : 1800
}
cars = dict(sorted(cars.items(),key = lambda item : item[1],reverse=True))
print(cars) '''

#objects
class car :
    def __init__(self,name,cc):
        self.name = name
        self.cc = cc
    
    def __repr__(self):
        return f"{self.name} : {self.cc}"

cars = [
    car("ferrari",3500),
    car("mclaren",2800),
    car("mercedes",3600)
]

cars = sorted(cars,key = lambda car : car.cc)
print(cars)