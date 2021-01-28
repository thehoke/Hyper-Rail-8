
import serial
import time

def main():

    uno = serial.Serial('COM3', 115200)

    rail = machine()

    uno.flushInput()
    while True:

        uinput = getinput()

        if(uinput.lower() == "exit"):
            break

        uno.write(str(uinput).encode())
        uno.write('\n'.encode())

        #grbl_out = uno.readline() # Wait for grbl response with carriage return
        #time.sleep(.1)
        #print(grbl_out.decode())

   
def getinput():
   

    uinput = input()

    return uinput

class machine():
    def __init__(self):
        self.x_max = 300
        self.y_max = 300
        self.z_max = 300

        self.x_speed = 600
        self.y_speed = 600
        self.z_speed = 600

    def set_speed(self, speed):
        self.x_speed = speed
        self.y_speed = speed
        self.z_speed = speed



if __name__ == "__main__":
    main()