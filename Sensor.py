class Sensor:
	
	def __init__(self, id):
		self.id = id
		self.value = 0.0
		self.x = 0
		self.y = 0
		self.z = 0

	'''returns the current value stored in the sensor object'''
	def getValue(self):
		return self.value

	'''Takes a float and changes the current value of the sensor object'''
	def setValue(self, value):
		self.value = value

	'''returns a tuple with 3 ints containing the current stored location of the sensor object'''
	def getLocation(self):
		return (self.x, self.y, self.z)

	'''Takes 3 ints and changes the current stored location of the sensor object'''
	def setLocation(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

	'''returns a string with the id stored in the Sensor object'''
	def getId(self):
		return self.id