class Person:
	#not a constructor
	def __init__(self,name):
		self.name=name
	def say_hi(self):
		print('My name is :',self.name)
p=Person('Shivam')
p.say_hi()
Person.say_hi(p)

#  Functions Like init are called Dunders or Magic Function

# Every Dunder start with __

# __init__(self)
#__del__(self)
#__add__(self,other)    #a+b->a.__add__(b)
#__str__(self)          #-> String Representation : a.__str__()
#__eq__(self,other)     #-> a==b: a.__eq__(b)

class Car:
	def __init__(self,model,mileage):
		self.model=model
		self.mileage=mileage
	def __str__(self):
		return f"{self.model} {self.mileage}"
	def __repr__(self):
		return f"{self.model}"

	def __eq__(self,other):
		return self.mileage==other.mileage

	def __add__(self,other):
		return self.mileage+other.mileage

c1=Car('a',2)
c2=Car('b',2)

print(c1+c2)
print(c1==c2)
print(repr(c1))
print(str(c1))

# how to make cout<<"Shivam" work on Python

class Output:
	def __lshift__(self,other):
		print(other,end=" ")
		return self

cout=Output()
cout<<"Shivam"<<"Bhat"<<"My Name"

# Example of how referencing takes place

class dog:
	tricks=[] #Problem with declaring outside __init__ therefore declare inside __init__

	def __init__(self,name):
		self.name=name

	def add_trick(self,trick):
		self.tricks.append(trick)

a=dog('Tuffy')
a.add_trick('Fetch')
a.add_trick('Run')

print(a.tricks)

b=dog('Mapple')
print(b.tricks)
