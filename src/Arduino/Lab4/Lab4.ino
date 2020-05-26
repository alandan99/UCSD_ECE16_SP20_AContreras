#include "BluetoothSerial.h"
#include <Wire.h>
BluetoothSerial SerialBT;
long sampling_rate = 50; //sampling rate in Hz
unsigned long last_sample_time = 0; //microsecond of last sample
unsigned long start_sample_time = 0; 

void setup() {
  // put your setup code here, to run once:
  setupMssg();
  initDisplay();
  setupADC();
  setupHR();
}

void loop() {
  // put your main code here, to run repeatedly:
  Lab3_Ch5();
}

void Lab3_Ch5(){
    receiveMessage(); //checks for serial message
    sendData(); //sends data via serial if suppose to
    
}
