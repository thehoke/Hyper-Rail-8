
import serial
import serial.tools.list_ports

def main():

    ports = list(serial.tools.list_ports.comports())
    
    flag = 0

    for p in ports:
        if 'Arduino' in p.description:
            uno = serial.Serial(p.name, 115200)
            flag += 1

    if(flag == 0 ):
        print("No Arduino found")
        return 0

    rail = machine()
    
    uno.flushInput()

    uno.readline()
    uno.readline()

    print("1. Change speed\n2. To get current position\nType Gcode commands, numbers above or exit to exit:")

    getinput(uno, rail)
   
def getinput(uno, rail):

    while True:
        print(":", end = " ")
        uinput = input()

        if (uinput.lower() == "exit"):
            break
        elif (uinput == "1"):
            changestep(uno, rail)
        elif uinput == "2":
            getcurrentpos(uno)
        else:
            uno.write(uinput.encode())
            uno.write('\n'.encode())

def getcurrentpos(uno):
    uno.write("?".encode())
    uno.write('\n'.encode())

    notok = True

    while notok == True:
        temp = uno.readline()
        if "ok" not in temp.decode():
            notok = False


    print(temp.decode())

def changestep(uno,rail):
    print("the current step size is " + str(rail.x_step))
    print("Type the step size you want: ", end = " ")
    uinput = input()

    rail.set_step(int(uinput))
    
    w = "$100 = " + str(uinput)

    uno.write(w.encode())
    uno.write('\n'.encode())

    w = "$101 = " + str(uinput)

    uno.write(w.encode())
    uno.write('\n'.encode())

    w = "$102 = " + str(uinput)

    uno.write(w.encode())
    uno.write('\n'.encode())

    print("speed chagned to " + str(rail.x_step))


class machine():
    def __init__(self):
        self.x_max = 300
        self.y_max = 300
        self.z_max = 300

        self.x_step = 600
        self.y_step = 600
        self.z_step = 600

    def set_step(self, step):
        self.x_step = step
        self.y_step = step
        self.z_step = step



if __name__ == "__main__":
    main()

