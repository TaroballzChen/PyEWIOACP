#include <avr/pgmspace.h>

#define CH595 48
#define arrayLength(arr) (sizeof((arr))/sizeof((arr)[0]))

String command = "";
const int latch = 5;
const int clock_pin = 6;
const int data_pin = 7;
const int output[] = {latch,clock_pin,data_pin};
int len = arrayLength(output);

void setup() {
  Serial.begin(9600);
  Serial.println("Ready");
  pinmode_init(output);
}

void pinmode_init(const int pinList[]){
  for(int i=0;i<len;i++){
    pinMode(pinList[i],OUTPUT);
    digitalWrite(pinList[i],LOW);
  }
}
  

void loop() {
  python_command();
  channel_select(command);
  command = '@';
}


void python_command() {
  if (Serial.available()){
  command="";
  delay(1);

  while(Serial.available()){
    command+=(char)Serial.read();
    }
  Serial.println(command);
  }

}


int calc_bit(char num,int i){
    switch (num){
    case 1:
        return (1<<(i*2));
    case -1:
        return (1<<(i*2+1));
    case 0:
        return 0;
    default:
        return 0;  
    }
}

void pin_operate(const char control_array[],int array_length){
  int line = array_length/CH595;
  for(int i=0;i<line;i++){
    digitalWrite(latch,LOW);
    int z = CH595*(i+1);
    for(int j=0;j<CH595/4;j++){
        z -= 4;
        int res = 0;
        for (int k=0;k<4;k++){
            char data = pgm_read_word_near(control_array + (z+k));
            res += calc_bit(data,k);
        }
    shiftOut(data_pin,clock_pin,MSBFIRST,res);
    }
    digitalWrite(latch,HIGH);
    delay(1500);
  }
}
