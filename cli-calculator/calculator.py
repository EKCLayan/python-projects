
while True:
   print("CLI Calculator Running")
   number1 = input("number1: ")
   if number1 == "exit":
     break
   try:
     number1 = int(number1)
   except ValueError:
     print("NOT A NUMBER!")
     continue
   number2 = input("number2: ")
   if number2 == "exit":
     break
   try:
     number2 = int(number2)
   except ValueError:
     print("NOT A NUMBER!")
     continue
   function = input("function: ")
   if function == "exit":
     break
  

   if function == "m":
     value = number1 * number2

   elif function == "d":
     if number2 == 0:
      print("MATH ERROR!")
      continue
     else:
      value = number1/number2

   elif function == "a":
     value = number1 + number2

   elif function == "s":
     value = number1 - number2
   else:
     print("ERROR!")
     continue

   print(value)
