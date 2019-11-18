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
    
    default:
      command="";
      break;
    }
    
}
