S = input()
for plus in range(0, len(S)):
   if S[plus] == '+':
      number1 = int(S[0: plus])
      number2 = int(S[plus + 1 : len(S)])
      
      print(number1 + number2)
