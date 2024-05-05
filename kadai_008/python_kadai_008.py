import random

var = random.randint(0, 1000)

if var % (3 * 5) == 0:
    print("FizzBuzz", var)
elif var % 3 == 0:
    print("Fizz", var)
elif var % 5 == 0:
    print("Buzz", var)
else:
    print(var)
