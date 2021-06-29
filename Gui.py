import tkinter as tk
from Room import Room
from Sensor import Sensor
from Obstacle import Obstacle
from Program import Program
from GuiPages import *

CLIENT_NAME = "waterstoffelaars"
PAGES = (
	StartPage,
	EditRoomPage,
	EditSensorPage,
	EditObstaclePage
)
SERVER_URL = "http://localhost:5000"

class Gui(tk.Tk):

	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		self.value = ""

		tk.Tk.wm_title(self, CLIENT_NAME)
		container = tk.Frame(self)

		container.pack(side="top", fill="both", expand = True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)
		self.program = Program(self, SERVER_URL)
		self.frames = {}
		
		for page in PAGES:
			frame = page(container, self)

			self.frames[page] = frame

			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame(StartPage)
		# self.startThreads()
		
	def show_frame(self, cont, post=None):
		frame = self.frames[cont]
		frame.tkraise()
		if cont == StartPage:
			# frame.reload()
			pass
		if post is not None:
			frame.post(post)
		return frame
	
	def setValue(self, value):
		self.value = value
	
	def getValue(self):
		return self.value

	def updateSensorValues(self, sensorValues):
		startPage = self.frames[StartPage]
		startPage.updateSensorValues(sensorValues)
	
	def updateSensorData(self, sensor, room):
		startPage = self.frames[StartPage]
		print(sensor.name)
		startPage.loadSensor(sensor, room)
	
	def updateRoomData(self, room):
		startPage = self.frames[StartPage]
		startPage.loadRoom(room, room.id)

	def updateObstacleData(self, obstacle, room):
		startPage = self.frames[StartPage]
		startPage.loadObstacle(obstacle, room)

	def updateRooms(self):
		startPage = self.frames[StartPage]
		startPage.loadRooms()


	# def startThreads(self):
	# 	self.program.startThreads()