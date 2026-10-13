class myClass:
	__privateVar = 27;

	def __privMeth(self):
		print("I'm inside class myClass")

	def hello(self):
		print("Private Variable value: ",myClass.__privateVar)



class Computer:
    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price



class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

foo = myClass()
foo.hello()
foo.__privMeth()


c = Computer()
c.sell()

c.__maxprice = 2000
c.sell()

c.setMaxPrice(2200)
c.sell()


p1 = Point(2, 3)
print(p1)