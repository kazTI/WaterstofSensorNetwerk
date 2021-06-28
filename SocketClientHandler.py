import socketio
import json


class SocketClientHandler():
    #Initialize socketIO client
    sio = socketio.Client(logger=False, engineio_logger=False)

    def __init__(self, program):
        #Start connect, print info and send message 
        self.program = program
        self.sio.connect('http://localhost:5001')
        self.sio.on('sendAllRooms', self.handleGetRooms)
        self.sio.on('updateSensorValue', self.handleUpdateSensorValue)
        self.sio.on('sendARoom', self.roomHandler)
        self.sio.on('sendASensor', self.sensorHandler)
        self.sio.on('sendAObstacle', self.obstacleHandler)
        self.sio.on('sendSensorValue', self.sensorValueHandler)
    #Default socketIO events
    #-------------------------------------------------------------------------#
    @sio.event
    def connect():
        print('Connected with SocketIO server')

    @sio.event
    def connect_error(data):
        print("Connection with SocketIO server failed!")

    @sio.event
    def disconnect():
        print('Disconnected from SocketO server')

    @sio.event
    def message(data):
        print('Message from SocketIO server: ' + data)

    @sio.event
    def json(data):
        print('Message from SocketIO server: ' + data)

    def handleGetRooms(self, data):
        rooms = json.loads(data)
        self.program.updateRooms(rooms)

    def handleUpdateSensorValue(self, data):
        sensorValues = json.loads(data)
        self.program.updateSensorValue(1, sensorValues)
    
    def roomHandler(self, data):
        room = json.loads(data)
        self.program.handleRoom(room)

    def sensorHandler(self, data):
        sensor = json.loads(data)
        self.program.handleSensor(sensor)

    def obstacleHandler(self, data):
        obstacle = json.loads(data)
        self.program.handleObstacle(obstacle)
    
    def sensorValueHandler(self, data):
        sensorValues = json.loads(data)
        self.program.updateSensorValues(sensorValues)
    #-------------------------------------------------------------------------#

    @sio.event
    def sendMessage(self, data):
        self.sio.emit('message', data)
    
    @sio.event
    def getAllRooms(self):
        self.sio.emit('getAllRooms')

    @sio.event
    def ready(self):
        self.sio.emit('ready')
    
    def createRoom(self, name, width, height, length):
        rawData = {
            'name': name,
            'width': width,
            'length': length,
            'height': height,
        }
        data = json.dumps(rawData)
        self.sio.emit('createRoom', data)

    def editRoom(self, id, name, width, height, length):
        rawData = {
            'id': id,
            'name': name,
            'width': width,
            'length': length,
            'height': height,
        }
        data = json.dumps(rawData)
        self.sio.emit('editRoom', data)



    def createSensor(self, roomId, name, x, y, z):
        rawData = {
            'room_id': roomId,
            'name': name,
            'x': x,
            'y': y,
            'z': z
        }
        data = json.dumps(rawData)
        self.sio.emit('createSensor', data)

    def createObstacle(self, roomId, name, x1, y1, z1, x2, y2, z2):
        rawData = {
            'room_id': roomId,
            'name': name,
            'x1': x1,
            'y1': y1,
            'z1': z1,
            'x2': x2,
            'y2': y2,
            'z2': z2
        }
        data = json.dumps(rawData)
        self.sio.emit('createObstacle', data)

    def editSensor(self, id, name, x, y, z):
        rawData = {
            'id': id,
            'name': name,
            'x': x,
            'y': y,
            'z': z
        }
        data = json.dumps(rawData)
        self.sio.emit('editSensor', data)

    def editObstacle(self, id, name, x1, y1, z1, x2, y2, z2):
        rawData = {
            'id': id,
            'name': name,
            'x1': x1,
            'y1': y1,
            'z1': z1,
            'x2': x2,
            'y2': y2,
            'z2': z2
        }
        data = json.dumps(rawData)
        self.sio.emit('editObstacle', data)

# socketconn = SocketClientHandler()
# print('my sid is', socketconn.sio.sid)

# socketconn.my_event('TestRoom')
# socketconn.EnterRoom('TestRoom')
# socketconn.createRoom(socketconn.sio.sid, 'test')
# socketconn.deleteRoom(socketconn.sio.sid, 'test')
# socketconn.EnterRoom(socketconn.sio.sid, 'test2')
# socketconn.sendMessage('teleurgesteld')