from threading import Thread
import time
import random

class SocketClient(Thread):
    def __init__(self, serverUrl, program, room, socketconn):
        self.program = program
        self.serverUrl = serverUrl
        self.room = room
        self.socketconn = socketconn
        self.running = False
        self.counter = 0
        Thread.__init__(self)
        self.roomId = str( self.room.getId() )
        self.roomName = self.room.getName()
        self.daemon = True
        # self.getRoomData()
    
    def run(self):
        # self.socketconn.getAllRooms( self.room.getId() )
        self.socketconn.createRoom(self.roomId, self.roomName)
        self.socketconn.deleteRoom(self.roomId, self.roomName)
        self.running = True
        while self.running:
            time.sleep(10)
            self.counter += 1
            self.updateSensorValue()
            self.updateRoomData()

    def updateSensorValue(self):
        sensorValues = []
        for sensor in self.room.getSensors():
            sensorValues.append({'id':sensor.getId(),
            'value':random.random()})
        self.program.updateSensorValue(self.room.getId(), sensorValues)
    
    def updateRoomData(self):
        # !!!Get roomdata (sensor, obstacles, size LBH,id, )
        roominfo = self.getRoomData()
        self.program.updateRoomData(self.room.getId(), roominfo)

    ### 1 socket verbinding bij program - alle rooms worden gemaakt)
    ### Create && delete rooms gebeurt bij program
    ### Alle rooms vragen zelf om updates, edits, delete sensoren of obstacles
    ### get alle rooms from server & print

    def getRoomData(self):
        return self.socketconn.getAllRooms() 
    #     return {
    #     "height": 40,
    #     "id": 3,
    #     "length": 50,
    #     "name": "test",
    #     "obstacles": [
    #         {
    #             "id": 1,
    #             "name": f"test {str(self.counter)}",
    #             "x1": 23,
    #             "x2": 23,
    #             "y1": 23,
    #             "y2": 23,
    #             "z1": 23,
    #             "z2": 23
    #         }
    #     ],
    #     "sensors": [
    #         {
    #             "id": 1,
    #             "name": f"test {str(self.counter)}",
    #             "x": 30,
    #             "y": 20,
    #             "z": 10
    #         },
    #         {
    #             "id": 2,
    #             "name": "test",
    #             "x": 32,
    #             "y": 23,
    #             "z": 23
    #         },
    #         {
    #             "id": 3,
    #             "name": "test",
    #             "x": 36,
    #             "y": 23,
    #             "z": 23
    #         },
    #         {
    #             "id": 4,
    #             "name": "test",
    #             "x": 12,
    #             "y": 12,
    #             "z": 12
    #         },
    #         {
    #             "id": 5,
    #             "name": "test",
    #             "x": 21,
    #             "y": 24,
    #             "z": 23
    #         }
    #     ],
    #     "width": 50
    # }