//Code for the slave board
#include<Wire.h>

int data;

void setup() {

  for (int i=2; i<8; i++)
  pinMode (i, OUTPUT);   //Connect LEDs

  Wire.begin(9);//9 here is the address
  Wire.onReceive(receiveEvent);
  Serial.begin(9600);
  
}
void receiveEvent(int bytes) {
  data = Wire.read();//Receive value from master board

}

void loop(){

 if (data == 0){

  for (int i=2; i<8; i++)
   digitalWrite(i, LOW);
 }
  
 else if (data == 1)
  digitalWrite(2, HIGH);

 else if (data == 2)
  digitalWrite(3, HIGH);

 else if (data == 3)
  digitalWrite(4, HIGH);

 else if (data == 4)
  digitalWrite(5, HIGH);

 else if (data == 5)
  digitalWrite(6, HIGH);

 else if (data == 6)
  digitalWrite(7, HIGH);
}
