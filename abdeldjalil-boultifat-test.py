
import random
from calculation import calculate as cal

'''List void'''
List = []

'''Filing the list with int random value for 1000 times'''
for i in range(0, int(1000)):
    n = random.randint(0,1000)
    List.append(n)

    
'''Print the list to confirm that it is well appended'''
print('The list :')
print(List)
print('Calculate :')
cal.functionTest(List)

