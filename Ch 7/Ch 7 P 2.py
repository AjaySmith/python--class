def moon_weight(w, gw, y):
    for year in range(0, y + 1):
        wom = w * 0.165
        print('Year-%s %s' % (year, wom))
        w = w + gw

moon_weight(47, 0.68, 3)
