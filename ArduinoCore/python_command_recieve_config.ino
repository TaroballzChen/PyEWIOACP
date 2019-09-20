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
    
    case '@':
      pin_operate(Pause,arrayLength(Pause));
      break;
    
    default:
      command="";
      break;
    }
    
}
