const int transistorPin = 7; // the pin that the base is attached to
int incomingByte;      // a variable to read incoming serial data into

void setup()
{
  // initialize serial communication:
  Serial.begin(9600);
  // initialize the LED pin as an output:
  pinMode(transistorPin, OUTPUT);
}

void loop()
{
  // see if there's incoming serial data:
  if (Serial.available() > 0)
  {
    // read the oldest byte in the serial buffer:
    incomingByte = Serial.read();
    if (incomingByte == '1')
    {
      digitalWrite(transistorPin, HIGH);
    }
    if (incomingByte == '0')
    {
      digitalWrite(transistorPin, LOW);
    }
  }
}