class Animal(object):
    """Makes cute animals."""
    is_alive = True
    health = "good"
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def description(self):
        print self.name
        print self.age
        
hippo = Animal("Tom", 12)
sloth = Animal("Sid", 5)
ocelot = Animal("Gir", 2)
Animal.description(hippo)
    
print hippo.health
print sloth.health
print ocelot.health
