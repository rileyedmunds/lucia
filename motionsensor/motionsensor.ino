// motion-transmitter
// 
// Read binary HIGH/LOW values from motion sensor and print them to serial port as 0 or 1

#include "Arduino.h"


int sensorPin = 2; //connect the sensor to pin 2

void setup()
{
  // initialize serial communication
  Serial.begin(9600); 

  //set the motion sensor to take input
  pinMode(sensorPin, INPUT); 
}

void loop()
{
  // read input value
  int val = digitalRead(sensorPin);  

  if (val == HIGH) {
    Serial.print("1");
    delay(8000); //wait for the python program to run
  } else {
    //nothing detected:
    Serial.print("0");
  }
  //dont' sleep here, so we have a responsive motion sensor
}
