//VARIABLE INITIALIZE--
unsigned long sampling_delay = calcSamplingDelay(sampling_rate); //microseconds between samples
bool sending_data = false; //to send data?
//bool receive_data = false;
char in_text[64];                // Character buffer
int in_text_index = 0;
//SEND DATA--
void sendData(){
   if(sending_data){
     last_sample_time = micros();//update last_sample_time with current micros()
     //last_sample_time = millis();
     if(last_sample_time - start_sample_time >= sampling_delay){
        readADC();
        readHR();
        printBTData();
        start_sample_time = last_sample_time;
        delay(1);  
        }
    }
}
//FIND PERIOD SAMPLE--
long calcSamplingDelay(long sampling_rate){
    long period_us = 1000000/sampling_rate;
    //long period_ms = (1/sampling_rate)*1000;
    return period_us; //number of microseconds to wait between samples
    //return period_ms;
}
//SETUP MESSAGE--
void setupMssg() {
  SerialBT.begin("Alan_Adafruit");
  //Serial.begin(115200);
   
}
//  RECEIVE-->CHECK MSSG  //
int checkMessage(){
  int i = 0;
  String message = String(in_text); // converts in_text into a string
  if (message == "start data"){// Check if the message is “stop data” or “start data”
    sending_data = true; // set sending_data according to the message received 
    
    delay(1000);//delay for 1 second after setting send_data to true.
    i = 0;
  }
  else if(message =="stop data"){
    sending_data = false; 
    delay (10);
    i = 1;
  }
  return i;
}

void receiveMessage(){
  if (SerialBT.available() > 0) {
  //if (Serial.available() > 0) {  
    char incomingChar = SerialBT.read();// read byte from Serial
    //char incomingChar = Serial.read();// read byte from Serial
    if (incomingChar == '\n'){//the incoming char is the new line char
       int r = checkMessage();
       showMessage(in_text, r, true);//show the in_text on the OLED with showMessage()
      in_text_index = 0;//reset the in_text index back to 0
      memset(in_text,0,20); // this will clear the in_text buffer
     
    }
    else{
      in_text[in_text_index] = incomingChar; //assign in_text[index] to the incoming char
      in_text_index += 1 ;//increment the index
    }
  }
}

//--PRINT ADC--//
void printBTData(){
   SerialBT.print(last_sample_time);
   SerialBT.print(", ");
   SerialBT.print(x_val);
   SerialBT.print(", ");
   SerialBT.print(y_val);
   SerialBT.print(", ");
   SerialBT.print(z_val);
   SerialBT.print(", ");
   SerialBT.println(HR_Data);
}
//void printData(){
//   Serial.print(last_sample_time);
//   Serial.print(", ");
//   Serial.print(x_val);
//   Serial.print(", ");
//   Serial.print(y_val);
//   Serial.print(", ");
//   Serial.print(z_val);
//   Serial.print(", ");
//   Serial.println(HR_Data);
//}
