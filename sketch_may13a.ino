#include <AFMotor.h>

AF_Stepper motor(4096, 2);
String readserial;

void setup() {
  Serial.begin(115200);           // set up Serial library at 9600 bps

  motor.setSpeed(100);  // 10 rpm
  motor.release();
  delay(1000);
}

void loop() {
    while(!Serial.available()) {}
  while (Serial.available())
  {
    if (Serial.available() >0)
    {
      readserial = Serial.readString();
    }
  }
  Serial.println(readserial);
  String sp = readserial.substring(0,readserial.indexOf('C'));
  String dr = readserial.substring(readserial.indexOf('C'),readserial.indexOf('W')+1);
  String st = readserial.substring(readserial.indexOf('W')+1);
  motor.setSpeed(sp.toInt());
  if (dr == "CW")
  motor.step(st.toInt(), FORWARD, SINGLE);
  if (dr == "CCW") 
  motor.step(st.toInt(), BACKWARD, SINGLE); 
  delay(10);
  char ard_sends = '1';
  Serial.println("Done!");
  Serial.flush();
}
