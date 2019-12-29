def devider_generator(number, x=1):
    while True:
        if number % x == 0:
            yield x
        x += 1
        if x > number:
            break

            
deviders = devider_generator(1024)
for i in deviders:
    print(i)
