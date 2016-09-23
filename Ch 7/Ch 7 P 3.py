def moon_weight():
    print('Please enter your current weight below:')
    w = float(input())

    print('''Thank you
Now, please enter on average how much your weight will increase each year''')
    gw = float(input())

    print('And lastly, please enter the number of years below')
    y = int(input())
    y = y + 1
    for year in range(0, y):
        wom = w * 0.165
        print('Year-%s %s' % (year, wom))
        w = w + gw

# The code above is what I would've done but in the chapter it said to use
# the sys.stdin.readline() so the code below does that.

import sys

def moon_weight():
    print('Please enter your current weight below:')
    w = float(sys.stdin.readline())

    print('''Thank you
Now, please enter on average how much your weight will increase each year''')
    gw = float(sys.stdin.readline())

    print('And lastly, please enter the number of years below')
    y = int(sys.stdin.readline())
    y = y + 1
    for year in range(0, y):
        wom = w * 0.165
        print('Year-%s %s' % (year, wom))
        w = w + gw
