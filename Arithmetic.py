def arithmetic_arranger(xs, solve = 0):
  first = ""
  sec = ""
  third = ""
  fourth = ""
  if len(xs) > 5: return "Error: Too many problems."
  for x in xs:
    y = x.split()
    v1, operator, v2 = y[0], y[1], y[2]
    if operator == "/":
      return "Error: Operator must be '+' or '-'."
    elif operator == "*":
      return "Error: Operator must be '+' or '-'."
    try:
      i1 = int(v1)
      i2 = int(v2)
    except:
      return "Error: Numbers must only contain digits."
      break
    if len(v1) > 4 or len(v2) > 4:
      return "Error: Numbers cannot be more than four digits."
    if len(v1)+ 2 > len(v2) + 2:
      dash = len(v1)+2
    else:
      dash = len(v2) + 2

    #ajuste para direita
    top = v1.rjust(dash)
    mid = v2.rjust(dash-1)
    if operator == "+":
      resultado = i1 + i2
    else:
      resultado = i1 - i2
    bot = str(resultado).rjust(dash)
    dash = "-" * dash

    if x != xs[-1]:
      first += top+"    "
      sec += operator+mid+"    "
      third+=dash+"    "
      fourth += bot+"    "
    else:
      first += top
      sec += operator+mid
      third += dash
      fourth += bot
  if solve == 0:
    problems = first+"\n" + sec+"\n" + third
  else: 
    problems = first+"\n" + sec+"\n" + third+"\n" +fourth
  return problems 
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"],True))

