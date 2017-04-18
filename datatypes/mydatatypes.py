def data_type(arg):
  if type(arg) is str:
    return len(arg)
  elif arg is None:
    return 'no value'
  elif type(arg) is bool:
    return arg
  elif type(arg) is int:
    if arg > 100:
      return 'more than 100'
    elif arg < 100:
      return 'less than 100'
    elif arg == 100:
      return 'equal to 100'
  elif type(arg) is list:
    if len(arg) < 3:
      return None
    else:
      return arg[2]
  else:
    raise TypeError("Unexpected data type")
