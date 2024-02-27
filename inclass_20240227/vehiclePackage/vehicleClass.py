#vehicle.py

class Vehicle:
    '''
    Vehicle Class
    this clas model a vehicle on a used car lot
    change order: we need to add maxiumum speed to the model
    change order: need a way to 'read' the maximu speed from the model
    change order: some developers need to use a constructor wihtout having to provide a max speed
    '''
    #constructor it is called when... when we instantiate an object of vehicle type
    def __init__(self, type, max_speed = None):
        '''
        param type: the kind of vehicle
        param max_speed: max of the vehicle, defaults to none
        '''
        self.type = type;
        self._thisisprivate = 42 #this is a weak attempt to 'support' data hiding
        self.max_speed = max_speed
        #a instanve method. it operates on an instance of the vehicle class
    def printType(self):
        print(self.type);
        
    def getSpeed(self): #a getter
            return self.max_speed
if __name__ == "__main__":
# Some code to test the class would go here.
# If there's no code, just pass
    pass

