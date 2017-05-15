class InstanceCounter():
    count = 0

    def __init__(self, name, val):
        InstanceCounter.count += 1
        self.name = name
        self.val = self.filterint(val)

    @classmethod   
    def showCounter(cls):
        return(cls.count)    

    @staticmethod
    def filterint(value):
        if not isinstance(value, int):
            return 0 
        else:
            return value            

instance1 = InstanceCounter("Ayush", 22)
instance2 = InstanceCounter("Astha", 26)
print(instance2.count)
instance3 = InstanceCounter("Anita", "Not an Integer")
print(str(instance3.val) + " is the value of Instance 3")
print(instance2.count)
print("Global Instance Count: " + str(InstanceCounter.count))
print("Global Instance Count from Decorated Class method : " + str(InstanceCounter.showCounter()))







