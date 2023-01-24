import time
from itertools import product
from typing import Any, Generator

def typewriter(text: str) -> Generator[None, None, None]:
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.1)
    print()
typewriter('Welcome to python pin bruteforce key possibilty program |\nThis program takes a passcode length as input and processes the possible pincode and stores it in a text file, which can be used later for bruteforcing \n Credits :\nJoel - Owner\nChatGpt - Helped in typewriter function')
combination = None
def restart():
    global combination
    combination = int(input('Enter passcode length : '))
    key = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
    total_combination = list(product(key, repeat=combination))
    time.sleep(1)
    typewriter('\nThere are {y} combinations for a {x} digit passcode'.format(x=combination, y=len(total_combination)))

    v = total_combination
    pin = '\n'.join([''.join(map(str, i)) for i in v])

    if combination == 4:
        def four():
            txt = open('fourDigitPin.txt', 'w')
            txt.write(pin)
            txt.close()
            time.sleep(1)
        four()
    elif combination == 6:
        def six():
            txt6 = open('sixDigitPin.txt', 'w')
            txt6.write(pin)
            txt6.close()
            time.sleep(1)
        six()
    return combination

restart()

def func():
    global combination
    ask2 = input('\nShall I print the combinations? : ').lower().strip()
    if ask2 == 'yes' and combination== 4:
        txt = open('fourDigitPin.txt', 'r')
        for line in txt:
            typewriter(line)
        typewriter('\nEnd of Line \n\nType "restart()" to restart program')
        txt.close()
    elif ask2 == 'yes' and combination== 6:
        txt = open('sixDigitPin.txt', 'r')
        for line in txt:
            typewriter(line)
        typewriter('\nEnd of Line \n\nType "restart()" to restart program')
        txt.close()
    elif ask2 == 'no' and combination == 4:
        typewriter('\nOk,\nPincode combinations saved to (fourDigitPin.txt) in your device! ')
    elif ask2 == 'no' and combination == 6:
        typewriter('\nOk,\nPincode combinations saved to (sixDigitPin.txt) in your device!')
    else:
        typewriter('\nReply has to be either yes or no')
    time.sleep(1)
    while ask2 != 'yes' and ask2 != 'no':
        func()
    return '\nProgram complete'

func()
def fut():
 while True:
    response = input("\nType 'restart' to run the program again or 'exit' to quit: ").lower().strip()
    if response == 'restart':
      restart()
      func()
    elif response == 'exit':
      break
    else:
      typewriter('\nYou typed something else')
      fut()
fut()
