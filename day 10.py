#ph keypad using dictionary
kp={2:['a','b','c'],3:['d','e','f'],4:['g','h','i'],5:['j','k','l'],6:['m','n','o'],7:'pqrs',8:['t','u','v'],9:'wxyz'}
key=int(input('key:'))
click=int(input('clicks:'))
if key==7 or key==9:
    print(kp[key][click%4-1])
else:
    print(kp[key][click%3-1])

    
