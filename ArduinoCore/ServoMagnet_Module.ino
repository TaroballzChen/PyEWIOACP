//ElectroMagnetic Module

bool IsServoMagEnable = false;

void Switch_ServoMagnetic(){
  switch (IsServoMagEnable) {
    case false:
      RotateServo(MagnetServo,90);
      break;
    case true:
      RotateServo(MagnetServo,170);
      break;
  }
  IsServoMagEnable = !IsServoMagEnable;
}
