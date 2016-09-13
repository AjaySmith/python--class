w = 68
gw = 1

for year in range(0, 16):
    wom = w * 0.165
    print('Year-%s: %s' % (year,wom))
    w = w + gw
    
"w stands for 'weight', gw for 'gained weight', wom for 'weight on moon'"
