int accelZ = A4;
int accelY = A3;//assign pin value
int accelX = A2;//assign pin value

int z_val = 0;//set to 0
int y_val = 0;//set to 0
int x_val = 0;//set to 0
//--ADC SETUP--//
void setupADC(){
  //setup each accel pins to be an input pin
  pinMode(accelZ, INPUT);
  pinMode(accelY, INPUT);
  pinMode(accelX, INPUT);
}
//--READ ADC--//
void readADC(){
  //read each accel pin and assign value to the corresponding Val
  z_val = analogRead(accelZ);
  y_val = analogRead(accelY);
  x_val = analogRead(accelX);
}
