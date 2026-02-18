const int trigPin = 9;
const int echoPin = 10;

void setup() {
  Serial.begin(9600); 
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop() {
  long duration;
  int distance;

  // Clear the trigPin
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  // Trigger the sensor for 10 microseconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH);

  distance = duration * 0.034 / 2;

  // Send distance to Python (only if valid)
  if (distance > 0 && distance < 400) {
    Serial.println(distance);
  }
  
  // Wait 100ms so we don't spam the computer
  delay(100); 
}