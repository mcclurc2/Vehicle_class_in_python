#main.py

from vehiclePackage.vehicleClass import *

if __name__ =="__main__":
    #instantiate an object if type vehicle
    myCorvette = Vehicle("car", 120) #trigger a call to constructor
    myCorvette.printType() #invoke
    
    #invoke the getter for maxiumum speed, store the reutrn valye in a variable
    #print
    maximum_speed = myCorvette.getSpeed()
    print("Maximum speed:", maximum_speed)
    #instanitiate another vehicle object. you can name it
    myLexus = Vehicle("car")
    
    #i want a list of three vehicles: car, boat, spaceship
    #i want some friendly output to demo your works
    # you can pcik the name and properties
    myVehicles = [Vehicle("lexus", 150)
                  , Vehicle("millinium falcon", 4000)
                  , Vehicle("Mastercraft", 40)]
    for vehicle in myVehicles:
        vehicle.printType()
        print(vehicle.getSpeed())
        