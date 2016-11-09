class fraction(object):
	def __init__(self,x,y):
		self.x = x
		self.y = y
		
	def __add__(self,other):
		x = (self.x * other.y) + (other.x * self.y)
		y = (self.y * other.y)
		z = x // y
		f = x % y
		if z == 0:
			return (f,y)
		if z != 0:
			return z,(f,y)
		
	def __mul__(self,other):
		x = self.x * other.x
		y = self.y * other.y
		z = x // y
		f = x % y
		if z == 0:
			return (f,y)
		if z != 0:
			return z,(f,y)
			

if __name__ == '__main__':
a = fraction(1,2)
b = fraction(3,4)


c = a + b
d = a * b

print(c)
print(d)
