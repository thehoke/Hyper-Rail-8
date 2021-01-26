//Master board that recieves joystick inputs

#include<Wire.h>

//transmission data
int data;

//x-axis
int joyFront = 0;
int joyBack = 0;

//y-axis
int joyLeft = 0;
int joyRight = 0;

//z-axis
int joyUp = 0;
int joyDown = 0;

void setup() {
 
  Wire.begin();
 
  for(int i = 1; i<7; i++){
    
    pinMode(i,OUTPUT);
    digitalWrite(i, HIGH);
  }

  for(int j = 7; j < 13; j++){
    pinMode(j, INPUT);
  } 
}

void loop() {
   joyFront = digitalRead(7);
   joyBack = digitalRead(8);

   joyLeft = digitalRead(9);
   joyRight = digitalRead(10);
  
   joyUp = digitalRead(11);
   joyDown = digitalRead(12);

   if (joyFront == HIGH)
    data = 1;

   else if (joyBack == HIGH)
    data = 2; 
   
   else if (joyLeft == HIGH)
    data = 3;

   else if (joyRight == HIGH)
    data = 4; 

   else if (joyUp == HIGH)
    data = 5;

   else if (joyDown == HIGH)
    data = 6; 
    
   else 
    data = 0; 

  Wire.beginTransmission(9);
  Wire.write(data);          
  Wire.endTransmission(); 
         
}
