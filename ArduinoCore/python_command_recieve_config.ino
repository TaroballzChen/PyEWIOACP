void channel_select(String str){
  switch (str[0]){
    case 'a':
      pin_operate(a,arrayLength(a));
      break;
    
    case 'b':
      pin_operate(b,arrayLength(b));
      break;

    case 'c':
      pin_operate(c,arrayLength(c));
      break;
      
    case 'd':
      pin_operate(d,arrayLength(d));
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
    
    case '@':
      pin_operate(Pause,arrayLength(Pause));
      break;
    
    default:
      command="";
      break;
    }
    
}
