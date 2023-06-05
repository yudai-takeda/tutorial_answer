import sys
x=sys.argv[1]

#pattern 1
if x.isdigit()==True:
    n = int(x)
    if n % 15==0:
        print('FizzBuzz')
    elif n % 3==0:
        print('Fizz')
    elif n % 5==0:
        print('Buzz')
    else:
        print(x)
else:
    raise ValueError('This is invalid input!')



#pattern 2
x=sys.argv[1]
try:
    x.isdigit()==True
    n = int(x)
    if n % 15==0:
        print('FizzBuzz')
    elif n % 3==0:
        print('Fizz')
    elif n % 5==0:
        print('Buzz')
    else:
        print(x)
except ValueError:
    print('This is invalid input!')
except:
    pass    
