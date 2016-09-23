def moon_weight(w, gw):
    for year in range(0, 16):
        wom = w * 0.165
        print('Year-%s: %s' % (year, wom))
        w = w + gw
        
moon_weight(36, 0.55)
