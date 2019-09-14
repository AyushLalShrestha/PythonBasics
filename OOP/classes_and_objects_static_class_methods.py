class InstanceCounter(object):
    count = 0

    def __init__(self, name, val):
        # InstanceCounter.count += 1
        self.name = name
        self.val = self.filterint(val)
        # print self.__private_method()

    @classmethod   
    def showCounter(cls):
        return (cls.count)

    @staticmethod
    def filterint(value):
        if not isinstance(value, int):
            return 0
        return value

    def __private_method(self):
        return self.name

    def some_instance_method(self, value):
        return self.filterint(value)

instance1 = InstanceCounter("Ayush", 22)
instance2 = InstanceCounter("Astha", 26)
# print(InstanceCounter.count)
instance3 = InstanceCounter("Anita", "Not an Integer")
# print("The value of Instance 3 is %s" %instance3.val)
print(InstanceCounter.count)
# print("Global Instance Count: " + str(InstanceCounter.count))
# print("Global Instance Count from Decorated Class method : " + str(InstanceCounter.showCounter()))
# print dir(instance3)

print instance2.some_instance_method(22)
print instance1.count







