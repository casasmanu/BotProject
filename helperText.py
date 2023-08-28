def prepareText(upvalue:bool,user:str,actPrize:int):
 
 output=''
 if upvalue:
  output=('$'+str(actPrize)+
  ' - SUBIO \n'
  'Precio VENTA obtenido de infodolar')
 else:
  output=('$'+str(actPrize)+
  ' - BAJO \n'
  'Precio VENTA obtenido de infodolar')

 return output