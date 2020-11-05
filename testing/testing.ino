String data = "";

void setup() {
  // put your setup code here, to run once:
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);  
}

void loop() {
  if (Serial.available() > 0) {
    data = Serial.readString();
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
