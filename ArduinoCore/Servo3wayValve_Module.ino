void RotateServo(Servo servo, int angle){
  servo.write(angle);
}

void SwitchValveThenRotate(int SwitchValvePin, Servo servo, int angle){
  digitalWrite(SwitchValvePin,HIGH);
  RotateServo(servo,angle);
  delay(1500);
  digitalWrite(SwitchValvePin,LOW);
  delay(300);
}

void FirstReagentInject(){
  SwitchValveThenRotate(FirstValve,Valve,0);
  SwitchValveThenRotate(ThirdValve,Valve,180);
  SwitchValveThenRotate(FourthValve,Valve,90);

  
}

void SecondReagentInject(){
  SwitchValveThenRotate(FirstValve,Valve,180);
  SwitchValveThenRotate(SecondValve,Valve,180);
  SwitchValveThenRotate(ThirdValve,Valve,90);
  SwitchValveThenRotate(FourthValve,Valve,90);
}


void ThirdReagentInject(){
  SwitchValveThenRotate(FirstValve,Valve,180);
  SwitchValveThenRotate(SecondValve,Valve,0);
  SwitchValveThenRotate(FourthValve,Valve,180);
}
