'''A Class that allows to calculate the devisers of a list'''
'''Calculation'''
class calculate(object):
    @staticmethod
    def functionTest(List):
        i = 0
        for l in List:
            if((l%3 == 0) and (l%5 == 0)): print(str(i) +': '+ str(l) + ' is FizzBuzz')
            if(l%5 == 0): print(str(i) +': '+str(l) +' is Buzz')
            if(l%3 == 0): print(str(i) +': '+str(l) +' is Fizz')
            if((l%3 != 0) and (l%5 != 0)): print(str(i) +': '+str(l))
            i = i + 1
