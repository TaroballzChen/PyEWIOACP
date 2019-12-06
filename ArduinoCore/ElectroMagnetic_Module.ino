void Switch_ElectroMagnetic(){
  switch (IsMagEnable) {
    case false:
      delay(500);
      digitalWrite(electroMagpin,HIGH);
      break;
    case true:
      digitalWrite(electroMagpin,LOW);
      break;
  }
  IsMagEnable = !IsMagEnable;
}

void Switch_ServoMagnetic(){
  switch (IsServoMagEnable) {
    case false:
      myservo.write(90);
      delay(15);
      break;
    case true:
      myservo.write(170);
      delay(15);
      break;
  }
  IsServoMagEnable = !IsServoMagEnable;
}
