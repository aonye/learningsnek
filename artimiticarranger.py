def arithmetic_arranger(problems, boolean="False"):
  storedtext = ""
  # check if the number of arguments is valid
  if (len(problems)>5):
    return "Error: Too many problems."
  #check for invalid operator
  for math in problems:
    add = math.find('+')
    subtract = math.find('-')
    if (add==-1 and subtract==-1):
      return "Error: Operator must be '+' or '-'."
    txt = math.split()

    #check for non-digits
    try:
      number1 = int(txt[0])
      number2 = int(txt[2])
    except:
      return "Error: Numbers must only contain digits."
    if (number1 > 9999 or number2 > 9999): #check for too many digits
      return "Error: Numbers cannot be more than four digits."

    #sum or subtract
    if(subtract==-1): #add bc the sign is not subtract
      result = number1 + number2
    if (add==-1): #subtract bc sign is not add
      result = number1 - number2

    # figure out size of biggest operand and allocate spaces accordingly


    if (boolean==False):
      if (number1>number2):
        arranged_problems = "{:>}\n{} {:>}\n----\n".format(txt[0],txt[1],txt[2])
      else:
        arranged_problems = "{:>}\n{} {:>}\n----\n".format(txt[0],txt[1],txt[2])

    else:
      arranged_problems = "{:>}\n{} {:>}\n----\n{:>}\n".format(txt[0],txt[1],txt[2],result)
    storedtext = storedtext + "    " + str(arranged_problems)

  return storedtext
