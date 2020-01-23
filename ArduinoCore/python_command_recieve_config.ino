void channel_select(String str){
  switch (str[0]){
    
    case 'b':
      pin_operate(b,arrayLength(b));
      break;
      
    case 'x':
      pin_operate(x,arrayLength(x));
      break;
      
    case 'm':
      pin_operate(m,arrayLength(m));
      break;

    case 'n':
      pin_operate(n,arrayLength(n));
      break;
      
    case 'c':
      pin_operate(c,arrayLength(c));
      break;

    case 'd':
      pin_operate(d,arrayLength(d));
      break;
    
    case 'e':
      pin_operate(e,arrayLength(e));
      break;

    case 'f':
      pin_operate(f,arrayLength(f));
      break;

    case 'g':
      pin_operate(g,arrayLength(g));
      break;
    
    case 'h':
      pin_operate(h,arrayLength(h));
      break;
      
    case 'i':
      pin_operate(i,arrayLength(i));
      break;
      
    case 'j':
      pin_operate(j,arrayLength(j));
      break;
      
    case 'k':
      pin_operate(k,arrayLength(k));
      break;

    case 'l':
      pin_operate(l,arrayLength(l));
      break;

    case 'a':
      pin_operate(a,arrayLength(a));
      break;
    
    case '@':
      pin_operate(Pause,arrayLength(Pause));
      break;

   // switch Magenetic 
    case '=':
      Switch_ServoMagnetic();
      break;


   // switch pump
//   case '.':
//      Switch_SyringeMotor1();
//      break;
//
//   case '#':
//      Switch_SyringeMotor2();
//      break;
    
    default:
      command="";
      break;
    }
    
}
