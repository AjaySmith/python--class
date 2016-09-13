print('''For this first practice it is going to print "hello 0"
because it says that if the value of 'x' is less than 9 to break.''')

for x in range(0, 20):
    print('hello %s' % x)
    if x < 9:
        break
