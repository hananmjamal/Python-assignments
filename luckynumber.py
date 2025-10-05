import random

lnum=random.randint(1,100)

attempt=0
maxattempt=7
while(attempt<maxattempt):
    attempt += 1
    num = int(input('Enter a number'))

    if num>lnum:
        print("Price too high")

    elif num<lnum:
        print("Price too low")
    else:
        print('Congratulations! You found the lucky number in',maxattempt-attempt, 'attempts')
        print(lnum)
if attempt==maxattempt and num!=lnum:
    print("Youve failed to gues it right. Better Luck next time!")
    print(lnum)

