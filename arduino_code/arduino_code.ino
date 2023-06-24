#include "SoftwareSerial.h"

// making serial communication
SoftwareSerial serial_connection(10, 11);

// setup for recieving the data
#define BUFFER_SIZE 64//This will prevent buffer overruns.
char inData[BUFFER_SIZE];//This is a character buffer where the data sent by the python script will go.
char inChar=-1;//Initialie the first character as nothingt
int i=0;

// Ultrasonic sensor pin setup
const int trigPin  = 3;
const int echoPin = 2;
long duration;
int distance;

// Full Indicator
const int LED = 7;


// Config variable
char code[] = "TP05BIRENDRA01";  // TP + _ward_no_ + _tole_fname_ + _serial_number
bool isReady = false;


void setup()
{
  Serial.begin(9600);
  serial_connection.begin(9600);
  serial_connection.println("Ready!!!");
  Serial.println("Started");
  
  // pin  mode setup for Ultrasonic sensor 
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(LED, OUTPUT);
  

}
void loop()
{
  
  digitalWrite(LED,LOW);
  // Calculating the distance
  // clearing the sensor  
  digitalWrite(trigPin, LOW);
  delay(2);

  // making the wave
  digitalWrite(trigPin, HIGH);
  delay(10);
  digitalWrite(trigPin, LOW);

  // receving the duration
  duration = pulseIn(echoPin, HIGH);

  // measuring the distance
  distance = duration * 0.034 /2;

  
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println("cm");
  delay(100);



  if (distance <=15){
    digitalWrite(LED, HIGH);
  }
  // validating
  if (isReady == true)
  {
    if (distance <= 15 )
    {
    serial_connection.print(code);
    serial_connection.println(" FULL");
    }
    else {
      serial_connection.print(code);
      serial_connection.println(" NOTFULL");
    }
    // else if ((distance >= 35) && (distance <= 50))
    // {
    // serial_connection.print(code);
    // serial_connection.println(" HALF");
    // }
    
    // else if (distance > 50)
    // {
    // serial_connection.print(code);
    // serial_connection.println(" EMPTY");
    // }
    // else{
    //   serial_connection.println("None");
    // }   
  }




  //This will prevent bufferoverrun errors
  byte byte_count=serial_connection.available();//This gets the number of bytes that were sent by the python script
  if(byte_count)//If there are any bytes then deal with them
  {
    Serial.println("Incoming Data");//Signal to the monitor that something is happening
    int first_bytes=byte_count;//initialize the number of bytes that we might handle. 
    int remaining_bytes=0;//Initialize the bytes that we may have to burn off to prevent a buffer overrun
    if(first_bytes>=BUFFER_SIZE-1)//If the incoming byte count is more than our buffer...
    {
      remaining_bytes=byte_count-(BUFFER_SIZE-1);//Reduce the bytes that we plan on handleing to below the buffer size
    }
    for(i=0;i<first_bytes;i++)//Handle the number of incoming bytes
    {
      inChar=serial_connection.read();//Read one byte
      inData[i]=inChar;//Put it into a character string(array)
    }
    inData[i]='\0';//This ends the character array with a null character. This signals the end of a string
    



    // checking for device configuration (CODE SETUP
    if (String(inData) == "connected")
    {
      isReady = true;
    }

    for(i=0;i<remaining_bytes;i++)//This burns off any remaining bytes that the buffer can't handle.
    {
      inChar=serial_connection.read();
    }
  }
  delay(10);//Pause for a moment 
}