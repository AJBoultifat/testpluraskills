import random

List = []

for i in range(0, int(1000)):
    n = random.randint(0,1000)
    List.append(n)

print(List)

i = 0
for l in List:
    if((l%3 == 0) and (l%5 == 0)): print(str(i) +': '+ str(l) + ' is FizzBuzz')
    if(l%5 == 0): print(str(i) +': '+str(l) +' is Buzz')
    if(l%3 == 0): print(str(i) +': '+str(l) +' is Fizz')
    if((l%3 != 0) and (l%5 != 0)): print(str(i) +': '+str(l))
    i = i + 1
    
    