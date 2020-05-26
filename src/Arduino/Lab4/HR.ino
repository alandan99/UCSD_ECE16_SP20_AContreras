#include <Wire.h>
#include "MAX30105.h"

MAX30105 particleSensor;
int HR_Data;

void setupHR(){
  // Initialize the sensor (begin & setup for RED, 50Hz, 12-bit)
  if (!particleSensor.begin(Wire, I2C_SPEED_FAST)) //Use default I2C port, 400kHz speed
  {
    SerialBT.println("MAX30105 was not found. Please check wiring/power. ");
    while (1);
  }
  byte ledBrightness = 0x0F; //Options: 0=Off to 255=50mA
  byte sampleAverage = 1; //Options: 1, 2, 4, 8, 16, 32
  byte ledMode = 1; //Options: 1 = Red only, 2 = Red + IR, 3 = Red + IR + Green
  int sampleRate = 50; //Options: 50, 100, 200, 400, 800, 1000, 1600, 3200
  int pulseWidth = 411; //Options: 69, 118, 215, 411
  int adcRange = 4096; //Options: 2048, 4096, 8192, 16384

  particleSensor.setup(ledBrightness, sampleAverage, ledMode, sampleRate, pulseWidth, adcRange); //Configure sensor with these settings
  // Do not setup Serial since that is handled in the Message tab
  // Do not include the plotting part of the code

//  const byte avgAmount = 64;
//  long baseValue = 0;
//  for (byte x = 0 ; x < avgAmount ; x++)
//  {
//    baseValue += particleSensor.getRed(); //Read the RED value
//  }
//  baseValue /= avgAmount;
//  //Pre-populate the plotter so that the Y scale is close to RED values
//  for (int x = 0 ; x < 500 ; x++)
//    Serial.println(baseValue);
}

int readHR(){
  HR_Data = (particleSensor.getRed()); //get HR pulse data (RED LED)
  return HR_Data;
}
