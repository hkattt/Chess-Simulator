// string to store incoming data
String data = ""; 

void setup() {
  // put your setup code here, to run once:
  pinMode(LED_BUILTIN, OUTPUT);
  // opens the serial monitor
  Serial.begin(9600);  
}

void loop() {
  // checks if data is being received 
  if (Serial.available() > 0) {
    // stores incoming data in the data variable
    data = Serial.readString();
    // indexing the data (this was for testing purposes)
    if (data[0] == '0') {
      digitalWrite(LED_BUILTIN, HIGH);
      delay(3000); 
    }
    
    if (data[1] == '1') {
      digitalWrite(LED_BUILTIN, LOW);
      delay(3000);
    }
  }
}
