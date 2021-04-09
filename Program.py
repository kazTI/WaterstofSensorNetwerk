from Room import Room
from Network import Network

class Program:

	def __init__(self, url):
		self.rooms = []
		self.network = Network(url)

	def getRooms(self):
		return self.rooms

	def addRoom(self, room):
		self.rooms.append(Room(room['id'], room['length'], room['width'], room['height'], room['sensors']))

	def addRoomsFromNetwork(self):
		rooms = self.network.getRooms()

		for room in rooms:
			self.addRoom(room)

	def createRoom(self, name, width, height, length):
		self.network.createRoom(name, width, height, length)