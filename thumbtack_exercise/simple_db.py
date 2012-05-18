def main():
  com_dict = {}
  set = 'SET'
  get = 'GET'
  unset = 'UNSET'
  equalto= 'EQUALTO'
  end = 'END'
  begin = 'BEGIN'
  rollback = 'ROLLBACK'
  commit = 'COMMIT'
  
  commandline = raw_input('')
  command_arr = commandline.split()
  command = command_arr[0]
  
  output = []
  dict = {}
  while(command != end):
    if command == set:
      var, val = command_arr[1:]
      dict[var] = val
    
    elif command == get:
      var = command_arr[1]
      if var in dict:
        print dict[var]
      else:
        print 'NULL'

    elif command == unset:
      var = command_arr[1]
      if var in dict:
        del dict[var]

    elif command == equalto:
      val = command_arr[1]
      print find_keys(val, dict)

    commandline = raw_input('')
    command_arr = commandline.split()
    command = command_arr[0]

    #print 'dict: ' + str(dict)
    # for begin, make a list of commands and pointers for the next begin block

def find_keys(val, dict):
  matches = []
  for k, v in dict.items():
    if v == val:
      matches.append(k)
  
  if len(matches) == 0:
    output = 'NONE'
  else:
    output = ' '.join(matches)

  return output
  
if __name__ == '__main__':
  main()
