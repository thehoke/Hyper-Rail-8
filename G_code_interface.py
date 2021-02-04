
import serial
import serial.tools.list_ports
import time

def main():

    #look for arduino port

    ports = list(serial.tools.list_ports.comports())
    
    flag = 0

    for p in ports:
        if 'Arduino' in p.description:
            uno = serial.Serial(p.name, 115200)
            flag += 1

    if(flag == 0 ):
        print("No Arduino found")
        return 0

    #start machine class variables
    rail = machine()
    
    #flush arduino serial monitor
    uno.flushInput()

    #get input
    getinput(uno, rail)
   
def getinput(uno, rail):
    #print UI
    print("1. Change speed\n2. To get current position\nType Gcode commands, numbers above or exit to exit:")


    #get user input
    while True:
        print(":", end = " ")
        uinput = input()

        if (uinput.lower() == "exit"):
            break
        elif (uinput == "1"):       #Set Step size
            changestep(uno, rail)
        elif uinput == "2":         #get current position
            getcurrentpos(uno)
        elif uinput == "3":         #stop motors
            uno.write('\x18'.encode())
        else:                       #send gcode or m code or coordinates
            uno.write(uinput.encode())
            uno.write('\n'.encode())

def getcurrentpos(uno):
    #send command to get position
    uno.write("?".encode())
    uno.write('\n'.encode())

    notok = True
    #read until position is sent from arduino
    while notok == True:
        temp = uno.readline()
        if "MPos" in temp.decode():
            notok = False

    #print position
    print(temp.decode())

def changestep(uno,rail):
    #print current step and get input for new step size
    print("the current step size is " + str(rail.x_step))
    print("Type the step size you want: ", end = " ")
    uinput = input()

    #set step size for all motors

    rail.set_step(int(uinput))
    
    x = "$100 = " + str(uinput)     #x step

    uno.write(x.encode())
    uno.write('\n'.encode())
    time.sleep(.3)

    y = "$101 = " + str(uinput)     #y step

    uno.write(y.encode())
    uno.write('\n'.encode())
    time.sleep(.3)

    z = "$102 = " + str(uinput)     #z step

    uno.write(z.encode())
    uno.write('\n'.encode())
    time.sleep(.3)

    print("Step size chagned to " + str(rail.x_step))

def set_xmax(self,uno):
        print("Current X max = " + str(self.x_max))
        print("Enter new X max:", end = " ")
        
        uin = input()

        self.x_max = int(uin)

        w = "$130 = " + str(uin)

        uno.write(w.encode())
        uno.write('\n'.encode())

        print("X max chagned to " + str(self.x_max))

class machine():
    def __init__(self):
        self.x_max = 300
        self.y_max = 300
        self.z_max = 300

        self.x_step = 600
        self.y_step = 600
        self.z_step = 600

    def set_x_max(self, max):
        self.x_max = max

    def set_y_max(self, max):
        self.y_max = max

    def set_z_max(self, max):
        self.z_max = max

    def set_step(self, step):
        self.x_step = step
        self.y_step = step
        self.z_step = step



if __name__ == "__main__":
    main()

