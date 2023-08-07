
import math

data = list()

def is_prime(number):
   
    if number <= 1:
        return False
    number_sqrt = int(math.sqrt(number)) 
    divisors = range(2, (number_sqrt + 1))
 
    for element in divisors:
        if number % element == 0:
            return False
    return True


with open("task01.txt", "r", newline='\n', encoding = "UTF-8") as file:

    for item in file:

        a = int(item)

        if is_prime(a):

            b = a*2 + 1

            if is_prime(b):

                data.append(b)


print(len(data))
        
            




